import tkinter as tk

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg="white", bg='black', width =80, height=20, font=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada", width=80, height=20)
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

dicionario_cotacoes = {
    'Dolar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}
mensagem_contacao = tk.Label(text="Cotação Não entrada")
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    if cotacao_moeda:
        pass # exibir a cotacao
    else:
        pass # exibir mensagem de cotação não encontrada






def buscar_cotacao():
    print(moeda.get())


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()