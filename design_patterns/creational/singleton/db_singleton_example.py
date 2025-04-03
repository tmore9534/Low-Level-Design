import sqlite3  

class DatabaseConnection:  
    _instance = None  

    def __new__(cls, db_name):  
        if cls._instance is None:  
            cls._instance = super().__new__(cls)  
            cls._instance.connection = sqlite3.connect(db_name)  
        return cls._instance  

# Usage  
db1 = DatabaseConnection("my_database.db")  
db2 = DatabaseConnection("my_database.db")  

print(db1 is db2)  # Output: True (Same instance)  
print(db1.connection == db2.connection)  # Output: True (Same DB connection)  