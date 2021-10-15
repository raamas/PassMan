#Arregla el array ´JsonObject´ e introducelo en ´data´
#y completa ´delete´
from objects import Password
from secret import secret_key
from time import sleep
import datetime
import sqlite3
import json
import re

con = sqlite3.connect('main.db')
cur = con.cursor()
rows = cur.execute('SELECT * FROM passwords').fetchall()

f = open('./main.json',)
data = json.load(f)
f.close() 
pswds = data["passwords"]

def jsonify(id, site, email, password):

    input_data = {
        "id":id,
        "site":site,
        "email":email,
        "pswd":password
    }

    pswds.append(input_data)
    jsonObject = json.dumps(data)

    print(jsonObject)

    return jsonObject

def insert(Pitem):
    cur.execute("INSERT INTO passwords (id, site, email, password) VALUES (?,?,?,?);", (Pitem.id, Pitem.site, Pitem.email, Pitem.pswd))
    con.commit()
    jsonObject = jsonify(Pitem.id, Pitem.site, Pitem.email, Pitem.pswd)
    print(" | 200: DONE \n New Passwords List \n ")   
    with open("main.json","w+")as f:
        f.write(str(jsonObject))
        f.close()
        show()

def create_password():
    id = len(pswds)
    site = input("  enter wesbsite's url: ")
    email = input("  enter account's email: ")
    pswd = input("  enter your password: ")
    new_password = Password(id, site, email, pswd)
    insert(new_password)

def show():

    search = input("What are you looking for?\n")
    for row in rows:
        if search == row[1]:
            print(search," password is ",row[3])

def delete_apend():
    for pswd in pswds:
        print(pswd["id"],'sexo',pswd["site"])
    Pitem = int(input("wich site's passwords do you want to delete? write the number \n:"))
    delete(Pitem)
    


def delete(Pitem):
    #cur.execute("DELETE FROM passwords WHERE id = ?",(Pitem))
    jsonObject =  list()
    for pswd in pswds:
        if pswd["id"] != Pitem:
            jsonObject.append(pswd)
            print(jsonObject,"\n")
    data["passwords"] = jsonObject
    data_ = json.dumps(data)
    print(" | 200: DONE \n New Passwords List \n ")   
    with open("main.json","w+")as f:
        f.write(str(data_))
        f.close()
        print(jsonObject)
        show()

def main():
    print("------------------------------WELCOME------------------------------")
    print("""1. add new password\n2. search passwords\n3. Delete""")

    res = int(input(": "))

    if res == 1:
        create_password()
    elif res == 2:
        show()
    elif res == 3:
        delete_apend()

master_key = input("Plataforma de aprendizaje mas cool?\n:")
hora = datetime.datetime.now().time()

if master_key == secret_key:
    main()
else:
    with open("logs/logs.txt", "a") as f:
        hora = str(hora)
        stats = "failed_try: " + master_key + "_" + hora + '\n'
        f.write(stats)
    print("Quitate, bobo!")
sleep(2000)
