from tkinter import *

janela = Tk()
janela.title('Radio_Button')
janela.geometry('390x350')
janela.config(bg='black')


def obter():
    resultado = selecionado_1.get()
    print(resultado)

selecionado_1 = IntVar()
selecionado_2 = BooleanVar()
selecionado_3 = StringVar()


radio = Radiobutton(janela,command=obter, text='Primeiro', value=0, variable=selecionado_1)
radio.grid(row=0, column=0, pady=10, padx=10)

radio1 = Radiobutton(janela,command=obter, text='Segundo', value=1, variable=selecionado_1)
radio1.grid(row=1, column=0, pady=10, padx=10)

radio2 = Radiobutton(janela,command=obter, text='Terceiro', value=2, variable=selecionado_1)
radio2.grid(row=2, column=0, pady=10, padx=10)











janela.mainloop()