len ,sum1, head = 0, 0, 0
n = int(input("number: "))

while n > 1:
    dig = n % 10
    n = n // 10
    if len % 2 == 1:
        dig *= 2
        if dig >=  10:
            sum1 = sum1 + ( dig // 10 ) + (dig % 10)
        else:
            sum1 += dig

    else:
        sum1 += dig

    len += 1

    if 9 < n < 100:
        head = n

if sum1 % 10 != 0 or len < 13 or len > 16 or len == 14:
    print("INVALID")

elif len == 15  and (head == 34 or head == 37):
    print("AMEX")

elif len == 16 and 50 < head < 56:
   print("MASTERCARD")

elif (len == 13 or len == 16) and (head // 10 == 4):
   print("VISA")

else:
    print("INVALID")
