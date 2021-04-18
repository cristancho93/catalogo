from fabricas import *

class ComponenteDecorador():

    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass


class ComponenteHumanos(ComponenteDecorador):

    def crear_cuerpo(self):
        return FabricaHumanosV2.crear_cuerpo(self)

    def crear_montura(self):
        return FabricaHumanosV2.crear_montura(self)

    def crear_arma(self):
        return FabricaHumanos.crear_arma(self)

    def crear_escudo(self):
        return FabricaHumanos.crear_escudo(self)


class ComponenteOrcos(ComponenteDecorador):

    def crear_cuerpo(self):
        return FabricaOrcosV2.crear_cuerpo(self)

    def crear_montura(self):
        return FabricaOrcosV2.crear_montura(self)

    def crear_arma(self):
        return FabricaOrcos.crear_arma(self)

    def crear_escudo(self):
        return FabricaOrcos.crear_escudo(self)


class Decorador(ComponenteDecorador):

    def __init__(self, cHumanos, cOrcos):
        self._cHumanos = cHumanos
        self._cOrcos = cOrcos

    def crear_montura(self):
        pass

    def crear_cuerpo(self):
        pass

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass


class DecoradorHumanos(Decorador):

    def crear_montura(self):
        return self._cHumanos.crear_montura()

    def crear_cuerpo(self):
        return self._cHumanos.crear_cuerpo()

    def crear_arma(self):
        return self._cHumanos.crear_arma()

    def crear_escudo(self):
        return self._cHumanos.crear_escudo()


class DecoradorOrcos(Decorador):

    def crear_montura(self):
        return self._cOrcos.crear_montura()

    def crear_cuerpo(self):
        return self._cOrcos.crear_cuerpo()

    def crear_arma(self):
        return self._cOrcos.crear_arma()

    def crear_escudo(self):
        return self._cOrcos.crear_escudo()
