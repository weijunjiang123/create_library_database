import json

import mysql.connector

def connect_db():
    config = json.load(open('config.json'))
    mysql_config = config['mysql']
    host = mysql_config['host']
    port = mysql_config['port']
    user = mysql_config['user']
    password = mysql_config['password']
    database = mysql_config['database']
    ssl_ca = mysql_config['ssl']

    try:
        cnx = mysql.connector.connect(user=user, password=password,
                                  host=host, port=port, database=database,
                                  ssl_ca=ssl_ca, ssl_disabled=False)
        print("Connection established")
    except mysql.connector.Error as err:
        print(err)
        return None
    return cnx