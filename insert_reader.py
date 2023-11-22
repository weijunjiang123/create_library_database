import mysql.connector
import random
import connect

def get_ramdom_name()->str:
    first_name = ["江", "黄", "刘", "陈", "蒋", "李", "王", "张", "吴", "周", "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "罗", "郑", "梁", "谢", "宋", "唐", "许", "邓", "冯", "韩", "曹", "曾", "彭", "萧", "蔡", "潘", "田", "董", "袁", "于", "余", "叶", "蒋", "杜", "苏", "魏", "程", "吕", "丁", "沈", "任", "姚", "卢", "姜", "崔", "钟", "谭", "陆", "汪", "范", "金", "石", "廖", "贾", "夏", "韦", "傅", "方", "白", "邹", "孟", "熊", "秦", "邱", "江", "尹", "薛", "闫", "段", "雷", "侯", "龙", "史", "陶", "黎", "贺", "顾", "毛", "郝", "龚", "邵", "万", "钱", "严", "覃", "武", "戴", "莫", "孔", "向", "汤"]
    last_name = ["伟", "芳", "娜", "秀英", "敏", "静", "丽", "强", "磊", "军", "洋", "勇", "艳", "杰", "娟", "涛", "明", "超", "秀兰", "霞", "平", "刚", "俊军", "桂英"]
    first = random.choice(first_name)
    last = random.choice(last_name)
    return first + last

def get_random_age()->int:
    return random.randint(18, 30)

def get_sql_list()->list:
    data = []
    for i in range(100):
        reader_name = get_ramdom_name()
        reader_age = get_random_age()
        data.append((i, reader_name, reader_age))
    return data

def insert_reader():
    data = get_sql_list()
    cnx = connect.connect_db()
    cursor = cnx.cursor()
    sql = 'INSERT INTO reader VALUES (%s, %s, %s);'
    try:
        cursor.executemany(sql, data)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)
    cursor.close()

if __name__ == '__main__':
    insert_reader()