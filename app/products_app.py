import getpass
import csv






def initialize(products, path):

    username = getpass.getuser()
    header = '''
                            ---------------------
                             PRODUCT APPLICATION
                            ---------------------
                              WELCOME {0}!

        There are {1} products in the database. Please select an operation
                   or type 'Quit' to exit the program:'''.format(username.upper(), len(products))

    operations = '''
            Operation | Description
            --------- | ----------
            'List'    | Display a list of product identifiers and names
            'Show'    | Show information about a product
            'Create'  | Add a new product
            'Update'  | Edit an existing product
            'Destroy' | Delete and existing product
            'Quit'    | Exit the program
            '''

    print(header)
    while True:
        print(operations)
        user_input = input("Please enter your selection:\n>").upper()
        if user_input.strip() == "QUIT":
            break
        elif user_input == "LIST":
            list_products(products)
            print("\n")
        elif user_input == "SHOW":
            show_product(products)
        elif user_input == "CREATE":
            create_product(products, path)
        else:
            print("ERROR: Please enter a valid operation")


new_path = '../data/products.csv'

def list_products(products):

    print("THERE ARE {0} PRODUCTS:\n".format(len(products)))
    for row in products:
        print(row["id"], "-", row["name"], "-", row["aisle"], "-", row["department"], "-", "$" + "{0:.2f}".format(float(row["price"])))

def show_product(products):

    while True:

        selection = input("Please enter a product ID or type 'Back':\n>")
        if selection.upper() == "BACK":
            break
        try:
            selection = int(selection)
        except ValueError:
            print("ERROR: Please enter an integer")
            continue
        if selection < 1 or selection > len(products):
            print("ERROR: No product exists for this ID. Please enter a product number between 1 and {0}".format(len(products)))
            continue
        else:
            product = list(filter(lambda x: x["id"] == str(selection), products))
            print("\n" + product[0]["id"], "-", product[0]["name"], "-", product[0]["aisle"], "-", product[0]["department"], "-", "$" + "{0:.2f}".format(float(product[0]["price"])) + "\n")

def create_product(products, path):

    while True:
        with open(new_path, "r") as csv_file:
            prod_num = len(list(csv.DictReader(csv_file)))

        new_product = {}
        print("Please enter the information for the new product:")
        new_product["id"] = prod_num + 1
        new_product["name"] = input("Name:\n")
        new_product["aisle"] = input("Aisle:\n")
        new_product["department"] = input("Department:\n")
        while True:
            try:
                new_product["price"] = float(input("price:\n"))
            except ValueError:
                print("Error: Enter a valid price")
                continue
            else:
                break

        with open(path, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["id", "name", "aisle", "department", "price"])
            writer.writerow(new_product)

        print("The product below has been successfully added: ")
        print(new_product["id"], "-", new_product["name"], "-", new_product["aisle"], "-", new_product["department"], "-", "$" + "{0:.2f}".format(float(new_product["price"])) + "\n")

        while True:
            selection = input("Do you want to input another product? y/n:\n").upper()
            if selection != "Y" and selection != "N":
                print("ERROR: Invalid input")
                continue
            else:
                break

        if selection == "Y":
            continue
        else:
            break

def main():
    new_path = '../data/products.csv'

    with open(new_path, "r") as csv_file:
        reader = list(csv.DictReader(csv_file))

    initialize(reader, new_path)

if __name__ == "__main__":
    main()


#import pdb; pdb.set_trace()
