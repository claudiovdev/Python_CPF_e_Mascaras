import re


class Telefone:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Formato de telefone invalido!!!")

    def __str__(self):
        return self.formata_numero()


    def valida_telefone(self, telefone):
        padrao = "([0-9]{2})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resultado = re.findall(padrao, telefone)
        if resultado:
            return True
        else:
            return False

    def formata_numero(self):
        padrao = "([0-9]{2})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        numero_formatado = f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado