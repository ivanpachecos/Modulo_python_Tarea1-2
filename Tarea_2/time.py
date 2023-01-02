import time 

hora = int(time.strftime('%H'))

if hora >= 19:
    print("Hora de ir a casa")
else:
    print("Esta temprano")