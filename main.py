from cpf_cnpj import DocCpf, DocCnpj
from PYBRDOC import cnpj
import requests

#Criando um cpf
cpf = '82649935081'
numero_cnpj = '46992857000136'

#adicionando o cpf a classe cpf
objeto_cpf = DocCpf(cpf)

#adicionando o cnpj ao objeto importado

documento = DocCnpj(numero_cnpj)

print(documento)





