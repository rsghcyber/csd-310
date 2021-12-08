/* 
    Title: whatabookdb_init
    Author: Robin Sebbag
    Date: 12/07/2021
    Description: Initialization script for creating the WhatABook database.
*/

-- Create whatabook database
CREATE DATABASE whatabook;

-- Create whatabook user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

USE whatabook;

-- Create user table 
CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL, 
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

-- Create book table 
CREATE TABLE Book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY(book_id)
);

-- Create store table
CREATE TABLE Store (
    store_id INT NOT NULL,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);

-- Create wishlist table
CREATE TABLE Wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES user(user_id),
    CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES book(book_id)
);

-- Insert book rows
INSERT INTO book(book_name, details, author)
    VALUES('Project Hail Mary', 'Hardcover, English, 496 pages, Ballantine Books', 'Andy Weir'),
    ('The Martian', 'paperback, English, 387 pages, Broadway Books', 'Andy Weir'),
    ('The Da Vinci Code', 'paperback, English, 597 pages, Anchor', 'Dan Brown'),
    ('Angels and Demons', 'paperback, English, 496 pages, Washington Square Press', 'Dan Brown'),
    ('The Lost Symbol', 'paperback, English, 624 pages, Knopf Doubleday Publishing Group', 'Dan Brown'),
    ('Origin', 'hardcover, English, 656 pages, Anchor', 'Dan Brown'),
    ('Wool', 'paperback, English, 592 pages, Marliner Books', 'Hugh Howey'),
    ('A Court of Thorns and Roses', 'paperback, English, 432 pages, Bloomsbury Publishing', 'Sarah J. Maas'),
    ('Throne of Glass', 'paperback, English, 432 pages, Bloomsbury USA Childrens', 'Sarah J. Maas');

-- Insert user rows
INSERT INTO user(first_name, last_name)
    VALUES('John', 'Doe'),
    ('Jennifer', 'White'),
    ('Jane', 'Smith');

-- Insert store rows
INSERT INTO store(store_id, locale)
    VALUES(1, '123 Main Street, Bellevue, Nebraska, 68005');

-- Insert wishlist rows
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 7),
    (2, 4),
    (3, 1);