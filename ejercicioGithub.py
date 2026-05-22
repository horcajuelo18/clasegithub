class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
# Crear una instancia de la clase Persona 
Jeshua= Persona( "Jeshua", 17 )
Pau = Persona('Pau', 14) 
Ibai = Persona('Ibai', 14)


# saludar
Jeshua.saludar()
Pau.saludar()
Ibai.saludar()