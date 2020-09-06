import sqlite3


def connect():
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if not exists Books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, ISBN INTEGER, Year Intege)")
    conn.commit()
    conn.close()
    print("I did it!")


def add_entry(title, author, isbn, year):
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("INSERT into Books VALUES(null, ?, ?, ?, ?)", (title, author, isbn, year))
    conn.commit()
    conn.close()


def view_all():
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Books")
    results=cur.fetchall()
    conn.close()
    return results


def search_func(title="", author="", isbn="", year=""):
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Books where title=? OR author=? OR isbn =? OR year = ?",(title, author, isbn, year))
    results=cur.fetchall()
    conn.close()
    return results


def delete_entry(id):
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("DELETE from Books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_entry(id, title, author, isbn, year):
    conn=sqlite3.connect("repository.db")
    cur=conn.cursor()
    cur.execute("UPDATE Books SET title=?, author =?, isbn=?, year=? where id=?", (title, author, isbn, year, id))
    conn.commit()
    conn.close()

connect()


#print(view_all())