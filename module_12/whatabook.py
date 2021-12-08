"""
    Title: what_a_book.py
    Author: Robin Sebbag
    Date: 12/07/2021
    Description: Program for customers to interact with whatabook database.
"""

# Import Statements
import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Connect to database
db = mysql.connector.connect(**config)

cursor = db.cursor()

# Main Menu function
def main_menu():
    print("--Menu--" + "\n 1. View Books" + "\n 2. View Store Locations" + "\n 3. My Account" + "\n 4. Quit")
    try:
        user_selection = int(input("Select an option (1, 2, 3, or 4):"))
        return user_selection
    except ValueError:
        print("\n Invalid number.")
        sys.exit(0)


# View Books function
def view_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()
    print("\n  -- DISPLAYING BOOK LIST --")
    for book in books:
        print(" Book ID: {}\n Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2], book[3]))

# View Store Locations function
def view_locations(cursor):
    cursor.execute("SELECT store_id, locale FROM store")
    location = cursor.fetchall()
    print("\n --DISPLAYING ALL LOCATIONS--")
    for store in location:
        print(" Store ID: {}\n Locale: {}\n".format(store[0], store[1]))

# Select Customer ID function
def validate_user():
    try:
        user_id = int(input("Enter customer ID(1, 2, or 3):"))
        if user_id < 0 or user_id > 3:
            print("Invalid customer ID. Quitting program.")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n Value is not valid. Quitting program.")
        sys.exit(0)


# View Customer Account function
def show_account():
    try:
        print("\n --My Account--")
        print("1. Wishlist\n 2. Add Book\n 3. Back to Main")
        user_selection = int(input("Select an option (1, 2, or 3):"))
        return user_selection
    except ValueError:
        print("\n Invalid number. Quitting program.")
        sys.exit(0)

# Display all items in wishlist function
def show_wishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    wishlist = cursor.fetchall()
    print("\n --DISPLAYING ALL WISHLIST ITEMS--")
    for items in wishlist:
        print("\n Book Title: {}\n Author: {}\n".format(items[4], items[5]))


# Display books not in wishlist function
def not_in_list(cursor, user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))
    print(query)
    cursor.execute(query)
    books_to_add = cursor.fetchall()
    print("\n --DISPLAYING AVAILABLE BOOKS--")
    for book in books_to_add:
        print(" Book ID: {}\n Book Name: {}\n".format(book[0], book[1]))


# Function for adding a book to wishlist
def add_book(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

# Error handling and main menu details
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = main_menu()

    while user_selection != 4:
        if user_selection == 1:
            view_books(cursor)

        if user_selection == 2:
            view_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:
                    
                    not_in_list(cursor, my_user_id) 
                    book_id = int(input("\n Enter book ID of book to add:"))
                    add_book(cursor, my_user_id, book_id)
                    db.commit()
                    print("\n Book id: {} was added to your wishlist.".format(book_id))

                if account_option < 0 or account_option> 3:
                    print("\n Invalid option. Please try again...")
                account_option = show_account()

        if user_selection < 0 or user_selection > 4:
            print("\n Invalid option. Please try again...")

        user_selection = main_menu()
        
    print("\n\n  Program terminated...")
    
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()