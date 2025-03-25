from datetime import datetime

def horario():
    agora = datetime.now()
    horas = agora.hour
    minutos = agora.minute
    segundos = agora.second

    print(f"Hora atual: {horas} horas {minutos} minutos {segundos} segundos")

horario()