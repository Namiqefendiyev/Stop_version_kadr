from flask import Flask, render_template, request
import pymysql


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Open DB and Insert values in DB
def open_insert_to_kadrlar_bazasi(int_id_x, first_name_x, sur_name_x, father_name_x, photo_x):
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="google1966",
                                 database='kadrlarbazasi', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    my_cursor = connection.cursor()
    insert_query = "INSERT INTO kadr_tbl (ID,FIRST_NAME,SUR_NAME,FATHER_NAME,PHOTO) VALUES (%s,%s,%s,%s,%s);"
    val = (int_id_x, first_name_x, sur_name_x, father_name_x, photo_x)
    my_cursor.execute(insert_query, val)
    print("INSERTED ANY DATA TO TABLE kadr_tbl")
    connection.close()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Open DB and Insert values in DB


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Open DB and Delete values in DB
def delete_from_kadrlar_bazasi(int_id_x):
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="google1966",
                                 database='kadrlarbazasi', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    my_cursor = connection.cursor()
    delete_query = "DELETE FROM `kadr_tbl` WHERE id=%s"
    val = (int_id_x)
    my_cursor.execute(delete_query, val)
    print("deleted ANY DATA FROM TABLE kadr_tbl")
    connection.close()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Open DB and Insert values in DB


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Заходит на главную страницу
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')   # ЗАПУСТИМ ИНДЕКС html


# ----------------------------------------------------------------------   для отдела кадров
@app.route('/k_insert', methods=["POST", "GET"])
def kadr():

    if request.method == 'POST':
        id = request.form["id"]
        int_id = int(id)
        first_name = request.form["first_name"]
        sur_name = request.form["sur_name"]
        father_name = request.form["father_name"]
        photo = request.form["photo"]
        if int_id > 0:
            open_insert_to_kadrlar_bazasi(int_id, first_name, sur_name, father_name, photo)
    return render_template('k_insert.html')   # ЗАПУСТИМ k_insert.html
# --------------------------Insert Data to Table <users(ID and Name)> in DB


@app.route('/k_search', methods=["POST", "GET"])
def kadr_search():

    if request.method == 'POST':
        id = request.form["id"]
        int_id = int(id)
        if int_id > 0:
            delete_from_kadrlar_bazasi(int_id)
            print(int_id)
    return render_template('k_search.html')   # ЗАПУСТИМ k_insert.html
# --------------------------Insert Data to Table <users(ID and Name)> in DB





if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host='192.168.1.37', debug=True)
    app.run(host='0.0.0.0')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Заходит на главную страницу