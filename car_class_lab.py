# car_class_lab.py
class Car():
    def __init__(self, car_model='GM', car_name='general1', car_doors=4, car_wheels=4, car_type='saloon'):
        self.__car_name = car_name
        self.__car_model = car_model
        self._car_doors = car_doors
        self.__car_type = car_type
        self._car_wheels = car_wheels

    @property
    def name(self):
        return self.__car_name

    @property
    def model(self):
        return self.__car_model

    @property
    def num_of_doors(self):
        if self.__car_model in ['Koenigsegg', 'Porshe']:
            self._car_doors = 2
            return self._car_doors

    @property
    def num_of_wheels(self):
        if self.__car_type == 'trailer':
            self._car_wheels = 8
            return self._car_wheels
        return self._car_wheels

    @property
    def is_saloon(self):
        if self.__car_type == 'saloon':
            return True
        return False
