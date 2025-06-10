from table_creation import create_table
from data_insertion import insert_data

try:
    create_table('Categories',
                "CategoryID int, CategoryName string",
                )
    create_table('Cities',
                 "CityID int,CityName string,Zipcode int,CountryID int",
                )
    create_table('Countries',
                 'CountryID int,CountryName string,CountryCode string',
                )
    create_table('Customers',
                 "CustomerID int,FirstName string,MiddleInitial string,LastName string,CityID int,Address string",
                )
    create_table('Employees',
                 "EmployeeID int,FirstName string,MiddleInitial string,LastName string,BirthDate timestamp,Gender string,CityID int,HireDate timestamp",
                )
    create_table('Products',
                 "ProductID int, ProductName string, Price int, CategoryID int, Class string, ModifyDate timestamp, Resistant string, IsAllergic string, VitalityDays int",
                )
    create_table('Sales',
                 "SalesID int,SalesPersonID int,CustomerID int,ProductID int,Quantity int,Discount float,TotalPrice float,SalesDate timestamp,TransactionNumber string",
                )

    insert_data('categories.csv',
                'Categories'
                )
    insert_data('cities.csv',
                'Cities'
                )
    insert_data('countries.csv',
                'Countries'
                )
    insert_data('customers.csv',
                'Customers'
                )
    insert_data('employees.csv',
                'Employees'
                )
    insert_data('products.csv',
                'Products'
                )
    insert_data('sales.csv',
                'Sales'
                )

except Exception as e:
    print("Error in hive schema:",e)
