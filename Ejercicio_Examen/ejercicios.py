


if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("ferrari", "200hp")
    c3 = Coche("adsfadsf", "asdf")

    coches= [c1, c2, c3]
    c = Carrera(coches)
    c.empieza_carrera()
    c.muestra_resultado()