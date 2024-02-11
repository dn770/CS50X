from restaurant import Restaurant
from management_system import ManagementSystem

def restaurant_declaration():
    print("Wellcome to Restaurant Management System.")
    name = input("Please insert restaurant's name: ")
    address = input("Please insert restaurant's address: ")
    phone_number = input("Please insert restaurant's phone number: ")
    description = input("Please insert restaurant's description: ")
    print("Thank you.")
    return name, address, phone_number, description


def tables_declaration(management_system):
    for num in range(1, int(input("Please insert number of tables\n"))+1):
        cap = int(input(f"Please insert capacity of table {num}\n"))
        management_system.add_table(cap)


def menus_declaration(management_system):
    for num in range(1, int(input("Please insert number of menus\n"))+1):
        menu_type = input(f"insert type of menu {num}\n")
        management_system.add_menu(menu_type)


def menu_items_declaration(management_system):
    for menu in management_system.menus:
        for num in range(1, int(input(f"Please insert number of items for menu {menu.menu_id}\n"))+1):
            title = input(f"insert title of item {num}\n")
            desc = input(f"insert description of item {num}\n")
            price = float(input(f"insert price of item {num}\n"))
            menu.add_menu_item(title, desc, price)


def customers_declaration(management_system):
    for num in range(1, int(input("Please insert number of customers\n"))+1):
        name = input(f"insert name of customer {num}\n")
        contact_number = input(f"insert contact number of customer {num}\n")
        management_system.add_customer(name, contact_number)


def initial_boot():
    name, address, phone_number, description = restaurant_declaration()
    management_system = ManagementSystem(name, address, phone_number, description)
    tables_declaration(management_system)
    menus_declaration(management_system)
    menu_items_declaration(management_system)
    customers_declaration(management_system)
    return management_system
