import getpass

username = getpass.getuser()

header = '''
                        ---------------------
                         PRODUCT APPLICATION
                        ---------------------
                          WELCOME {0}!

    There are 21 products in the database. Please select an operation:

        Operation | Description
        --------- | ----------
        'List'    | Display a list of product identifiers and names
        'Show'    | Show information about a product
        'Create'  | Add a new product
        'Update'  | Edit an existing product
        'Destroy' | Delete and existing product

'''.format(username.upper())
print(header)
