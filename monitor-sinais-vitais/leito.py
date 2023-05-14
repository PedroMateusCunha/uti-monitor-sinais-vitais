"""Modulo para monitoramento do leito hospitalar."""
import random

class Leito:
    """
    Classe para monitoramento do leito hospitalar
    """
    def __init__(self):
        """
        Metodo para inicializar os atributos do monitoramento leito hospitalar
        """
        self.temperatura = 0
        self.spo2 = 0
        self.freq_respiratoria = 0
        self.freq_cardiaca = 0
        self.pressao_sistolica = 0
        self.pressao_diastolica = 0
        self.alertas = []
        
    def gerar_sinais_vitais(self):
        """
        Metodo para gerar sinais vitais para o monitoramento leito hospitalar
        """
        self.temperatura = random.randint(33, 40)
        self.spo2 = random.randint(60, 100)
        self.freq_respiratoria = random.randint(10, 60)
        self.freq_cardiaca = random.randint(40, 190)
        self.pressao_sistolica = random.randint(100, 180)
        self.pressao_diastolica = random.randint(60, 90)

    def gerar_alertas(self):
        """
        Metodo para gerar alertas para o monitoramento leito hospitalar
        """
        limites = {
            "temperatura": {"min": 34, "max": 40},
            "spo2": {"min": 90, "max": 100},
            "freq_respiratoria": {"min": 12, "max": 16},
            "freq_cardiaca": {"min": 70, "max": 100},
            "pressao_sistolica": {"min": 90, "max": 120},
            "pressao_diastolica": {"min": 60, "max": 80} #coloca min e max em contants também 
        } #Pode ser um "static" um atributo da prórpia classe

        sinais_vitais = {
            "temperatura": self.temperatura, #repetição dessas string, coloca numa classe "constants" e sabe a variável em vez da própria string
            "spo2": self.spo2,
            "freq_respiratoria": self.freq_respiratoria,
            "freq_cardiaca": self.freq_cardiaca,
            "pressao_sistolica": self.pressao_sistolica,
            "pressao_diastolica": self.pressao_diastolica,
        }

        self.alertas = []
        for sinal, limite in limites.items():
            if sinais_vitais[sinal] < limite["min"]:
                self.alertas.append(f"{sinal}_baixa")
            elif sinais_vitais[sinal] > limite["max"]:
                self.alertas.append(f"{sinal}_alta")
        
    def get_sinais_vitais(self):
        """
        Metodo para recuperar os sinais vitais para o monitoramento leito hospitalar
        """
        return {
                    "sinais_vitais": {
                    "temperatura": self.temperatura,
                    "spo2": self.spo2,
                    "freq_cardiaca": self.freq_cardiaca,
                    "freq_respiratoria": self.freq_respiratoria,
                    "pressao_arterial": f"{self.pressao_sistolica}/{self.pressao_diastolica}",
                    "alertas": self.alertas
                    }
                }
