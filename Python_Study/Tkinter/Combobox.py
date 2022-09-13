from tkinter.ttk import *
from tkinter import *

janela = Tk()
janela.title('Combobox')
janela.geometry('390x350')
janela.config(bg='black')


def obter():
    resultado = combo.get()
    print(resultado)


# Nome ------------------
label_nome = Label(janela,width=15, height=1, text='faça uma escolha', font=('Arial 12'), anchor=W)
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

combo = Combobox(janela,)
combo['values'] = (1, 2, 3, 4)
combo.current(0)
combo.grid(row=1, column=0,padx=5, pady=5, sticky=NSEW)




butao = Button(janela,command=obter, width=10, height=1, text='Ver respostas', relief='raised', bg='white')
butao.grid(row=2, column=0, pady=20, padx=5)

janela.mainloop()