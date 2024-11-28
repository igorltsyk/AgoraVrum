import customtkinter as ctk
import os
from PIL import Image  # pip install pillow

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Janela Principal')
        self.geometry('700x400')
        
        # configuração de grid 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # pegando imagens 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'imgs')
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, 'agora_vrum_logo1.png')), size=(100, 55))
        self.home_image = ctk.CTkImage(Image.open(os.path.join(image_path, 'home_icon.png')), size=(20, 20))
        
        # frame de botões de navegação
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0, fg_color='#000000')
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_rowconfigure(7, weight=1)
        
        # label do frame de navegação com imagem
        fonte = ctk.CTkFont(family='Montserrat', size=22)

        self.nav_frame_label = ctk.CTkLabel(
            self.navigation_frame,
            text='AgoraVrum',
            image=self.logo_image,
            compound='left',
            font=fonte)
        
        self.nav_frame_label.grid(row=0, column=0, padx=20, pady=20)

 ####################################################################################################
        
        # botão home                                                                                 
        self.home_button = ctk.CTkButton(   
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Home',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            image=self.home_image,
            anchor='w',
            command=self.show_home
        )
        self.home_button.grid(row=1, column=0, sticky='ew')

        
        # botão de pesquisa de placa 
        self.pesquisaplaca_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Placa',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            anchor='w',
            command=self.show_placa
        )
        self.pesquisaplaca_button.grid(row=2, column=0, sticky='ew')

        # botão de pesquisa por marca 
        self.pesquisamarca_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Marca',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            anchor='w',
            command=self.show_marca
        )
        self.pesquisamarca_button.grid(row=3, column=0, sticky='ew')

        # botão de pesquisa por ano 
        self.pesquisaano_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Ano',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            anchor='w',
            command=self.show_ano
        )
        self.pesquisaano_button.grid(row=4, column=0, sticky='ew')
 
        # botão valor diária 
        self.pesquisadiaria_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Valor Diária',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            anchor='w',
            command=self.show_valor_diaria
        )
        self.pesquisadiaria_button.grid(row=5, column=0, sticky='ew')

         # botão adicionar meu veiculo
        self.config_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text='Adicionar Meu Veículo',
            fg_color='transparent',
            text_color=('gray15', 'gray30'),
            hover_color=('white', 'white'),
            anchor='w',
            command=self.show_add_meu_veiculo
        )
        self.config_button.grid(row=6, column=0, sticky='ew')
        

