import requests

from cepbr import BuscaEndereco

cep = "01001000"

objeto_cep = BuscaEndereco(cep)

#r = requests.get('https://viacep.com.br/ws/01001000/json/')


bairro, cidade, uf = objeto_cep.acesso_via_cep()

print(bairro, cidade, uf)