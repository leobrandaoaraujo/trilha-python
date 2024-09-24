#pip install mplcyberpunk
#pip install yfinance==0.2.40
#pip install setuptools

import yfinance as yf
import mplcyberpunk
import pandas as pd
import matplotlib.pyplot as plt
import win32com.client as win32

tickers = ["^BVSP", "^GSPC", "BRL=X"]
dados_mercado = yf.download(tickers, period = "6mo")
dados_mercado = dados_mercado["Adj Close"]
dados_mercado = dados_mercado.dropna()
dados_mercado.columns = ["DOLAR", "IBOVESPA", "S&P500"]
#print(dados_mercado)

plt.style.use("cyberpunk")
plt.plot(dados_mercado["IBOVESPA"])
plt.title("IBOVESPA")
plt.show
plt.savefig("ibovespa.jpg")

plt.plot(dados_mercado["DOLAR"])
plt.title("DOLAR")
plt.show
plt.savefig("dolar.jpg")

plt.plot(dados_mercado["S&P500"])
plt.title("S&P500")
plt.show
plt.savefig("sp500.jpg")

retornos_diarios = dados_mercado.pct_change()

retorno_dolar = str(round(retornos_diarios["DOLAR"].iloc[-1] * 100, 2)) + "%"
retorno_ibovespa = str(round(retornos_diarios["IBOVESPA"].iloc[-1] * 100, 2)) + "%"
retorno_sp500 = str(round(retornos_diarios["S&P500"].iloc[-1] * 100, 2)) + "%"

outlook = win32.Dispatch("outlook.apllication")

email = outlook.CreateItem(0)
email.To = "leonardo.brandao@gmail.com"
email.Subject = "Relatório de Mercado"
email.Body = f'''Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}.
* O Dólar teve o retorno de {retorno_dolar}.
* O S&P500 teve o retorno de {retorno_sp500}.

Segue em anexo, a performance destes ativos dos últimos seis meses.

Att,

Melhor estágiário do mundo.'''

anexo_ibovespa = r"\.ibovespa.jpg"
anexo_dolar = r"\.dolar.jpg"
anexo_sp500 = r"\.sp500.jpg"

email.Attachements.Add(anexo_ibovespa)
email.Attachements.Add(anexo_dolar)
email.Attachements.Add(anexo_sp500)

email.Send()