#######################################################################################################



        # area principal onde o conteúdo será exibido           
        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color='#942121')
        self.content_frame.grid(row=0, column=1, sticky='nsew')
        
        # exibir conteúdo inicial
        self.show_home()
        
        # função para exibir o conteúdo da tela home
    def show_home(self):
        # limpa a área de conteúdo antes de adicionar novos widgets
        for widget in self.content_frame.winfo_children():
            widget.destroy()
   
   
   
    def buscar_no_arquivo(self, campo, valor):
   
    # Definir o caminho do arquivo
        caminho_arquivo = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dados.txt')

    # Mapear índices dos campos
        indice_campo = {'marca': 0, 'ano': 1, 'placa': 2, 'valordiaria': 3}

        # Verificar se o campo informado é válido
        if campo not in indice_campo:
            print(f"Campo inválido: {campo}")
            return []

        # Obter o índice correspondente ao campo
        indice = indice_campo[campo]
        resultados = []

        try:
            with open(caminho_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    # dividir a linha em dados
                    dados = linha.strip().split(',')

                    # garantir que a linha contém os dados necessários
                    if len(dados) != 4:
                        print(f"Linha ignorada por formato inválido: {linha}")
                        continue

                    # buscar o campo com base no índice
                    valor_dado = dados[indice].strip()  

                    #ccomparar valore
                    if campo == 'valordiaria':
                        try:
                            # converter para float se for valordiaria
                            valor_dado = float(valor_dado)
                            valor = float(valor)
                        except ValueError:
                            print(f"Erro ao converter valor da diária: {valor_dado}")
                            continue

                    if str(valor_dado).upper() == str(valor).upper():
                        resultados.append(dados)

            return resultados

        except FileNotFoundError:
            print("Arquivo não encontrado")
            return []

        except Exception as e:
            print(f"Erro inesperado: {e}")
            return []

        home_label = ctk.CTkLabel(self.content_frame, text="Home")
        home_label.pack(pady=10)
        
        # caixa de entrada de texto
        caixa_de_entrada = ctk.CTkEntry(self.content_frame, placeholder_text="Pesquisar...")
        caixa_de_entrada.pack(pady=10)
        
        # botão de envio
        botao_enviar = ctk.CTkButton(self.content_frame, text="Pesquisar", 
                                     command=self.home_button_event, 
                                     fg_color='#242424', 
                                     text_color='white',
                                      hover_color='#000000' )
        botao_enviar.pack(pady=10)

        


    def show_placa(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    

    

        # caixa de entrada da placa 
        entrada_placa = ctk.CTkEntry(self.content_frame, placeholder_text='Digite a placa')
        entrada_placa.pack(pady=10)

        botao_pesquisa_placa = ctk.CTkButton(self.content_frame, text='Pesquisar', 
                                             command=lambda: self.pesquisar_placa(entrada_placa), 
                                             fg_color='#242424',
                                             text_color='white',
                                             hover_color='#000000')
        botao_pesquisa_placa.pack(pady=10)


    def pesquisar_placa(self, placa_entry): 
        placa = placa_entry.get()
        if placa: 
                dados_veiculos = self.buscar_no_arquivo('placa', placa)

                if dados_veiculos: 
                    for widget in self.content_frame.winfo_children():
                        widget.destroy()


                    for dados_veiculo in dados_veiculos:
                        marca, ano, placa, valor_diaria = dados_veiculo

               # criando um frame para cada carro
                    veiculo_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color='#242424')
                    veiculo_frame.pack(padx=10, pady=10, fill="x")  
                    self.after(40000, veiculo_frame.destroy)

                        #  informações do veículo dentro do frame
                    ctk.CTkLabel(veiculo_frame, text=f"Placa: {placa}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Marca: {marca}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Ano: {ano}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Valor Diária: {valor_diaria}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkButton(veiculo_frame, 
                                    text='Ver Mais', 
                                    fg_color='#242424', 
                                    corner_radius=0, 
                                    command=lambda: self.ver_detalhes({'placa': placa, 'marca': marca, 'ano': ano, 'valor_diaria': valor_diaria})).pack(side='right', padx=5)
    
                else:
                    # placa não seja encontrada
                    resultado = f'Placa {placa} não encontrada'
                    resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
                    resultado_label.pack(padx=10)
                    self.after(20000, resultado_label.destroy)  # O aviso desaparece depois de 20 segundos
        else: 
            # caso o camp esteja vazio
            resultado = 'Por favor, digite uma placa'
            resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
            resultado_label.pack(padx=10)
            self.after(20000, resultado_label.destroy)  # O aviso desaparece depois de 20 segundos
    



    def show_marca(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # caixa de entrada marca 
        entrada_marca = ctk.CTkEntry(self.content_frame, placeholder_text='Digite a marca')
        entrada_marca.pack(pady=10)

        botao_pesquisa_marca= ctk.CTkButton(self.content_frame, text='Pesquisar', 
                                             command=lambda: self.pesquisar_marca(entrada_marca), 
                                             fg_color='#242424',
                                             text_color='white', 
                                             hover_color='#000000')
        botao_pesquisa_marca.pack(pady=10)
    
    
    def pesquisar_marca(self, marca_entry):
        marca = marca_entry.get()
        if marca:
            # busca no arquivo pela marca
            dados_veiculos = self.buscar_no_arquivo('marca', marca)
            
            if dados_veiculos:
              
                for widget in self.content_frame.winfo_children():
                    widget.destroy()

                for dados_veiculo in dados_veiculos:
                    marca, ano, placa, valor_diaria = dados_veiculo

                    veiculo_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color='#242424')
                    veiculo_frame.pack(padx=10, pady=10, fill="x")  
                    self.after(40000, veiculo_frame.destroy)

                    ctk.CTkLabel(veiculo_frame, text=f"Placa: {placa}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Marca: {marca}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Ano: {ano}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Valor Diária: {valor_diaria}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkButton(veiculo_frame, 
                                text='Ver Mais', 
                                fg_color='#242424', 
                                corner_radius=0, 
                                command=lambda: self.ver_detalhes({'placa': placa, 'marca': marca, 'ano': ano, 'valor_diaria': valor_diaria})).pack(side='right', padx=5)
            else:
                resultado = f'Marca {marca} não encontrada'
                resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
                resultado_label.pack(padx=10)
                self.after(20000, resultado_label.destroy)  
        else: 
            resultado = 'Por favor, digite uma marca'
            resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
            resultado_label.pack(padx=10)
            self.after(20000, resultado_label.destroy)  

    def ver_detalhes(self, veiculo):
        # criando nova janela para exibir detalhes do veiculo 
        detalhes_janela = ctk.CTkToplevel(self)
        detalhes_janela.geometry('400x300')
        detalhes_janela.title('Detalhes do Veículo')

        placa_label = ctk.CTkLabel(detalhes_janela, text=f"Placa: {veiculo['placa']}")
        placa_label.pack(pady=5)
        marca_label = ctk.CTkLabel(detalhes_janela, text=f"Marca: {veiculo['marca']}")
        marca_label.pack(pady=5)
        ano_label = ctk.CTkLabel(detalhes_janela, text=f"Ano: {veiculo['ano']}")
        ano_label.pack(pady=5)
        
        # converter valor diaria para float antes de formatá-lo
        try:
            valor_diaria = float(veiculo['valor_diaria'])
        except ValueError:
            valor_diaria = 0.0  # caso não consiga converter, define como 0.0 

        diaria_label = ctk.CTkLabel(detalhes_janela, text=f"Diária: R$ {valor_diaria:,.2f}")
        diaria_label.pack(pady=5)

        detalhes_janela.transient(self)  
        detalhes_janela.grab_set()      # faz a janela ficar na frente 

        # garantir que a janela de detalhes não seja fechada até que o usuário interaja com ela
        detalhes_janela.wait_window(detalhes_janela)



    def show_ano(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

                    # caixa de entrada ano
        entrada_ano = ctk.CTkEntry(self.content_frame, placeholder_text='Digite o ano')
        entrada_ano.pack(pady=10)

        botao_pesquisa_ano = ctk.CTkButton(self.content_frame, text='Pesquisar',
                                           command=lambda: self.pesquisar_ano(entrada_ano),
                                           fg_color='#242424', 
                                            text_color='white',
                                            hover_color='#000000')
        botao_pesquisa_ano.pack(pady=10)

    def pesquisar_ano(self, ano_entry): 
        ano = ano_entry.get()
        if ano: 
            dados_veiculos = self.buscar_no_arquivo('ano', ano) # retorna uma lista com todos os anos 
              
            
            if dados_veiculos:
                    # limpa a área de conteúdo antes de adicionar novos widgets
                for widget in self.content_frame.winfo_children():
                    widget.destroy()

                   # cria um frame para cada veiculo
                for dados_veiculo in dados_veiculos:
                    marca, ano, placa, valor_diaria = dados_veiculo

                    # criando um frame para cada veiculo
                    veiculo_frame = ctk.CTkFrame(self.content_frame,
                                                 corner_radius=0,
                                                 fg_color='#242424', 
                                                )    
                    veiculo_frame.pack(padx=10, pady=10, fill='x')
                    self.after(40000, veiculo_frame.destroy)

                    # exibindo as informações do veiculo dentro do frame 
                    ctk.CTkLabel(veiculo_frame, text=f"Placa: {placa}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Marca: {marca}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Ano: {ano}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Valor Diária: {valor_diaria}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkButton(veiculo_frame, 
                                  text='Ver Mais', 
                                  fg_color='#242424', 
                                  corner_radius=0, 
                                  command=lambda: self.ver_detalhes({'placa': placa, 'marca': marca, 'ano': ano, 'valor_diaria': valor_diaria})).pack(side='right', padx=5)
            else:
                resultado = f'Ano {ano} não encontrado'
                resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
                resultado_label.pack(padx=10)
                self.after(20000, resultado_label.destroy)  # o aviso desaparece depois de 20 segundos
        else: 
            resultado = 'Por favor, digite um ano'
            resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
            resultado_label.pack(padx=10)
            self.after(20000, resultado_label.destroy)  # o aviso desaparece depois de 20 segundos


               

    
    def show_valor_diaria(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()   
            
            # caixa de entrada marca 
        entrada_diaria= ctk.CTkEntry(self.content_frame, placeholder_text='Digite o valor máximo desejado')
        entrada_diaria.pack(pady=10)

        botao_pesquisa_diaria = ctk.CTkButton(self.content_frame, text='Pesquisar', 
                                              command=lambda: self.pesquisar_valor_diaria(entrada_diaria),
                                              fg_color='#242424',
                                              text_color='white',
                                              hover_color='#000000')
        botao_pesquisa_diaria.pack(pady=10)


    def pesquisar_valor_diaria(self, diaria_entry):
        valor_diaria = diaria_entry.get()
        if valor_diaria: 
            dados_veiculos = self.buscar_no_arquivo('valordiaria', valor_diaria) # retorna uma lista com todos as diarias
              
            
            if dados_veiculos:
                    # limpa a área de conteúdo antes de adicionar novos widgets
                for widget in self.content_frame.winfo_children():
                    widget.destroy()
                for dados_veiculo in dados_veiculos:
               
                    if len(dados_veiculo) >= 4:
                        placa, marca, ano, valor_diaria = dados_veiculo

                   # cria um frame para cada veiculo
                for dados_veiculo in dados_veiculos:
                    marca, ano, placa, valor_diaria = dados_veiculo

                    # criando um frame para cada veiculo
                    veiculo_frame = ctk.CTkFrame(self.content_frame,
                                                 corner_radius=0,
                                                 fg_color='#242424', 
                                                )    
                    veiculo_frame.pack(padx=10, pady=10, fill='x')
                    self.after(40000, veiculo_frame.destroy)

                    # exibindo as informações do veiculo dentro do frame 
                    ctk.CTkLabel(veiculo_frame, text=f"Placa: {placa}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Marca: {marca}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Ano: {ano}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkLabel(veiculo_frame, text=f"Valor Diária: {valor_diaria}", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
                    ctk.CTkButton(veiculo_frame, 
                                  text='Ver Mais', 
                                  fg_color='#242424', 
                                  corner_radius=0, 
                                  command=lambda: self.ver_detalhes({'placa': placa, 'marca': marca, 'ano': ano, 'valor_diaria': valor_diaria})).pack(side='right', padx=5)
            else:
                resultado = f'Valor {valor_diaria} não encontrado, por favor digite um valor válido.'
                resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
                resultado_label.pack(padx=10)
                self.after(2000, resultado_label.destroy)  # o aviso desaparece depois de 2 segundos
        else: 
            resultado = 'Por favor, digite um número'
            resultado_label = ctk.CTkLabel(self.content_frame, text=resultado)
            resultado_label.pack(padx=10)
            self.after(20000, resultado_label.destroy)  # o aviso desaparece depois de 20 segundos






    def show_add_meu_veiculo(self): 
            for widget in self.content_frame.winfo_children():
                widget.destroy()

            # entradas necessarias para cadastro do automovel 
            self.entrada_modelo = ctk.CTkEntry(self.content_frame, placeholder_text= 'Digite o modelo do seu carro...', width= 250)
            self.entrada_modelo.pack(padx=10, pady=25)
            
            self.entrada_ano = ctk.CTkEntry(self.content_frame, placeholder_text='Digite o ano do seu veiculo...', width=250)
            self.entrada_ano.pack(padx=10, pady=25)

            self.entrada_placa = ctk.CTkEntry(self.content_frame, placeholder_text='Digite a placa do seu veiculo...', width=250)
            self.entrada_placa.pack(padx=10, pady=25)
            

            self.entrada_valor_diaria = ctk.CTkEntry(self.content_frame, placeholder_text='Digite o valor da diaria desejada...', width=250)
            self.entrada_valor_diaria.pack(padx=10, pady=25)

            self.botao_salvar_dados = ctk.CTkButton(self.content_frame, text='Anunciar no AgoraVrum', 
                                                    command=self.salvar_dados,
                                                    corner_radius=35,
                                                    fg_color='#242424', 
                                                    text_color='white', 
                                                    hover_color='#000000')


            self.botao_salvar_dados.pack(padx=10, pady=25)
    
    def salvar_dados(self): 
        # coletar os dados
        modelo = self.entrada_modelo.get()
        ano = self.entrada_ano.get()
        placa = self.entrada_placa.get()
        valor_diaria = self.entrada_valor_diaria.get()

        # verificar se algum campo está vazio
        if not modelo or not ano or not placa or not valor_diaria:
            mensagem = ctk.CTkLabel(
                self.content_frame, 
                text="Todos os campos devem ser preenchidos", 
                text_color="red", 
                font=("Arial", 14)
            )
            mensagem.pack(pady=10)
            return

        # padronizar 
        modelo = modelo.strip().title()
        ano = ano.strip()
        placa = placa.strip().upper()
        valor_diaria = valor_diaria.strip()

        # validar os dados
        try:
            int(ano)  # verifica se o ano é um número
            float(valor_diaria)  # verifica se o valor diário é um número
        except ValueError:
            mensagem = ctk.CTkLabel(
                self.content_frame, 
                text="Ano e valor diário devem ser numéricos.", 
                text_color="red", 
                font=("Arial", 14)
            )
            mensagem.pack(pady=10)
            return

        dados = [modelo, ano, placa, valor_diaria]

        # verificar se o arquivo existe e se a placa já foi registrada
        caminho_arquivo = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dados.txt')
        placas_existentes = set()
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    partes = linha.strip().split(',')
                    if len(partes) == 4:
                        placas_existentes.add(partes[2].strip())
        except FileNotFoundError:
            pass  # o arquivo ainda não existe

        if placa in placas_existentes:
            mensagem = ctk.CTkLabel(
                self.content_frame, 
                text="Placa já registrada! Insira uma placa única.", 
                text_color="red", 
                font=("Arial", 14)
            )
            mensagem.pack(pady=10)
            return

        # adicionar os dados ao arquivo
        with open(caminho_arquivo, 'a', encoding='utf-8') as f:
            if os.stat(caminho_arquivo).st_size == 0:  # verifica se o arquivo está vazio
                f.write('Marca,Ano,Placa,Valor Diária\n')  # adiciona o cabeçalho
            f.write(','.join(dados) + '\n')

        mensagem = ctk.CTkLabel(
            self.content_frame, 
            text="Veículo registrado com sucesso!", 
            text_color="green", 
            font=("Arial", 14)
        )
        mensagem.pack(pady=10)



    def home_button_event(self):
        ...

    


        

if __name__ == '__main__':
    app = App()
    app.mainloop()
