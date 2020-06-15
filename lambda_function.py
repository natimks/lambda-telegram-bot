import json
import requests
from src.score import calcular

TELE_TOKEN = 'TOKEN'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)


def enviar_mensagem(texto_msg, chat_id):
    nome, idade = texto_msg.split(",")
    nome = nome[nome.find(":") + 1:]
    idade = idade[idade.find(":") + 1:]
    score = calcular(nome, int(idade))
    msg_final = "Ola, {}! Seu score é {} com base em sua idade {}".format(nome, score, idade)
    url = URL + "sendMessage?text={}&chat_id={}".format(msg_final, chat_id)
    requests.get(url)


def lambda_handler(event, context):
    mensagem = json.loads(event['body'])
    chat_id = mensagem['message']['chat']['id']
    texto = mensagem['message']['text']
    enviar_mensagem(texto, chat_id)
    return {
        'statusCode': 200
    }
