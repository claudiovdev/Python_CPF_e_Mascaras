from validate_docbr import CPF
from PYBRDOC import cnpj
import requests
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("documento inválido!!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)



class DocCnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CPF inválido!!!")

    def __str__(self):
        return self.formata_cnpj()

    def valida_cnpj(self, documento):
        if len(documento) == 14:
            return cnpj.validar_cnpj(documento)


    def formata_cnpj(self):
        parte1 = self.cnpj[:2]
        parte2 = self.cnpj[2:5]
        parte3 = self.cnpj[5:8]
        parte4 = self.cnpj[8:12]
        parte5 = self.cnpj[12:]
        formatacao = f'{parte1}.{parte2}.{parte3}/{parte4}-{parte5}'
        return formatacao
