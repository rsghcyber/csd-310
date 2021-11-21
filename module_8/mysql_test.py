"""     

    Title: mysql_test
    Author: Robin Sebbag
    Date: 11/21/2021
    Description: Test program for joining player and team tables.

"""
# Import statements
import mysql.connector
from mysql.connector import errorcode 

# Database config object
config = {
    "user": "pysports_user",
    "password": "T1sPaS$w0rdsucks",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

""" Error handling for potential MySQL errors """
try:
    # Connect to database
    db = mysql.connector.connect(**config)

    # Connection status output
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:

    """ On error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

# Close connection
finally:
    db.close()
