def ongoing_loop(management_system):
    while True:
        option = input(" insert 1 - to add reservation\n\
          2- to add shipping\n,3 - to take order\n \
          4 - to bill\n 5- to update menus\n 6 - to update menuItems\n 7- to update customers\n \
          8 - to update tables\n 9- to show data \n   0 - to exit\n")

        if not option: # 0 -> exit
            return

        elif option == "1" or option == "2": # create reservation
            if option == "1":
                reserv = management_system.create_reservation(input("Time: "), int(input("num of people: ")))
                ans = input("to change time? y/n\n")
                if ans == "y":
                    reserv.change_reservation_time(input("new time: "))
                ans = input("to change number of people? y/n\n")
                if ans == "y":
                    reserv.change_number_of_people(input("new number: "))

                table = management_system.match_table(reserv)
            elif option =="2":
                ships = management_system.create_shipping(input("Address: "))
                table = 0

            #create order according the reservation or shipping details
            ans = input("New customer or old customer ? n/o")
            if ans == "n":
                customer = management_system.add_customer(input("name: "), input("contact_number: "))
                customer.check_in()
            else: # find the customer and check in
                for custom in management_system.customers:
                    if custom.contact_number == input("contact_number: "):
                        custom.check_in()
                        customer = custom
                        break

            #create the order and it's details
            order = management_system.create_order(table, customer, input("payment_type: "))
            ans = "y" # flag
            while ans == "y":
                print("What would you like to order?")
                management_system.update_order(order, input("menu_id:"), input("menu_item_id: "))
                ans = input("anything else? y/n\n")
            print("Thank you.")

            ans = input("do you want to remove item from the ordr? y/n\n") # flag
            while ans == "y":
                print("What would you like to remove from the order?")
                order.remove_menu_item(input("menu_item_id: "))
                ans = input("anything else? y/n\n")
            print("Thank you.")

            #update address of shipping
            if option == "2":
                ans = input("Are you want to change the address? y/n\n")
                if ans == 'y':
                    ships.change_address(input("new address: "))

        elif option == "3": # take order
            order = management_system.take_order() # find the first order in the list that satus is false
            print(order.calculate_price())

        elif option == "4": # bill
            # change payment_type
            order_id = input("order_id: ")
            order_to_bill = None
            for order in management_system.orders:
                if order.order_id == order_id:
                    order_to_bill = order
                    break

            print(order_to_bill)
            ans = input("Are you want to change the payment type? y/n\n")
            if ans == 'y':
                order_to_bill.bill.change_type(input("new type: "))

            if not order_to_bill.bill.payment_status:
                order_to_bill.bill.pay()
                management_system.remove_order(order_to_bill.order_id)

                for tab in management_system.tables:
                    if tab.table_id == order_to_bill.table_id:
                        tab.free()
                        break

                for custom in management_system.customers:
                    if custom.customer_id == order_to_bill.customer_id:
                        custom.check_out()
                        break

        elif option == "5": # update menus
                sub_option = input(" insert 1 - to add new menu\n 2 - to remove menu\n 3 - to clear menu\n")
                if sub_option == "1":
                    management_system.add_menu(input("type: "))
                elif sub_option == "2":
                    management_system.remove_menu(input("menu_id = "))
                elif sub_option == "3":
                    management_system.clear_menu(input("menu_id = "))
                else:
                    print("invalid option, back to main-menu")

        elif option == "6": # update menuItems
            sub_option = input(" insert 1 - to add new menuItem\n 2 - to remove menuItem\n 3 - to update price of menuItem\n")
            menu_id = input("menu_id: ")
            for menu in management_system.menus:
                if menu.menu_id == menu_id:
                    if sub_option == "1":
                        menu.add_menu_item(input("title: "), input("description: "), float(input("price:")) )
                    elif sub_option == "2":
                        menu.remove_menu_item(input("item_id = "))
                    elif sub_option == "3":
                        item_id = input("item_id: ")
                        for item in menu:
                            if item.item_id == item_id:
                                menu.remove_menu_item(input("item_id = "))
                                break
                    else:
                        print("invalid option, back to main-menu")

        elif option == "7": # update customers
            sub_option = input(" insert 1 - to add new customer \n 2 - to remove customer\n 3- update contact_number\n")
            if sub_option == "1":
                management_system.add_customer(input("name: "), input("contact_number: "))
            elif sub_option == "2":
                management_system.remove_customer(input("customer_id = "))
            elif sub_option == "3":
                old_number = input("old contact_number: ")
                for cust in management_system.customers:
                    if cust.contact_number == old_number:
                        cust.change_number(input("new contact_number"))

            else:
                print("invalid option, back to main-menu")

        elif option == "8": # update tables
            sub_option = input(" insert 1 - to add new table\n 2 - to remove table\n")
            if sub_option == "1":
                capacity = input("capacity: ")
                management_system.add_table(capacity)
            elif sub_option == "2":
                table_id = input("table_id = ")
                management_system.remove_table(table_id)
            else:
                print("invalid option, back to main-menu")

        elif option == "9":
            sub_option = input(" insert 1 - to show orders\n 2 - menus\n 3 - customers\n 4- tables\n")
            if sub_option == "1":
                for order in management_system.orders:
                    print(order)
            elif sub_option == "2":
                for menu in management_system.menus:
                    print (menu)
            elif sub_option == "3":
                for custom in management_system.customers:
                    print(custom)
            elif sub_option == "4":
                for tab in management_system.tables:
                    print(tab)
            else:
                print("invalid option, back to main-menu")

