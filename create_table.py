import connect
import mysql.connector

def create_table():
    cnx = connect.connect_db()
    cursor = cnx.cursor()
    sql1 = "use library;"
    books_table = "create table if not exists books(bookid int primary key, title varchar(150), score decimal(4,2) , author varchar(100));"
    reader_table = "create table if not exists reader(readerid int primary key, name varchar(10), age int);"
    borrow_table = "create table if not exists borrow(readerid int, bookid int, borrow_date date, return_date date, foreign key(readerid) references reader(readerid), foreign key(bookid) references books(bookid));"
    try:
        cursor.execute(sql1)
        cursor.execute(books_table)
        cursor.execute(reader_table)
        cursor.execute(borrow_table)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)
    cursor.close()

if __name__ == '__main__':
    create_table()