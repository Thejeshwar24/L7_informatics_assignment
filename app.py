# import requirements
import sqlite3
from prettytable  import PrettyTable
# creating the database
def ice_cream_parlor_db():
    try:
            # connection
        conn = sqlite3.connect("Ice_cream_parlor.db")
        c= conn.cursor()
        # creating the required tables
        # Ice_Cream_Flavors table
        c.execute(
            '''
                Create Table IF NOT EXISTS Ice_Cream_Seasonal_flavors(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                season_name TEXT NOT NULL,
                flavor_name_1 TEXT NOT NULL,
                flavor_name_2 TEXT NOT NULL,
                flavor_name_3 TEXT NOT NULL
                )
            '''
        )
        # Ice_Cream_Ingredients table
        c.execute(
            '''
                Create Table IF NOT EXISTS Ice_Cream_Ingredients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_name TEXT,
                is_allergen TEXT
                )   
            '''
        )
        # Your_cart
        c.execute(
            '''
                Create Table IF NOT EXISTS Cart(
                order_id INTEGER PRIMARY KEY,
                user_name TEXT,
                ice_cone TEXT,
                ice_scoop INTEGER,
                flavor TEXT,
                order_quantity INTEGER
                )   
            '''
        )
        # commiting the db
        conn.commit()
        print("Database created successfully")
    except sqlite3.Error as e:
        print(f"Error in initializing the database: {e}")
    finally:
        conn.close()

ice_cream_parlor_db()

# Functions that are used to insert,delete,view the tables   
"""
function to insert flavors into the table
"""
def add_Ice_Cream_Flavors(season_name,flavor_name_1,flavor_name_2,flavor_name_3):
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO Ice_Cream_Seasonal_flavors (season_name,flavor_name_1,flavor_name_2,flavor_name_3) VALUES (?,?,?,?)', (season_name,flavor_name_1,flavor_name_2,flavor_name_3))
    conn.commit()
    conn.close()
"""
function to check if the flavor exits when the user/customer orders
"""
def check_flavor_exits(flavor):
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Ice_Cream_Seasonal_flavors WHERE flavor_name_1 = ? OR flavor_name_2 = ? OR flavor_name_3 = ?',(flavor,flavor,flavor))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    
"""
function to view the list of flavors
"""
def view_flavors():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Ice_Cream_Seasonal_flavors')
    rows = c.fetchall()

    table=PrettyTable()
    table.field_names = ["Id","Season","flavor_1","flavor_2","flavor_3"]
    for row in rows:
        table.add_row(row)
    
    print(table)
    conn.close()
"""
function to insert ingredients into the table
"""
def add_Ice_Cream_Ingredients(ingredient_name,allergens):
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO Ice_Cream_Ingredients (ingredient_name,is_allergen) VALUES (?,?)', (ingredient_name,allergens))
    conn.commit()
    conn.close()

"""
function to view the list of ingredients
"""
def view_ingredient():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Ice_Cream_Ingredients')
    rows = c.fetchall()
    table=PrettyTable()
    table.field_names = ["Id","ingredient","allergens"]
    for row in rows:
        table.add_row(row)
    print("Ice Cream Ingredients")
    print(table)
    conn.close()
"""
function add the list of allergens 
"""
def add_Ice_Cream_allergens(allergens_name):
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO Ice_Cream_Ingredients (ingredient_name,is_allergen) VALUES (?,"yes")', (allergens_name,))
    conn.commit()
    conn.close()

    print(f"Allergen '{allergens_name}' added.")
"""
function to view the list of allergens
"""
def view_allergens():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Ice_Cream_Ingredients WHERE is_allergen = 1 OR is_allergen = "yes"')
    rows = c.fetchall()
    conn.close()

    if rows:
        table=PrettyTable()
        table.field_names = ["Id","Allergen_Name","Allergens"]
        for row in rows:
            table.add_row(row)
        print("Allergens List: ")
        print(table)
    else:
        print("No allergen ingredients found.")
    

    
"""
function to insert the user/customer order into the cart
"""
def add_to_cart(user_name,ice_cone,ice_scoop,flavor,order_quantity):
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO Cart (user_name,ice_cone,ice_scoop,flavor,order_quantity) VALUES (?,?,?,?,?)', (user_name,ice_cone,ice_scoop,flavor,order_quantity))
    conn.commit()
    conn.close()
"""
function to view the customer suggestion posted by the admin
"""
def view_suggestions():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
            
    c.execute('SELECT * FROM Ice_Cream_Seasonal_flavors')
    rows = c.fetchall()
    table=PrettyTable()
    table.field_names = ["Sl.No","Season_name","Flavor1","Flavor2","Flavor3"]
    for row in rows:
        table.add_row(row)
    print("\n",table)
    conn.close()
"""
function to view the cart once the user/customer has ordered there ice cream
"""
def view_cart():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Cart')
    table=PrettyTable()
    rows = c.fetchall()
    if rows:
        table.field_names = ["Id","Name","Cone Size","Scoop","Flavor","Order quantity"]
        for row in rows:
            table.add_row(row)
        print("Cart Items: ")
        print(table)
    else:
        print("Cart is empty")
    conn.close()
"""
function to clear the cart of the user once he exits the application
"""
def del_cart():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('Delete FROM Cart')
    conn.commit()
    conn.close()
