from tkinter import *


janela = Tk()
janela.title('Entry')
janela.geometry('390x350')
janela.config(bg='black')

# função obter resultados
def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_re['text'] = nome
    label_idade_re['text'] = idade
    label_pais_re['text'] = pais

    entry_nome.delete(0,END)
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)


# Nome ------------------------------------
label_nome = Label(janela,width=10, height=2, text='Nome:',font=('Arial 10 bold'), fg='white', bg='black', anchor=W)
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)
entry_nome = Entry(janela, width=11, font=('Arial 15'))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

# Idade ------------------------------------
label_idade = Label(janela,width=10, height=2, text='Idade:',font=('Arial 10 bold'),fg='white', bg='black', anchor=W)
label_idade.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)
entry_idade = Entry(janela, width=11, font=('Arial 15'))
entry_idade.grid(row=1, column=1, padx=10, pady=5)

# País ------------------------------------
label_pais = Label(janela,width=10, height=2, text='País:',font=('Arial 10 bold'),fg='white', bg='black', anchor=W)
label_pais.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)
entry_pais = Entry(janela, width=11, font=('Arial 15'),)
entry_pais.grid(row=2, column=1, padx=10, pady=5)


# Respostas ------------------------------------
label_nome_re = Label(janela,width=20, height=2, text='',font=('Arial 10 bold'),fg='white', bg='black', anchor=W)
label_nome_re.grid(row=0, column=2, padx=10, pady=5, sticky=NSEW)

label_idade_re = Label(janela,width=10, height=2, text='',font=('Arial 10 bold'),fg='white', bg='black', anchor=W)
label_idade_re.grid(row=1, column=2, padx=10, pady=5, sticky=NSEW)

label_pais_re = Label(janela,width=10, height=2, text='',font=('Arial 10 bold'),fg='white', bg='black', anchor=W)
label_pais_re.grid(row=2, column=2, padx=10, pady=5, sticky=NSEW)

# Botão ----------------------------
botao = Button(janela,command=obter, width=10, height=1, text='Obter Dados', bg='white', font=('Arial 15 bold'), fg='black',relief='raised')
botao.grid(row=3, column=0, padx=5, pady=20)



janela.mainloop()