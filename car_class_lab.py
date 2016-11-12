# car_class_lab.py
class Car(object):
    def __init__(self, car_name='General', car_model='GM',
                 car_type='saloon', car_doors=4, car_wheels=4):
        self.__car_name = car_name
        self.__car_model = car_model
        self._car_doors = car_doors
        self.__car_type = car_type
        self._car_wheels = car_wheels
        self.speed = 0

    @property
    def name(self):
        return self.__car_name

    @property
    def model(self):
        return self.__car_model

    @property
    def num_of_doors(self):
        if self.__car_name in ['Koenigsegg', 'Porshe']:
            self._car_doors = 2
            return self._car_doors
        return self._car_doors

    @property
    def num_of_wheels(self):
        if self.__car_type == 'trailer':
            self._car_wheels = 8
            return self._car_wheels
        return self._car_wheels

    def is_saloon(self):
        if self.__car_type == 'saloon':
            return True
        return False

    @property
    def num_of_wheels(self):
        if self.__car_type == 'trailer':
            self._car_wheels = 8
            return self._car_wheels
        return self._car_wheels

    @property
    def type(self):
        return self.__car_type

    def drive(self,  drive_number):
        if self.type == 'trailer':
            if drive_number in range(1, 8):
                self.speed = 11 * drive_number
                return self
            return self
        else:
            if drive_number in range(1, 4):
                self.speed = 997 + drive_number
                return self
            return self

def main():
    man = Car('MAN', 'Truck', 'trailer')
    moving_man = man.drive(7)
    moving_man_instance = isinstance(moving_man, Car)
    moving_man_type = type(moving_man) is Car
    print(moving_man_instance, moving_man_type, moving_man.speed, man.speed)

    man = Car('Mercedes', 'SLR500')
    parked_speed = man.speed
    moving_speed = man.drive(3).speed

    print(parked_speed, moving_speed)

    honda = Car('Honda')
    print(type(honda) is Car)

    man = Car('MAN', 'Truck', 'trailer')
    koenigsegg = Car('Koenigsegg', 'Agera R')
    print(man.num_of_wheels, koenigsegg.num_of_wheels)

    opel = Car('Opel', 'Omega 3')
    porshe = Car('Porshe', '911 Turbo')
    print(opel.num_of_doors,porshe.num_of_doors,Car('Koenigsegg', 'Agera R').num_of_doors)

    toyota = Car('Toyota', 'Corolla')
    print(toyota.name, toyota.model)
if __name__ == '__main__':main()