from flask import Flask, request
import sqlite3
from time import gmtime, strftime

app = Flask(__name__)
con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


@app.route('/status/update', methods=["POST"])
def add_status():
    if request.method == "POST":
        bdd_object = cur.execute("""SELECT * FROM server WHERE ip=?""", [request.remote_addr]).fetchone()
        if bdd_object:
            cur.execute(f"""INSERT INTO test(date, uptime_from) VALUES (?, ?)""", ("3", request.form["uptime_from"]))
            con.commit()
            return request.remote_addr
        else:
            return "302: Not Authorized"


@app.route('/add_server', methods=["POST"])
def add_server():
    if request.method == "POST":
        if request.form["token"] == "886f8b70484617eb26264d2b9c95574b20ccbe864571c22d1a993ef8ed492a383afde51fdaf18ba79f899581f0b730d9":
            if request.form["name"] != "" or request.form["ip"] != "" or request.form["desc"] != "":
                cur.execute('''INSERT INTO server(name, ip, desc) VALUES (?, ?, ?)''', (request.form["name"], request.form["ip"], request.form["desc"]))
                con.commit()
                return "Done!"


if __name__ == '__main__':
    app.run(debug=True)
