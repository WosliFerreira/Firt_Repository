from tkinter import *
from tkinter import messagebox


janela_inicial = Tk()
janela_inicial.title('Inventario Clientes')
janela_inicial.geometry('400x500')
janela_inicial.iconphoto(False, PhotoImage(file='Imagens/logo.png'))
janela_inicial.resizable(width=False, height=False)

img_fundo = PhotoImage(file='Imagens/Inventário Clientes.png')
img_botao = PhotoImage(file='Imagens/LOGIN.png')


# Variaveis Globais ------------------
def login():
    usuario = 'a'
    senha = '1'
    if l_user.get() == usuario and l_pwd.get() == senha:
        janela_inicial.destroy()
        janela2()

    else:
        messagebox.showinfo('Error', 'Usuario ou senha incorreta!')

# Segunda janela
def janela2():
    janela_iventario = Tk()
    janela_iventario.title('Inventario')
    janela_iventario.geometry('1200x500')
    janela_iventario.iconphoto(False, PhotoImage(file='Imagens/logo.png'))
    janela_iventario.config(bg='skyblue')
    janela_iventario.resizable(width=False, height=False)

    # Frames -------------------------------------------------------------
    frame_cima = Frame(janela_iventario, width=310, height=50, bg='orange', relief='flat')
    frame_cima.grid(row=0, column=0)

    frame_baixo = Frame(janela_iventario, width=310, height=450, bg='white', relief='flat')
    frame_baixo.grid(row=1, column=0, padx=0, pady=0)

    frame_direita = Frame(janela_iventario, width=788, height=403, bg='white', relief='flat')
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)
    # Labels cima ---------------------------------------------------------
    nome = Label(janela_iventario, text='Maquinas', anchor=NW, font='Arial  16 bold', bg='orange', fg='black', relief='flat')
    nome.place(x=10, y=20)
    # Labels baixo ---------------------------------------------------------
    nome = Label(janela_iventario, text='Maquinas', anchor=NW, font='Arial  16 bold', bg='orange', fg='black',
                 relief='flat')
    nome.place(x=10, y=20)

    janela_iventario.mainloop()

# Label fundo
bg = Label(janela_inicial, image=img_fundo)
bg.pack()
# Label Login -----------------------
l_user = Entry(janela_inicial, width=20, font='Arial 18', justify=CENTER)
l_user.place(x=70, y=233)
l_pwd = Entry(janela_inicial, show='*', width=20, font='Arial 18', justify=CENTER)
l_pwd.place(x=70, y=303)
# Botão
botao = Button(janela_inicial, command=login, image=img_botao, relief=RAISED)
botao.place(x=90, y=380)

janela_inicial.mainloop()
