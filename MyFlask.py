from flask import Flask, render_template, request
from k_delete import delete_from_kadrlar_bazasi
from k_insert import open_insert_to_kadrlar_bazasi

app = Flask(__name__)
app.config["debug"] = True


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')   # ЗАПУСТИМ ИНДЕКС html


# ----------------------------------------------------------------------   для отдела кадров
@app.route('/k_insert', methods=["POST", "GET"])
def kadr():
    if request.method == 'POST':
        id1 = request.form["id"]
        int_id = int(id1)
        first_name = request.form["first_name"]
        sur_name = request.form["sur_name"]
        father_name = request.form["father_name"]
        photo = request.form["photo"]
        if int_id > 0:
            open_insert_to_kadrlar_bazasi(int_id, first_name, sur_name, father_name, photo)
    return render_template('k_insert.html')   # ЗАПУСТИМ k_insert.html

# --------------------------Insert Data to Table <users(ID and Name)> in DB


@app.route('/k_delete', methods=["POST", "GET"])
def kadr_search():

    if request.method == 'POST':
        id1 = request.form["id"]
        int_id = int(id1)
        if int_id > 0:
            delete_from_kadrlar_bazasi(int_id)
            print(int_id)
    return render_template('k_delete.html')   # ЗАПУСТИМ k_insert.html
# --------------------------Insert Data to Table <users(ID and Name)> in DB


if __name__ == "__main__":
    app.run()
   #app.run(host='192.168.1.37')
