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
        # fetchone()获取结果的下一行
        # fetchmany(size)获取结果的下size行
        # fetchall() 获取结果中剩下的所有行
        result = cursor.fetchall()
        print(result)
        """
        result = cursor.fetchmany(size=3)
        print(result)
finally:
    connection.close()