from tkinter import * 
import tkinter.messagebox as MessageBox

import mysql.connector as mysql

interface = Tk()
interface.geometry("500x300")
interface.title("Exemplo de banco de dados")

lbl_codigo = Label(interface, text="Código", font=("Arial 12"))
lbl_codigo.place(x=50, y=30)
txt_codigo = Entry(interface)
txt_codigo.place(x=150, y=30)
lbl_nome = Label(interface, text="Nome:", font=("Arial 12"))
lbl_nome.place(x=50, y=80)
txt_nome = Entry(interface)
txt_nome.place(x=150, y=80)
lbl_telefone = Label(interface, text="Telefone:", font=("Arial 12"))
lbl_telefone.place(x=50, y=130)
txt_telefone = Entry(interface)
txt_telefone.place(x=150, y=130)

def salvar():
    variavel_cod = txt_codigo.get()
    variavel_nome = txt_nome.get()
    variavel_telefone = txt_telefone.get()

    if(variavel_cod == "" or variavel_nome == "" or variavel_telefone == ""):
        MessageBox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connect(host= "localhost", user="root", password="", database="exemplo")
        cursor = conectar.cursor()
        cursor.execute("INSERT INTO teste VALUES('" + variavel_cod + "', '" + variavel_nome + "', '" + variavel_telefone + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Cadastro Realizado com sucesso!")
        conectar.close()

def excluir():
    if(txt_codigo.get() == ""):
        MessageBox.showinfo("ALERT", "Digite o código para deletar")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="exemplo")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM teste WHERE cod='"+ txt_codigo.get() +"'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação Excluída com Sucesso!")
        conectar.close()

def atualizar():
    id = txt_codigo.get()
    name = txt_nome.get()
    phone = txt_telefone.get()

    if(name == "" or phone == ""):
        MessageBox.shoinfo("ALERT", "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="exemplo")
        cursor = conectar.cursor()
        cursor.execute("UPDATE teste SET nome = '"+ txt_nome.get() + "', telefone = '" + txt_telefone.get() + "' WHERE cod='"+ txt_codigo.get() + "'")
        cursor.execute("commit")

    MessageBox.showinfo("Status", "Atualização feita com sucessão!")
    conectar.close()

def Select():
    if(txt_codigo.get() == ""):
        MessageBox.showinfo("ALERT", "Por favor Digite o Código")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="exemplo")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM teste WHERE cod= '"+ txt_codigo.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            txt_nome.insert(0, row[1])
            txt_telefone.insert(0, row[2])

        conectar.close()

btn_cadastrar = Button(interface, text="Salvar", command=salvar, font=("Arial 12")).place(x=100, y=190)
btn_excluir = Button(interface, text="Apagar", command=excluir, font=("Arial 12")).place(x=200, y=190)
btn_update = Button(interface, text="Atualizar", command=atualizar, font=("Arial 12")).place(x=320, y=190)
btn_consultar= Button(interface, text="Consultar", command=Select, font=("Arial 12")).place(x=200, y=240)

interface.mainloop()