"""
function to clear all the entries made by the admin once he exits the application
"""
def admin_clear():
    conn = sqlite3.connect('Ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('Delete FROM Ice_Cream_Seasonal_flavors')
    c.execute('Delete FROM Ice_Cream_Ingredients')
    conn.commit()
    conn.close()



def main():
    
    print("\n")
    print("\n\t\tWelcome To Our Ice Cream Parlor App.")
    while True:
        print("\nFeel free to select the following options.")
        print("1.Admin")
        print("2.User")
        print("3.Exit")
        # if admin is selected he/she may be able to the flavors, ingredient and allergen list.
        # is user is selected he/she may be able to view the menu and place the order and view the order
        choice = input("Select Your role: ")
        if choice == '1':
            print("\nWelcome Admin")
            while True:
                    print("\nSelect your options")
                    print("1.Add Flavor")
                    print("2.Add Ingredients")
                    print("3.Add Allergen")
                    print("4.View Flavors")
                    print("5.View Ingredients")
                    print("6.View Allergen")
                    print("7.Exit")

                    admin_option = input("Enter your option: ")
                    if admin_option =="1":
                        while True:
                            try:
                                season_name = input("Enter the season: ")
                                flavor_name_1 = input("Enter flavor name 1: ")
                                flavor_name_2 = input("Enter flavor name 2: ")
                                flavor_name_3 = input("Enter flavor name 3: ")

                                if season_name=="" or flavor_name_1=="" or flavor_name_2=="" or flavor_name_3=="":
                                    print("Enter all fields")
                                    continue
                                # add function
                                add_Ice_Cream_Flavors(season_name,flavor_name_1,flavor_name_2,flavor_name_3)
                                print("Flavor added.\n")
                                break
                            except Exception as e:
                                print(e)
                        
                    elif admin_option =="2":
                        while True:
                            try:
                                ingredient_name = input("Enter ingredient name: ")
                                if ingredient_name=="":
                                    print("Enter valid inputs")
                                    continue
                                allergens = input("Enter yes/true or no/false if the ingredient is an allergen. ")
                                if allergens.lower()=="true" or allergens.lower()=="yes":
                                    add_Ice_Cream_Ingredients(ingredient_name,allergens)
                                    print("\n Ingredient added")
                                elif allergens.lower()=="false" or allergens.lower()=="no":
                                    add_Ice_Cream_Ingredients(ingredient_name,allergens)
                                    print("\n Ingredient added")
                                else:
                                    print("Invalid input")
                                print("Ingredient added.\n")
                                break
                            except Exception as e:
                                print(e)
                    elif admin_option == "3":
                        allergens_name=input("Enter allergens name:\n")
                        add_Ice_Cream_allergens(allergens_name)
                        print("Added")
                    elif admin_option =="4":
                        view_flavors()
                    elif admin_option =="5":
                        view_ingredient()
                    elif admin_option =="6":
                        view_allergens()
                    elif admin_option =="7":
                        print("\nExisting admin panel")
                        break
                    else:
                        print("Invalid")

            
        elif choice=="2":
            print("\nWelcome User")
            while True:
                print("\nSelect your options")
                print("1.View Suggestions")
                print("2.Search flavors")
                print("3.Order")
                print("4.view cart")
                print("5.view allergens")
                print("6.Exit")

                user_option = input("Enter your option: ")
                # user is able to view the list of ice cream flavors/ingredients available. 
                if user_option == "1":
                        print("Suggestion from US.\n")
                        view_suggestions()
                elif user_option =="2":
                    print("Want to search for flavors:\n")
                    search_flv=input("What do you have in mind?")
                    if check_flavor_exits(search_flv):
                        print(f"{search_flv} is available.\n")
                    else:
                        print(f"{search_flv} is currently unavailable.\n")
                        print("Have a look of the flavors that we have.")
                        view_flavors()
                elif user_option =="3":
                    # user is able to order there ice cream
                    while True:
                        user_name = input("Enter your name: ")
                        if not user_name:
                            print("Enter a valid name: ")
                    
                        cone = input("Enter the cone size (small/medium/large): ")
                        if cone not in ["small","medium","large"]:
                            print("invalid inputs. please select from small,medium,large")
                            continue
                    
                        while True:
                            try:
                                scoop = int(input("Enter the number of scoops: "))
                                if scoop<=0:
                                    print("Enter a number of scoops.")
                                    continue
                                break
                            except ValueError:
                                print("Enter a number")

                        while True:

                            flavor = input("Enter the flavor: ")
                            # check if the flavor is available if not display the list of available flavors
                            if check_flavor_exits(flavor):
                                print(f"{flavor} is available. ")
                            else:
                                print(f"{flavor} is currently unavailable.")
                                print("Enter a flavor from the list")
                                view_flavors()
                                continue
                            break
                                
                    
                        while True:
                                try:
                                    order_quantity =int(input("Enter the quantity."))
                                    if order_quantity <= 0:
                                        print("Enter a number.")
                                        continue
                                    break
                                except ValueError:
                                    print("Invalid")
                                    
                            # order is added to cart
                        add_to_cart(user_name,cone,scoop,flavor,order_quantity)
                        break

                    

                elif user_option=="4":
                    # user is able to view the cart
                    view_cart()
                elif user_option=="5":
                    # user is able to view the allergens
                    view_allergens()
                elif user_option=="6":
                    del_cart()
                    print("Existing the user panel")
                    break
                else:
                    print("invalid")


        elif choice == "3":
            print("\nExiting the ice cream app")
            break
        else:
            print("invalid option")

if __name__ == '__main__':
    main()




