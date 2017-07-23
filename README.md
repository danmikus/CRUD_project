# Mikus Systems Inc. Presents: The Inventory Management Application

The Inventory Management Application allows you to quickly and easily
manage your entire store inventory. The application allows you to:

* **_List_** All products in Inventory
* **_Show_** details of a particular products
* **_Create_** entries for new products
* **_Update_** existing product entries
* **_Destroy_** records of products no longer in Inventory

Once a command is selected, the app reads a csv file with the products and
takes the appropriate action, displaying or writing the data in the csv
appropriately. To ensure data quality data validation is enforced in this
application.

## Installation

Download the source code:

```shell
git clone https://github.com/danmikus/CRUD_project.git
cd ~/Documents/CRUD_project
```

Finally, download the [example `products.csv` file](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) and save it as `data/products.csv`.

## Usage

Run the command below to run the program.

```shell
python app/products_app.py
```
