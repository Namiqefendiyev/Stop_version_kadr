import pymysql


def delete_from_kadrlar_bazasi(int_id_x):
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="google1966",
                                 database='kadrlarbazasi', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    my_cursor = connection.cursor()
    delete_query = "DELETE FROM `kadr_tbl` WHERE id=%s"
    val = (int_id_x)
    my_cursor.execute(delete_query, val)
    connection.close()
