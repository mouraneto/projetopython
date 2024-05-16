# vc cria a interface gráfica aqui
from tkinter import*
def pacote():
    print('5')
    
cor1='#242323'
janela= Tk()
janela.title("Pacotao")
janela.geometry('1280x720')
janela.config(bg=cor1)
label = Label (janela, width=200, text = 'Bem vindo ao pacotao')
label.grid(row=0, column=0, padx=10, pady=10)

botao = Button(janela, command=pacote,width=20, height=5, text='adicionar item')
botao.grid (row=0, column=1, padx=10, pady=10)

janela.mainloop()

 