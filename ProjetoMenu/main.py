import tkinter as tk
from tkinter import PhotoImage
import random


janela = tk.Tk()
imagem = tk.PhotoImage(file="logo.png") # imagem para Logo
janela.iconbitmap('icone.ico') # imagem de link
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

janela.geometry("400x260")
janela.title("Gerador de numeros")

def mega_sena():
    lista = []
    while len(lista) < 6:
        x = random.randint(1,60)
        if x not in lista:
            lista.append(x)
    tema["text"] = lista


logotipo = tk.Label(janela, image=imagem)
logotipo.grid(row=2, column=1, sticky="NSEW")

tema = tk.Label(text="Sorteio da Mega-Sena", fg="#1C1C1C", bg="#aef5c3")
tema.grid(row=0, column=0, columnspan=2, sticky="NSEW")
tema.configure(font=("Cooper Black", 20, "bold" ))



mensagem = tk.Label()
mensagem.grid(row=3, column=1, columnspan=2, sticky="NSEW")

botao = tk.Button(janela, text="Gerar numeros para Mega-Sena",  command=mega_sena, width=80, height=2)
botao.grid(row=3, column=1, columnspan=2)

janela.mainloop()

