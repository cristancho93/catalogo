from productos import *

class Fabrica:

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaHumanos(Fabrica):

    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabrica):

    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()


# Fabrica decorador

class FabricaVersion2():

    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass

class FabricaHumanosV2(FabricaVersion2):

    def crear_cuerpo(self):
        return CuerpoHumano()

    def crear_montura(self):
        return MonturaHumano()


class FabricaOrcosV2(FabricaVersion2):

    def crear_cuerpo(self):
        return CuerpoOrcos()

    def crear_montura(self):
        return MonturaOrcos()
