"""
MODULE DATETIME
permite manipular fechas de forma sencilla
datetima.now
date.today
date
datetime 
"""
import datetime

print("El dia y la hora de hpy es: ", datetime.datetime.now())
print("El dia de hpy es:", datetime.date.today())
fecha = datetime.date(1984,5,10)
print(fecha)
fechahora = datetime.datetime(2017,11,29,23,19,00,123)
print(fechahora)