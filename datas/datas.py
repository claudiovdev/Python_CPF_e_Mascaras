from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.formate_data()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
                        "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                        "Novembro", "Dezembro"]
        mes_cadastro = self.data_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        dia_semana = self.data_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def formate_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_de_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.data_cadastro
        return tempo_cadastro
