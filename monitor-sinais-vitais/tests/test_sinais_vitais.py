import pytest
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from leito import *

@pytest.fixture
def leito():
    return Leito()

def test_inicializacao(leito):
    assert leito.temperatura == 0
    assert leito.spo2 == 0
    assert leito.freq_respiratoria == 0
    assert leito.freq_cardiaca == 0
    assert leito.pressao_sistolica == 0
    assert leito.pressao_diastolica == 0
    assert leito.alertas == []

def test_gerar_sinais_vitais(leito):
    leito.gerar_sinais_vitais()

    assert leito.temperatura >= 33 and leito.temperatura <= 40
    assert leito.spo2 >= 80 and leito.spo2 <= 100
    assert leito.freq_respiratoria >= 10 and leito.freq_respiratoria <= 60
    assert leito.freq_cardiaca >= 40 and leito.freq_cardiaca <= 190
    assert leito.pressao_sistolica >= 100 and leito.pressao_sistolica <= 180
    assert leito.pressao_diastolica >= 60 and leito.pressao_diastolica <= 90

def test_gerar_alertas(leito):
    leito.gerar_sinais_vitais()  # Gerar sinais vitais antes de gerar alertas
    leito.gerar_alertas()

    assert isinstance(leito.alertas, list)

def test_get_sinais_vitais(leito):
    leito.gerar_sinais_vitais()
    leito.gerar_alertas()

    sinais_vitais = leito.get_sinais_vitais()

    assert isinstance(sinais_vitais, dict)
    assert "sinais_vitais" in sinais_vitais
    assert "temperatura" in sinais_vitais["sinais_vitais"]
    assert "spo2" in sinais_vitais["sinais_vitais"]
    assert "freq_cardiaca" in sinais_vitais["sinais_vitais"]
    assert "freq_respiratoria" in sinais_vitais["sinais_vitais"]
    assert "pressao_arterial" in sinais_vitais["sinais_vitais"]
    assert "alertas" in sinais_vitais["sinais_vitais"]