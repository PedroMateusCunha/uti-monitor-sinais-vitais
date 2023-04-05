from fastapi import FastAPI
import random

class Leito:
    def __init__(self):
        self.temperatura = 0
        self.spo2 = 0
        self.freq_respiratoria = 0
        self.freq_cardiaca = 0
        self.pressao_arterial = ""
        self.alertas =[]
        
    def gerar_sinais_vitais(self):
        self.temperatura = random.randint(33, 40)
        self.spo2 = random.randint(60, 100)
        self.freq_respiratoria = random.randint(10, 60)
        self.freq_cardiaca = random.randint(40, 190)
        self.pressao_arterial = f"{random.randint(100, 180)}/{random.randint(60, 90)}"

    def gerar_alertas(self):
        LIMITE_TEMP   = {"min":34, "max":40}
        LIMITE_SPO2   = {"min":90, "max":100}
        LIMITE_FR     = {"min":12, "max":16}
        LIMITE_FC     = {"min":70, "max":100}

        if self.temperatura < LIMITE_TEMP["min"]:
            self.alertas.append("temp_baixa")
        if self.temperatura > LIMITE_TEMP["max"]:
            self.alertas.append("temp_alta")

        if self.spo2 < LIMITE_SPO2["min"]:
            self.alertas.append("spo2_baixa")
        if self.spo2 > LIMITE_SPO2["max"]:
            self.alertas.append("spo2_alta")

        if self.freq_respiratoria < LIMITE_FR["min"]:
            self.alertas.append("fr_baixa")
        if self.freq_respiratoria > LIMITE_FR["max"]:
            self.alertas.append("fr_alta")

        if self.freq_cardiaca < LIMITE_FC["min"]:
            self.alertas.append("fc_baixa")
        if self.freq_cardiaca > LIMITE_FC["max"]:
            self.alertas.append("fc_alta")

        # if self.pressao_arterial < LIMITE_FC["min"]:
        #     self.alertas.append("pa_baixa")
        # if self.pressao_arterial > LIMITE_FC["max"]:
        #     self.alertas.append("pa_alta")

        
    def get_sinais_vitais(self):
        return {
            "sinais_vitais": {
                "temperatura": self.temperatura,
                "spo2": self.spo2,
                "freq_cardiaca": self.freq_cardiaca,
                "freq_respiratoria": self.freq_respiratoria,
                "pressao_arterial": self.pressao_arterial
            },
            "alertas": self.alertas
        }

app = FastAPI()
leito = Leito()

@app.get("/")
def read_root():
    return {"message": "Monitor de sinais vitais em um leito de UTI"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/sinais_vitais")
def sinais_vitais():
    leito.gerar_sinais_vitais()
    leito.gerar_alertas()
    return leito.get_sinais_vitais()