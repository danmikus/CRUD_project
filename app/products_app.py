import getpass
import csv
import collections

def start_reader(path):

    with open(path, "r") as csv_file:
        reader = list(csv.DictReader(csv_file))
    return reader

def initialize(path):

    products = start_reader(path)
    username = getpass.getuser()
    header = '''

    __  ____ __                 _____            __                         ____
   /  |/  (_) /____  _______   / ___/__  _______/ /____  ____ ___  _____   /  _/___  _____
  / /|_/ / / //_/ / / / ___/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/   / // __ \/ ___/
 / /  / / / ,< / /_/ (__  )   ___/ / /_/ (__  ) /_/  __/ / / / / (__  )  _/ // / / / /___
/_/  /_/_/_/|_|\__,_/____/   /____/\__, /____/\__/\___/_/ /_/ /_/____/  /___/_/ /_/\___(_)
                                  /____/


                            ---------------------
                              INVENTORY MANAGER
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
            list_products(path)
            print("\n")
        elif user_input == "SHOW":
            show_product(path)
        elif user_input == "CREATE":
            create_product(path)
        elif user_input == "UPDATE":
            update_product(path)
        elif user_input == "DESTROY":
            destroy_product(path)
        else:
            print("ERROR: Please enter a valid operation")


def list_products(path):

    products = start_reader(path)

    print("\nThere are {0} products:\n".format(len(products)))
    for row in products:
        print(row["id"], "-", row["name"], "-", row["aisle"], "-", row["department"], "-", "$" + "{0:.2f}".format(float(row["price"])))

def show_product(path):

    products = start_reader(path)

    while True:
        selection = input("\nPlease enter a product ID or type 'Back':\n>")
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
            product = list(filter(lambda x: x["id"] == str(selection), products))[0]
            product["price"] = float(product["price"])
            print("\n{id} - {name} - {aisle} - {department} - ${price:.2f}".format(**product))
            #print("\n" + product[0]["id"], "-", product[0]["name"], "-", product[0]["aisle"], "-", product[0]["department"], "-", "$" + "{0:.2f}".format(float(product[0]["price"])))

def create_product(path):

    while True:
        prod_num = len(start_reader(path))

        new_product = {}
        print("\nPlease enter the information for the new product:")
        new_product["id"] = prod_num + 1
        new_product["name"] = input("\nName:\n>")
        new_product["aisle"] = input("\nAisle:\n>")
        new_product["department"] = input("\nDepartment:\n>")
        while True:
            try:
                new_product["price"] = float(input("\nprice:\n>"))
            except ValueError:
                print("Error: Enter a valid price")
                continue
            else:
                break

        with open(path, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["id", "name", "aisle", "department", "price"])
            writer.writerow(new_product)

        print("\nThe product below has been successfully added: ")
        print("{id} - {name} - {aisle} - {department} - ${price:.2f}\n".format(**new_product))

        while True:
            selection = input("Do you want to input another product? y/n:\n>").upper()
            if selection != "Y" and selection != "N":
                print("ERROR: Invalid input")
                continue
            else:
                break
        if selection == "Y":
            continue
        else:
            break

def update_product(path):

    while True:
        products = start_reader(path)
        updated_product = collections.OrderedDict()
        selection = input("\nPlease enter the ID of the product you want to update, or type 'Back':\n>")
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
            product = (list(filter(lambda x: x["id"] == str(selection), products)))[0]
            ind = products.index(product)

            updated_product["id"] = product["id"]
            updated_product["name"] = input("Input the product name to replace '{0}':\n>".format(product["name"]))
            updated_product["aisle"] = input("Input the aisle to replace '{0}':\n>".format(product["aisle"]))
            updated_product["department"] = input("Input the department to replace '{0}':\n>".format(product["department"]))
            while True:
                try:
                    updated_product["price"] = float(input("Input the price to replace '{0}':\n>".format(product["price"])))
                except ValueError:
                    print("Error: Enter a valid price")
                    continue
                else:
                    break

            products.pop(ind)
            products.insert(ind, updated_product)

            with open(path, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames = ["id", "name", "aisle", "department", "price"])
                writer.writeheader()
                writer.writerows(products)

            print("\nThe product below has been successfully updated:")
            print("{id} - {name} - {aisle} - {department} - ${price:.2f}".format(**updated_product)) #TODO change to truncate


def destroy_product(path):

    while True:
        products = start_reader(path)
        selection = input("\nPlease enter the ID of the product you want to delete, or type 'Back':\n>")
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
            product = (list(filter(lambda x: x["id"] == str(selection), products)))[0]
            product["price"] = float(product["price"])

            while True:
                confirmation = input("Are you sure you want to delete {0}? y/n:\n>".format(product["name"])).upper()
                if confirmation != "Y" and confirmation != "N":
                    print("ERROR: Invalid input")
                    continue
                else:
                    break
            if confirmation == "Y":
                ind = products.index(product)
                products.pop(ind)
                new_id = range(1, (len(products) + 1))

                for index, prod in enumerate(products):
                    prod["id"] = new_id[index]

                with open(path, "w") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames = ["id", "name", "aisle", "department", "price"])
                    writer.writeheader()
                    writer.writerows(products)

                print("\nThe product below has been successfully deleted:")
                print("{id} - {name} - {aisle} - {department} - ${price:.2f}".format(**product))
            else:
                continue


def main():

    prod_path = '../data/products.csv'
    initialize(prod_path)

if __name__ == "__main__":
    main()


#import pdb; pdb.set_trace()
