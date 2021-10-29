class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        TV._numTV += 1
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
    
    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getControl(self):
        return self._control

    def setControl(self, control):
        self._control = control

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        self._volumen = volumen if volumen <= 7 and volumen >= 0 and self._estado else self._volumen

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        self._canal = canal if canal <= 120 and canal >= 1 and self._estado else self._canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTv):
        cls._numTV = numTv
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        self._canal = self._canal + 1 if self._canal < 120 and self._estado else self._canal

    def canalDown(self):
        self._canal = self._canal - 1 if self._canal > 1 and self._estado else self._canal

    def volumenUp(self):
        self._volumen = self._volumen + 1 if self._volumen < 7 and self._volumen and self._estado else self._volumen

    def volumenDown(self):
        self._volumen = self._volumen - 1 if self._volumen > 0 and self._volumen and self._estado else self._volumen
