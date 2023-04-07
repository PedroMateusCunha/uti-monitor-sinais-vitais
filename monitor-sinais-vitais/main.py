from fastapi import FastAPI
from leito import Leito

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