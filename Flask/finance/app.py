import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
db.execute("""
CREATE TABLE IF NOT EXISTS stocks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price numeric NOT NULL,
    total numeric NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
""")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


"""Index page showing transaction history for each symbol"""
@app.route("/")
@login_required
def index():
    transactions = db.execute("SELECT symbol, SUM(shares) as total_shares, price, SUM(total) as total_value FROM stocks WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0;",
                              session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total = cash + sum(transaction["total_value"] for transaction in transactions)
    return render_template("index.html", transactions=transactions, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        if not request.form.get("symbol") or not lookup(request.form.get("symbol")):
            return apology("Missing symbol", 400)
        if  not (request.form.get("shares")).isnumeric() or float(request.form.get("shares")) - int(request.form.get("shares")) != 0 or int(request.form.get("shares")) < 1 :
            return apology("must provide natural number of shares", 400)
        price = float(lookup(request.form.get("symbol"))["price"]) * int(request.form.get("shares"))
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if price > cash:
             return apology("You do not have enough cash to complete the transaction", 400)
        else:
            db.execute("INSERT INTO stocks (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)",\
            session["user_id"], request.form.get("symbol").upper(), int(request.form.get("shares")),\
            lookup(request.form.get("symbol"))["price"], int(request.form.get("shares")) * lookup(request.form.get("symbol"))["price"])

            # Calculate the new cash balance after the purchase
            remaining_cash = cash - price
            # Update the user's cash balance in the database
            db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        current_password = request.form.get("current_password")
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        if not check_password_hash(rows[0]["hash"], current_password):
            return apology("invalid username and/or password", 403)

        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        if new_password != confirm_password:
            return apology("The passwords are not identical", 403)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new_password), session["user_id"])
        return redirect("/")

    else:
        return render_template("change_password.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT symbol, shares, price , timestamp FROM stocks WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        quote = lookup(request.form.get("symbol"))
        if quote:
            return render_template("quote.html",quote=quote)
        else:
            return apology("Invalid symbol", 400)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirm password", 400)

        elif not request.form.get("password") == request.form.get("confirmation"):
                    return apology("The passwords are not identical", 400)

        existing_usernames = [row['username'] for row in db.execute("SELECT username FROM users")]
        if request.form.get("username") in existing_usernames:
            return apology("The username is already in use", 400)


        # Query database for username
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)",request.form.get("username"), generate_password_hash(request.form.get("password")))
        return redirect("/")

    else:
        return render_template("register.html")

"""Sell shares of stock"""
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        submitted_symbol = request.form.get("symbol")
        submitted_shares = int(request.form.get("shares"))

        # Retrieve the stock information using the submitted symbol
        stock_info = lookup(str(submitted_symbol))
        if stock_info is None:
            return apology("must provide valid symbol", 400)

        # Retrieve the user's shares for the submitted symbol
        user_shares = db.execute("SELECT shares FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], submitted_symbol)[0]["shares"]
        if int(submitted_shares) > int(user_shares):
            return apology("not enough shares to sell", 400)

        # Calculate the total value of the sold shares
        total_value = stock_info["price"] * submitted_shares

        # Update the database to reflect the sale
        db.execute("INSERT INTO stocks (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], submitted_symbol, -submitted_shares,
                   stock_info["price"], total_value)

        # Update the user's cash balance
        user_info = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]
        remaining_cash = user_info["cash"] + total_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])

        flash("Sale successful", "success")  # Flash a success message
        return redirect("/")
    
    else:
        symbols= db.execute("SELECT symbol FROM stocks WHERE user_id = ? GROUP BY symbol HAVING shares > 0;",session["user_id"])
        return render_template("sell.html", symbols=symbols)
