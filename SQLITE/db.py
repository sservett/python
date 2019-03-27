import sqlite3

con = sqlite3.connect("library.db")

cursor =  con.cursor()

def table_creation():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (NAME TEXT, WRITER TEXT, PUBLISHER TEXT, PAGE INT)")
    con.commit()

table01 = table_creation()


def add_book():
    cursor.execute("INSERT into books Values('ELMER', 'Ibrahim Berk INCE', 'INCE YAYINLARI', 20)")
    con.commit()

#add_book()


def query_book():
    cursor.execute("SELECT * FROM books")
    list = cursor.fetchall()
    for i in list:
        print(i)
    con.commit

#query_book()


def query_book2():
    cursor.execute("SELECT NAME,WRITER FROM books")
    list = cursor.fetchall()
    for i in list:
        print(i)
    con.commit

query_book2()


con.close


"""
def add_book_new(name,writer,publisher,page):
    cursor.execute("INSERT INTO books VALUES(?,?,?,?)",(name,writer,publisher,page))
    con.commit()

name = input("NAME: ")
writer = input("WRITER: ")
publisher = input("PUBLISHER: ")
page = int(input("PAGE: "))

#add_book_new(name,writer,publisher,page)
"""
