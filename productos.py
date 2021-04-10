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



class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)