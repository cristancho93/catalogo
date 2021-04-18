class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/arma.png"
        self.descripcion = "arma del humano"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/arma.png"
        self.descripcion = "arma del orco"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/escudo.png"
        self.descripcion = "escudo humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/escudo.png"
        self.descripcion = "escudo orcos"


# Componentes del decorador
class Producto2:
    def __init__(self):
        self.grupo = ""
        self.imagen = ""
        self.descripcion = ""

class Cuerpo(Producto2):
    def __init__(self):
        Producto2.__init__(self)

class CuerpoHumano(Cuerpo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/cuerpo.jpg"
        self.descripcion = "miden 1.80 metros"

class CuerpoOrcos(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/cuerpo.jpg"
        self.descripcion = "miden 2.5 metros"


class Montura(Producto2):
    def __init__(self):
        Producto2.__init__(self)

class MonturaHumano(Montura):
    def __init__(self):
        self.grupo = "Humano"
        self.imagen = "static/imagenes/humanos/montura.jpg"
        self.descripcion = "General mente son de cuero"

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/montura.jpg"
        self.descripcion = "General mente son peiles"

