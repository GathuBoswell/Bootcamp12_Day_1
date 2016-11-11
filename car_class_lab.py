# car_class_lab.py
class Car():
    def __init__(self, car_model='GM', car_name='general1'):
        self.__car_name = car_name
        self.__car_model = car_model

    @property
    def name(self):
        return self.__car_name

    @property
    def model(self):
        return self.__car_model


