#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
#  A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#  La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación (0.0,0.4,0.6): "))
if puntos == inaceptable:
    print("Inaceptable y cobraras de bonificación " + str(2400 * inaceptable)+"€")
elif puntos == aceptable:
    print("Aceptable y cobraras de bonificación " + str(2400 * aceptable)+"€")
elif puntos >= meritorio:
    print("Meritorio y cobraras de bonificación " + str(2400 * meritorio)+"€")
else:
    print("Puntos no válidos")