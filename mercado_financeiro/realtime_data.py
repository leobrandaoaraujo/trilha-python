#pip install MetaTrader5

import MetaTrader5 as mt5
import time

mt5.initialize() #Abre o MetaTrader.

simbolos = mt5.symbols_get()
simbolos[0].name

mt5.symbol_select("EGIE3") #Adiciona o ticker no MetaTrader.
preco_realtime = mt5.symbol_info("EGIE3").last
retorno_realtime = mt5.symbol_info("EGIE3").price_change

tempo = time.time() + 10 #Janela de 10 seg.
while time.time() < tempo:
        tick = mt5.symbol_info_tick("EGIE3").last
        print(f"Fechamento: {tick.last()}")
        print(f"Compra: {tick.ask()}")
        print(f"Venda: {tick.bid()}")
        time.sleep(1)