# Devuelve el valor de la clave si ya existe y, en caso contrario, le asigna el valor que se pasa como segundo argumento. Si no se especifica este segundo argumento, por defecto es None.

d = {'uno': 1, 'dos': 2}
print(d.setdefault('uno', 1.0)) # Devuelve el valor de la clave si ya existe.
d.setdefault('tres', 3) # Incluye la clave 'tres' y le asigna un valor
d.setdefault('cuatro') # Incluye la clave 'cuatro', pero no le asigna un valor, por lo tanto es None
print(d)