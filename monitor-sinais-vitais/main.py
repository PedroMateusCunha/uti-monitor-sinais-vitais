"""
Modulo para inicialização e disponilibilização do serviço
relacionado ao painel de monitoramento de sinais vitais.
"""
from fastapi import FastAPI
from leito import Leito

app = FastAPI()
leito = Leito()

@app.get("/")
def read_root():
    """Metodo para roteamento inicial do componente"""
    return {"message": "Monitor de sinais vitais em um leito de UTI"}

@app.get("/health")
def health_check():
    """Metodo para roteamento para checagem de status do paciente"""
    return {"status": "ok"}

@app.get("/status")
def sinais_vitais():
    """Metodo para roteamento para geração de sinais vitais"""
    leito.gerar_sinais_vitais()
    leito.gerar_alertas()
    return leito.get_sinais_vitais()
