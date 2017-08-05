import pymysql.cursors

connection = pymysql.connect(host='192.168.64.132',
                                     user='root',
                                     password='paSSport',
                                     db='wikiurl',
                                     charset='utf8')

try:
    with connection.cursor() as cursor:
        #查询语句, 计数
        sql = "select `urlname`, `urlhref` from `urls` where `id` is not null "
        count= cursor.execute(sql)
        print(count)

        #查询数据
        """
        result = cursor.fetchall()
        print(result)
        """
        result = cursor.fetchmany(size=3)
        print(result)
finally:
    connection.close()