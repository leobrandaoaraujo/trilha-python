#pip install python-bcb

from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

#Calcular a rentabilidade do capital investido no período pela frequência.
#capital = float(input("Informe o capital investido: "))
#frequencia = input("Informe a frequência do período [Y | M | D]: ")
#data_inicio = datetime.strptime(input("Informe a data inicial do período [YYYY/MM/DD] Deve ser maior que 1995/01/01: "), "%Y/%m/%d").date()
#data_final = datetime.strptime(input("Informe a data final do período [YYYY/MM/DD]: "), "%Y/%m/%d").date()

#taxas_selic = sgs.get({"selic": 11}, start=data_inicio, end=data_final) / 100

#capital_acumulado = round(capital * (1 + taxas_selic["selic"]).cumprod() - 1, 2)
#capital_acumulado_com_frequencia = capital_acumulado.resample(frequencia).last()
#print(capital_acumulado_com_frequencia)

#Analisar janelas de investimento (Ex.: 500 dias).
data_inicio_janela = date(2000,1, 1)
data_final_janela = date(2022, 3, 31)
taxas_selic_janela = sgs.get({"selic": 11}, start=data_inicio_janela, end=data_final_janela) /100
janela = ((1 + taxas_selic_janela).rolling(window=500).apply(np.prod) - 1)
janela = janela.reset_index()
janela.columns = ["data_final", "retorno_janela"]

janela["data_inicial"] = janela["data_final"].shift(500)
janela = janela.dropna()
maior_retorno = janela["retorno_janela"].max()
print(janela[janela["retorno_janela"] == maior_retorno])
