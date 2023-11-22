import random
import mysql.connector
import connect


def get_data()->list:
    with open('booklist.txt','r', encoding='utf-8') as f:
        data = f.read().splitlines()
        return data


def parse_data():
    bookList = get_data()
    booksql = []
    bookid = 1
    for book in bookList:
        oneBook = book.split("\t")
        bookName = oneBook[0]
        try:
            if len(oneBook[3]) > 100:
                oneBook[3] = "NULL"
            bookAuthor = oneBook[3]
        except:
            bookAuthor = "NULL"
        score = oneBook[1]
        # sql = f'INSERT INTO books VALUES ({bookid}, "{bookName}",  {score}, "{bookAuthor}");'
        booksql.append((bookid, bookName, score, bookAuthor))
        bookid += 1
    return booksql



def insert_book():
    data = parse_data()
    cnx = connect.connect_db()
    cursor = cnx.cursor()
    sql = 'INSERT INTO books VALUES (%s, %s,  %s, %s);'
    try:
        cursor.executemany(sql, data)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)
    cursor.close()


if __name__ == '__main__':
    insert_book()


