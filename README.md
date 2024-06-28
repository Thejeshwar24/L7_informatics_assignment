Overview
This Python script implements a simple ice cream parlor system using SQLite for data storage. It provides functionalities for both administrators and users to manage and add flavors, ingredients, orders, and allergens.

Feature:

Admin Features
1. Add seasonal ice cream flavors 
2. Manage ingredients, specifying and specifying whether they are allergens or not
3. View allergens list 
4. View current list of flavors and ingredients
5. Clear entries upon exiting

User Features
1. View ice cream suggestions
2. Search for a particular flavor and check for its availability
3. Place order specifying the cone size ,scoops, flavor and quantity
4. View current items in cart 
5. View allergens information 

Database Structure 

The SQLite Database 'Ice_cream_parlor' includes the following table:
    1.Ice_Cream_Seasonal_flavors - stores seasonal flavors.
    2.Ice_Cream_Ingredients - stores ingredients with allergen information.
    3.Cart - stores user order.


Getting Started

Prerequisites:
1. Python 3x
2. SQLite 3
3. VS Code

Installations:

1. Install Python and SQLite in your system 
2. Download the SQLite extension by "alexcvzz" or SQLite Viewer (to view the database)
3. clone the repository or download and run the script ('Ice_Parlor_app.py')
4. Install PrettyTable package to view the database (pip install prettytable) 

Usage:

Admin:- Choose admin role to add/manage flavors, ingredients and allergen. Follow on-screen prompts to add or view data.(Start from the admin and then move on to the user side.)
User:- Select user role to view suggestion, search flavors, place order, and view cart contents. Follow on-screen prompts to interact with the system.

Notes

Ensure all inputs are valid and follow the specified formats.
The script handles basic CRUD operation for managing the database.
Error handling is included for the database operations and user inputs

Reference 
1.https://www.geeksforgeeks.org/
2.https://www.javatpoint.com/
3.https://www.w3schools.com/sql/sql_quickref.asp
4.https://dev.mysql.com/doc/
5.https://www.w3schools.com/python/python_reference.asp
6.https://docs.python.org/3/


