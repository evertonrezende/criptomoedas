from tkinter import *
import tkinter.messagebox
import json
import requests
from sem_tempo_grafico import TempGraf

header= {'Content-Type':'application/json; charset=utf-8'}
api_coinmkt= 'https://api.coinmarketcap.com/v1/ticker/'

def dezmais(): # cria uma lista com as dez primeiras moedas do CoinMarketCap
    resp_coin= requests.get(api_coinmkt, headers=header)
    a = json.dumps(resp_coin.json())
    b = json.loads(a) #decoode json format
    dm= []
    con= 0

    for cont in range(0, 10):
    
        dm.append(b[con]['symbol'])
        con = con+1
    print(f'{dm}')



def bt_rsi():
    chap_charts= 250 # periodo padrão que o RSI será calculado
    
    if not moeda.get() and not t_grafico.get():
        
        #lb2["text"]= "Campos vazios"
        tkinter.messagebox.showinfo('Erro', 'Campos vazios!!') # exibe a mensagem de erro 
        lb2['text'] = ' ' # limpa o label 
    if not t_grafico.get():
        pass
    
    if not t_grafico.get():
        tkinter.messagebox.showinfo('Erro', 'Tempo grafico nao informado!!')
        
    if moeda.get().isnumeric(): #valida se foi digitado numero no campo da moeda
        tkinter.messagebox.showinfo('Erro', 'Valores informados inválidos!!') # exibe a mensagem de erro 
        lb2['text'] = ' ' # limpa o label     
    else:
         mo= moeda.get().upper()   # Converte o valor digitado para caixa alta
         if mo == 'BTC': # se o usuário digitar somente btc ele irá calcular com o USDT
            mo= 'BTCUSDT'
         else :
            mo=  mo+'BTC'
            
         tg= t_grafico.get() # pega a string digitada do campo "Tempo gráfico" 
         btc_var = 'https://api.binance.com/api/v1/klines?symbol='+ mo +'&interval='+ tg + '&limit=250'
         resp_btc= requests.get(btc_var, headers=header)
         a = json.dumps(resp_btc.json())
         b = json.loads(a) #decoode json format
         #ab=1 # abertura do candle coletado da API da Binance
    
         list_gain= [] #lista dos candles de subida
         list_loss= [] # lista dos candles de descida
         periodos= 14 # são 12 periodos pois o primeiro é igual a zero, começa a contar do zero 
         ganho_medio= []
         perda_media= []
         rs= []
         rsi= []
         crt=1 # candle após o primeiro
         crt_ant= 0 # primeiro candle na posição 0
         fe=4 # fechamento do candle coletado da API da Binance
         fechamento= []
         crt_fe= 0
    
            #
            #adiciona o primeiro candle sendo um candle de valor igual a zero pois nao conhecemos se é de alta ou baixa
            #
         list_loss.append(0)
         list_gain.append(0) 
    
           ############################################################################## 
           #### Criar uma lista com todos os 250 fechamentos ############################
           ##############################################################################
         for cont in range(0, chap_charts):
             fechamento.append(float(b[crt_fe][fe]))
             crt_fe= crt_fe + 1
    
           #######################################################################
           ######## Faz o primeiro tratamento dos 14 primeiros períodos ##########
           #######################################################################
         for cont in range(0, periodos): 
             if float(b[crt_ant][fe]) < float(b[crt][fe]):  #verifica se o candle é alta ou de queda 
                 gain= float(b[crt][fe]) - float(b[crt_ant][fe])
                 list_gain.append(gain)
                 list_loss.append(0) # adicona 0 na lista de loss pois o gain já foi adicionado.
    
             else:
                    loss= float(b[crt_ant][fe]) - float(b[crt][fe])
                    list_loss.append(loss) #adiciona na lista pelo preço de fechamento
                    list_gain.append(0)
    
             crt= crt+1   
             crt_ant= crt_ant+1
    
    
         p_perda_media= sum(list_loss) /14
         perda_media.append(float(p_perda_media)) #adiciona a primeira perda média na lista
    
         p_alta_media= sum(list_gain) /14 
         ganho_medio.append(float(p_alta_media)) #adiciona o primeiro ganho médio na lista
    
    
            ######################################################################
            ######################## Lista de Perda e Ganho ######################
            ######################################################################
         chap_charts= chap_charts-periodos
    
         for cont in range (0, 235):   
    
             if float(b[crt_ant][fe]) < float(b[crt][fe]):  #verifica se o candle é alta ou de queda 
                 list_loss.append(0)
                 gain= float(b[crt][fe]) - float(b[crt_ant][fe])
                 list_gain.append(gain)
    
    
             else:
                 list_gain.append(0)
                 loss= float(b[crt_ant][fe]) - float(b[crt][fe]) #adiciona na lista pelo preço de fechamento
                 list_loss.append(loss) #adiciona na lista pelo preço de fechamento
    
             crt= crt+1 
             crt_ant= crt_ant+1
    
            ####################################################################
            # reseta os contadores para começar a criar a lista de perda e ganho médio
            ####################################################################
         crt_ant= 14
         crt=15
    
            ##########################################################################
            ## Cria a lista de Ganho médio e perda média
            ##########################################################################
         for cont in range (0, 235):
             pm= float(( (perda_media[-1] * 13) + list_loss[crt]) /14) 
             perda_media.append(float(pm))
    
             gm= float( ((ganho_medio[-1] * 13) + list_gain[crt]) /14) 
             ganho_medio.append(float(gm))
             crt= crt+1 
             crt_ant= crt_ant+1
    
    
         calculo_rs= float(ganho_medio[-1]/perda_media[-1]) #calculo força relativa
         rs.append(float(calculo_rs)) #adiciona rs na lista
         calculo_rsi= 100 - (100/(1+rs[-1])) #calculo rsi
         rsi.append(float(calculo_rsi)) #adiciona rsi na lista
    
    
    ############################################################################################
    
    
         lb2["text"]= rsi
    

#Cria a nossa tela , instancia da janela principal
tela= Tk()

# Dá um título a nossa janela
tela.title('Indicadores')

texto_titulo= Label(tela, text="Indicadores", bg="black", fg= "red")
texto_titulo.pack(side=TOP, fill=X)

#Da um tamanho a tela
tela.geometry("600x400+200+200")

#Altera a cor de fundo
#tela["bg"] = "black"

# Da um icone ao aplicativo

#cria um Label
lb_moeda= Label(tela, text="Digite a moeda:")
lb_moeda.place(x=100, y=100)

moeda= Entry(tela)
moeda.place(x=200, y=100)

lb_temp= Label(tela, text="Tempo gráfico:")
lb_temp.place(x=100, y=150)

t_grafico= Entry(tela)
t_grafico.place(x=200, y=150)

bt= Button(tela, width=10, text = "RSI", command= bt_rsi)
bt.place(x=100, y=200)

lb2= Label(tela, fg= "red")
lb2.place(x=100, y=230)
#distanca da margem do vídeo é o x e a distancia do topo do vídeo


#Inicia o programa
tela.mainloop() #