from tkinter import *

janela = Tk()
janela.title('Ola mundo!')
janela.geometry('500x550')
janela.config(bg='white')
# janela.iconphoto(False, PhotoImage(file='local onde a imagem esta') )
janela.resizable(width=False, height=False)

global contador 
contador = 0

def executar():
    texto_1 = 'Numero Impar: '
    texto_2 = 'Numero Par: '
    global contador

    if contador % 2 == 0:
        resultado = texto_2 + str(contador)
        label_botao['text'] = resultado
        label_botao['fg'] = 'blue'

    else:
        resultado = texto_1 + str(contador)
        label_botao['text'] = resultado
        label_botao['fg'] = 'red'
    contador += 1

#Labels
label = Label(janela,width=5, height=2, text='Nome: ',font=('Arial 15 bold'),fg='#3446eb',bg='gray')
#label.grid(row=0, column=0, pady=5)
label.place(x=10, y=10)
#label.pack(side=LEFT)
nome = Label(janela,width=11, height=2, text='Wosli Ferreira',font=('Arial 15 bold'),fg='#3446eb',bg='gray')
nome.place(x=100, y=10)
#nome.pack(side=LEFT)

label2 = Label(janela,width=5, height=2, text='Idade: ',font=('Arial 15 bold'), fg='red',bg='gray')
#label2.grid(row=1, column=0,pady=5)
label2.place(x=10, y=70)
#label2.pack(side=LEFT)
idade = Label(janela,width=11, height=2, text='21',font=('Arial 15 bold'),fg='red',bg='gray')
idade.place(x=100, y=70)
#idade.pack(side=LEFT)


label3 = Label(janela,width=5, height=2, text='Pais: ',font=('Arial 15 bold'),fg='green',bg='gray')
#label3.grid(row=2, column=0,pady=5)
label3.place(x=10, y=130)
#label3.pack(side=LEFT)
pais = Label(janela,width=11, height=2, text='Brasil',font=('Arial 15 bold'),fg='Green',bg='gray')
pais.place(x=100, y=130)
#pais.pack(side=LEFT)

botao = Button(janela, command=executar, width=10, height=1, text='Clique Aqui', bg='gray', font=('Arial 15 bold'), fg='pink',relief='raised')
botao.place(x=10, y=190)

label_botao =  Label(janela,width=18, height=2, text='texto aqui ',font=('Arial 15 bold'),fg='black',bg='gray')
label_botao.place(x=150, y=190)

janela.mainloop()