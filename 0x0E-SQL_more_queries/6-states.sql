-- creates the database hbtn_0d_usa and the table states.
-- create database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create tabel
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
