import getpass
import os
import csv


#    user_input = input("Ther: ")
#    if user_input.strip() == "DONE":
#        break
#    try:
#        int_input = int(user_input)
#    except ValueError:
#        print("ERROR: Please enter an integer")
#        continue
#    if int_input < 1 or int_input > len(products):
#        print("ERROR: Please enter a product number between 1 and %s" % len(products))
#        continue
#    else:
#        shopping_list.append(int(user_input))
#return shopping_list


new_path = '../data/products.csv'

def list_products(products):

    print("THERE ARE {0} PRODUCTS:\n".format(len(products)))
    for row in products:
        print(row["id"], "-", row["name"], "-", row["aisle"], "-", row["department"], "-", "$" + "{0:.2f}".format(float(row["price"])))



def show_product(input, products):

    product = list(filter(lambda x: x["id"] == str(input), products))
    print(product[0]["id"], "-", product[0]["name"], "-", product[0]["aisle"], "-", product[0]["department"], "-", "$" + "{0:.2f}".format(float(product[0]["price"])))

def main():
    username = getpass.getuser()
    new_path = '../data/products.csv'

    with open(new_path, "r") as csv_file:
        reader = list(csv.DictReader(csv_file))

    header = '''
                            ---------------------
                             PRODUCT APPLICATION
                            ---------------------
                              WELCOME {0}!

        There are {1} products in the database. Please select an operation:

            Operation | Description
            --------- | ----------
            'List'    | Display a list of product identifiers and names
            'Show'    | Show information about a product
            'Create'  | Add a new product
            'Update'  | Edit an existing product
            'Destroy' | Delete and existing product

    '''.format(username.upper(), len(reader))

    #list_products(reader)
    show_product(2, reader)


if __name__ == "__main__":
    main()


#import pdb; pdb.set_trace()
