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

btn_cadastrar = Button(interface, text="Salvar", command=salvar, font=("Arial 12")).place(x=100, y=190)

interface.mainloop()