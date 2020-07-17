## Python Database Connections
- create a python file that contains parameters which enable us to connect to the database

```python
server = 'databases.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
  
```
#### PYODBC module

Pyodbc is a python library which helps connect to a database
-  in order to establish a connection between SQL python we need to import the pyodbc module and establish the parameters in the connection string
- 
```python
import pyodbc
  
```
## ODBC
- open database ___ which is for opening microsoft applications
cursor is a control structure that allows us to control and manage rows data from a response. in the pyodbc instance it is used to manage our

## OOP with pyodbc
- Single responsibility - so having one task per file
- Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.

- it is also good practice to make the connection to the database via OOP 
- in the below code example, I created a class and method.
- the class lets us access the open_database() which establishes a connection and returns a cursor

```python
class ConnectingToDataBase:
    
    def open_database(self):

        print("connecting to SQl server with ODBC driver")
        server = 'databases.spartaglobal.academy'
        database = 'Northwind'
        username = 'SA'
        password = 'Passw0rd2018'
        connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        connection_key = pyodbc.connect(connection_string, autocommit=True)
        print("connected {}".format(database))
        return connection_key
  
```

- as a second iteration, I created a second method that enables me to read product data and return the table in a data frame 

```python
    def read_product_data(self):

        print("reading data")
        connection_string = obj.open_database()
        cursor = connection_string.cursor()
    # create a variable - query variable - use triple quotes
        cursor.execute("select productid, productname, supplierid, unitprice from products")
        rows = cursor.fetchall()
        # for row in rows:
        product_id = []
        product_name = []
        supplierid = []
        price = []
        for row in rows:
            product_id.append(row.productid)
            product_name.append(row.productname)
            supplierid.append(row.supplierid)
            price.append(row.unitprice)

        df = pd.DataFrame()

        df["product_id"] = product_id
        df["product_name"] = product_name
        df["supplierid"] = supplierid
        df["price"] = price

        print(df.head(len(product_id)))
  
```




---
# Project notes
My project has been through a couple of iterations but has a lot of room for improvement
Currently, it is comprised of three files
- My Databasecnxn file imports pyodbc and creates a class to establish a connection with the database 
- I can improve on this by storing the sensitive information in a secret file in my gitignore to prevent the details from being shared publicly 
Next I have a file called queries
- I used instantiation to link the methods in my Open connection class with the method in my queries class
- I hard coded the SQL command, but in the future, I will try to implement user inputs to drive the SQL queries
Finally i have a 'main' or run file
- I used the pillar of abstraction here to hide some of the details from plain sight. I like the simplicity of this file and I will continue using this framework for future iterations of my project