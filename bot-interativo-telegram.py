import telebot
from telebot import logging
import pandas as pd
import json
import requests
from dotenv import load_dotenv
load_dotenv()


CHAVE_API = str(os.getenv('CHAVE-API'))
text2 = """
Encontre tudo que você precisa e aproveite nossa promoção relâmpago de 70% em Moveis! 
Clique em opcao para ter  mais detalhes e comprar!:

        /opcao1 : Produtos que Facilitam a Vida.

        /opcao2 : Saúde, Beleza e Bem-Estar.

        /opcao3 : Produtos Eletronicos.

        /Outras opções

Responder qualquer outra opção não vai Funcionar, Clique em uma das Opções...
"""

bot = telebot.TeleBot(CHAVE_API)

variavel = 'https://api.telegram.org/bot7398829816:AAFTRjs4Sird4neidLEMNewGqAoCm7zuu-w'

#----------------------------------------------------------#
@bot.message_handler(commands=["opcao6"])
def opcao6(mensagem):
    texto = """
    Ventilado. R$ 200,48 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op6 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao7"])
def opcao7(mensagem):
    texto = """
    fogão.  R$ 300,29 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op7 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao8"])
def opcao8(mensagem):
    texto = """
    Geladeira.  R$ 2000,15 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op8 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao9"])
def opcao9(mensagem):
    texto = """
    Creatina 150g. R$ 20,25 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op9 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao10"])
def opcao10(mensagem):
    texto = """
    Creatina 75g.  R$ 30,25 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op10 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao11"])
def opcao11(mensagem):
    texto = """
    Creatina 1kg.  R$ 200,25 compra aprovada!
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op11 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao12"])
def opcao12(mensagem):
    texto = """
    Ps5.       R$ 2460,95 compra aprovada!.
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op12 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao13"])
def opcao13(mensagem):
    texto = """
    TV 75pl.   R$ 3680,45 compra aprovada!.
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op13 salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao14"])
def opcao14(mensagem):
    texto = """
    Pc Gamer.  R$ 7940,41 compra aprovada!.
    Obrigado por interagim... com o bot!.
    """
    print('mensagem op14 salva!.')
    bot.send_message(mensagem.chat.id , texto)

#----------------------------------------------------------#

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Produtos que Facilitam a Vida
    Clique em opcao para ter  mais detalhes e comprar!:
    /opcao6 : ventlado. R$ 200,48
    /opcao7 : fogão.  R$ 300,29 
    /opcao8 : Geladeira.  R$ 2000,15 
    """
    print('mensagem salva!.')
    bot.send_message(mensagem.chat.id , texto)
    
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Saúde, Beleza e Bem-Estar!
    Clique em opcao para ter  mais detalhes e comprar!:
    /opcao9 : Creatina 150g. R$ 20,25
    /opcao10 : Creatina 75g.  R$ 30,25 
    /opcao11 : Creatina 1kg.  R$ 200,25 
    """
    print('mensagem salva!.')
    bot.send_message(mensagem.chat.id , texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    
    texto = """
    Produtos Eletronicos!
    Clique em opcao para ter  mais detalhes e comprar!:
    /opcao12 : Ps5.       R$ 2460,95
    /opcao13 : TV 75pl.   R$ 3680,45 
    /opcao14 : Pc Gamer.  R$ 7940,41 
    
    """
    print('mensagem salva!.')
    bot.send_message(mensagem.chat.id , texto)
#-----------------------------------------------------------#

def  verificar(message):
    chat_id = message.chat.id
    text = message.text

    if text.lower() == 'menu':
        bot.send_message(chat_id, f'Olá Seja Bem-vindo à Compre BEM! {text2}' )
    else:
        bot.send_message(chat_id,f"Digite 'menu' para ter as Opções!" )

@bot.message_handler(func=verificar)
def responder(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, "This is another message handler!")





bot.polling()