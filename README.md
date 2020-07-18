## Python Database Connections
- create a python file that contains parameters which enable us to connect to the database
```python
server = '*************'
database = '************'
username = '************'
password = '*************' 
```
### PYODBC module
- Pyodbc is a python library which helps connect to a database
-  In order to establish a connection between SQL python we need to import the pyodbc module and establish the parameters in the connection string

```python
import pyodbc  
```
### ODBC
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
        server = '**********'
        database = '**********'
        username = '**********'
        password = '**********'
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
#### Homework

- in terms of the homework - the objective was to write text to a file and then read from this file to write to another file, simultaneously 

- in the code below, I constructed an OOP program that takes an input from a user and the in the following methods reads the message. 

```python
class fileHandling:
    def __init__(self, text_storage=None):
        self.text_storage = text_storage

    def user_input(self):
        try:
            name = input("Enter your name: \n")
            if len(name) == 0:
                raise Exception
        except Exception:
            print("please enter a valid name(at least one letter)")
            self.user_input()
        else:
            print("thank you, your name has been registed {}".format(name))
        
        def readtext(self):

        try:
            user_input = input("please leave a message: \n")
            if len(user_input) == 0:
                raise Exception
        except Exception:
            print("please enter a message --> at least one character")
            self.readtext
        else:
            with open("message.txt","w+") as file:
                file.write(user_input)
                file.seek(0)
                self.text_storage = file.read()
            with open("message2.txt","w") as file:
                file.write(self.text_storage)
                return self.text_storage

```
- the third method in the class allows us to retrieve a predefined image file and then read that image.

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
#### Homework

- in terms of the homework - the objective was to write text to a file and then read from this file to write to another file, simultaneously 

- in the code below, I constructed an OOP program that takes an input from a user and the in the following methods reads the message. 

```python
def readimage(seld):

        with open(mike_tyson,'rb') as image_file: # reading it as bytes rb = read_bytes
            image_string = image_file.read()
            with open("file location.png","wb") as dest_image:
                dest_image.write(image_string) # writing the top two lines into the bottom two lines 


```
https://github.com/Spartabariallali/filehandling/blob/master/mike_tyson.jpg
