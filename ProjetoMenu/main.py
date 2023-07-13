import tkinter as tk
import random

janela = tk.Tk()
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

janela.geometry("300x200")


def mega_sena():
    lista = []
    while len(lista) < 6:
        x = random.randint(1,60)
        if x not in lista:
            lista.append(x)
    tema["text"] = lista


tema = tk.Label(text="Sorteio da Mega-sena", fg="green", bg="white")
tema.grid(row=0, column=0, columnspan=2, sticky="NSEW")
tema.configure(font=("Cooper Black", 22, "italic" ))



mensagem = tk.Label()
mensagem.grid(row=3, column=1, columnspan=2, sticky="NSEW")

botao = tk.Button(janela, text="Gerar um numero da Mega-Sena", command=mega_sena)
botao.grid(row=2, columnspan=2)



janela.mainloop()

