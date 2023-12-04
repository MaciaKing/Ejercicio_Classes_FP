
class TratamientoFichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        f = open(self.nombre_fichero, "a")
        f.write(line_to_write)
        f.write("\n")
        f.close()
        
    def read_file(self):
        f = open(self.nombre_fichero, "r")
        print(f.read())
        f.close()

### Main
if __name__ == '__main__':
    f = TratamientoFichero("prueba.txt")
    f.write_file("Juan 12")
    f.read_file()
