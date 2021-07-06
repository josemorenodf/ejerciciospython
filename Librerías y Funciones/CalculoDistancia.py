import math

def distancia():
    r = 6371  # km (Radio de la Tierra)
    print("Primera coordenada")
    Lat1 = float(input("Coordenada 1, latitud 1: "))
    long1= float(input("Coordenada 1, longitud 1: "))
    print("Segunda coordenada")
    Lat2 = float(input("Coordenada 2, latitud 2: "))
    long2 = float(input("Coordenada 2, longitud 2: "))

    # Cálculo de los deltas
    dlat = math.radians((Lat2 - Lat1))
    dlon = math.radians((long2 - long1))
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(Lat1)) * math.cos(math.radians(Lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # Cálculo de la distancia
    d = r * c
    print("La distancia en kilómetros es:",round(d,3))

distancia()