import os
import sqlite3
#mysql.connector.path['C:\\Users\\Пользователь\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\mysql\\connector']
import mysql.connector
#import pymysql
#import numpy

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "SymphoniaHeroica1803!",
    #auth_plugin='mysql_native_password'
    database = "hometaskdb",
    )

print(mydb)    

input()