import random
import math

class Vehiculo():
    def __init__(self):
        print('this is a vehicle')

    def fuerzaMotor(self):
        torque = random.randint(0, 9)
        return torque


class Camion(Vehiculo):
    def __init__(self):
        pass

    def rendimiento(self):
        avance = 2 * super().fuerzaMotor() + 1
        return avance




class Tractor(Vehiculo):
    def __init__(self):
        pass

    def rendimiento(self):
        avance = round(math.log2(2) * super().fuerzaMotor())
        return avance


class Sedan(Vehiculo):
    def __init__(self):
        pass

    def rendimiento(self):
        avance = 3 * (super().fuerzaMotor())**2
        return avance


class Bus(Vehiculo):
    def __init__(self):
        pass

    def rendimiento(self):
        avance = 5 * super().fuerzaMotor()
        return avance


camion = Camion()
tractor = Tractor()
sedan = Sedan()
bus = Bus()


#carrera

carrera = {'camion': camion, 'tractor':tractor, 'sedan':sedan, 'bus':bus}


for item in carrera.keys():
    print(carrera[item].rendimiento())


