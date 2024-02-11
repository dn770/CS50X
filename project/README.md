# IRMS- Interactive Restaurant Management System
#### Video Demo:  https://youtu.be/_0hYlWnqgew
#### Description:

The "Restaurant Management System" project is a functional and efficient system designed for the management and operation of a restaurant. The system provides powerful tools for managing a wide range of restaurant operations, aimed at enhancing customer service experience, improving cost management, and enabling easy and user-friendly tracking of restaurant details.

The system enables the management of various aspects, including adding and removing dishes to menus, placing specific orders for customers, and updating prices. It also provides options for managing dishes based on their types and handling their modifications.

Furthermore, the system facilitates seamless and organized ordering of dishes, menu items, and customer details. It offers an interface for customers to create orders, select payment methods, and receive quick confirmations of order status.

The system also allows the management of orders, providing real-time visibility into the status of orders, orders in progress, and customer information. Each user can monitor order statuses and efficiently manage them.

This system focuses on enhancing the customer experience by offering convenient and user-friendly consultation and ordering processes. Through this solution, restaurant managers can effectively manage processes and resources, thereby improving the quality of service provided to their customers.

In the restaurant management project, we have utilized various objects to facilitate different operations within the restaurant. Here's a brief description of each object:

Restaurant:
This object holds the fundamental information about the restaurant, such as its name, address, phone number, and description. It represents the restaurant itself and contains essential identification details.

Menu:
Each instance of this object represents a specific type of menu in the restaurant, such as the main food menu, wine menu, kids' menu, and so on. Each menu contains a collection of individual menu items that customers can order.

MenuItem:
This object represents individual dishes or products listed on the menu. Each menu item has attributes like name, description, and price.

Table:
The table object represents a table within the restaurant, with a certain seating capacity. Tables can be assigned to different orders and then released after customers finish their meals.

Customer:
The customer object represents various patrons who visit the restaurant. It contains information such as the customer's name and phone number.

Order:
This object represents an order placed by a customer for a specific table. An order may consist of various menu items from the menu, along with the total price and additional information.

Bill:
The bill object represents the bills generated for customers, including details such as the total amount, payment method, and payment status.

Reservation:
An object that represents table reservations made in advance. It includes details like the reservation time and the number of people in the party.

Shipping:
This object represents deliveries made to customers. It contains information about the delivery address and the associated order.

ManagementSystem:
The central object that oversees the operations within the system. It handles tasks like adding and removing objects, creating orders, calculating prices, and more.

Each of these objects contributes to managing the various actions within the restaurant and its management system, providing insight into how information and actions are organized and stored within the restaurant system.