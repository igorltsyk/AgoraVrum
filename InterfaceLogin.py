import customtkinter as ctk 
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import PhotoImage


# funções dos comandos dos botões 

def com1(): 
        testee = ctk.CTkEntry(janela_p, placeholder_text="Teste", width=300)
        testee.pack(padx=10, pady=10)

        


def login():

        usuario = usuario_entrada.get()
        senha = senha_entrada.get()
        if usuario == 'igor' and senha == 'igor':
                loginconfig()
             
        else: 
                erro = ctk. CTkLabel(janela, text="Erro, usuário ou senha incorretos. Tente novamente.", fg_color="#242424", corner_radius=10)
                erro.place(x=455, y=300)
                janela.after(2000, erro.destroy) # o erro desaparece depois de 2 segundos

# função de abrir janela depois do login  

def loginconfig(): 
        janela.withdraw()
        global janela_p

        janela_p = ctk.CTkToplevel()
        janela_p.geometry("800x500")
        janela_p.title("Segunda janela")
       



        




# criação da primeira janela

janela = ctk.CTk()
janela.geometry("800x500")
janela.title("Janela Pricipal")
janela.resizable(False, False)

#frame da janela 
frame = ctk.CTkFrame(master=janela, width=400, height=1000)
frame.pack(side=ctk.LEFT)

#frames

ajuste_usuario= ctk.CTkFrame(janela, fg_color='#242424', corner_radius=10)#ajustando o pixels 
ajuste_usuario.place(relx=0.55, rely=0.26)

ajuste_senha = ctk.CTkFrame(janela, fg_color='#242424', corner_radius=10)
ajuste_senha.place(relx=0.573, rely=0.400)

ajustebtlogin = ctk.CTkFrame(janela, fg_color='#242424', corner_radius=10)
ajustebtlogin.place(relx=0.670, rely=0.500)


# criação dos campos de entrada login 
usuario_entrada = ctk.CTkEntry(ajuste_usuario, placeholder_text="Usuário", width=300) #cria o campo de entrada do usuário
usuario_entrada.pack(padx= 20, pady= 30) # .pack chama a função da biblioteca 


senha_entrada = ctk.CTkEntry(ajuste_senha, placeholder_text="Senha", show=("*"), width=300)#cria o campo de entrada de senha
senha_entrada.pack(pady=10, padx=1)

#botões na janela de criar conta e fazer login 

botao_login = ctk.CTkButton(ajustebtlogin, text="Login", command=login)
botao_login.pack(pady=10)

# segunda janela botões 



#menu 




janela.mainloop()


