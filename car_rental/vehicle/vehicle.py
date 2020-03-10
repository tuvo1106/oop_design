#!/usr/bin/env python3

from abc import ABC


class Vehicle(ABC):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof,
                 status, model, make, manufacturing_year, mileage):
        self.__license_number = license_num
        self.__stock_number = stock_num
        self.__passenger_capacity = capacity
        self.__barcode = barcode
        self.__has_sunroof = has_sunroof
        self.__status = status
        self.__model = model
        self.__make = make
        self.__manufacturing_year = manufacturing_year
        self.__mileage = mileage
        self.__log = []

    def reserve_vehicle(self):
        pass

    def return_vehicle(self):
        pass


class Car(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof,
                 status, model, make, manufacturing_year, mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type


class Van(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof,
                 status, model, make, manufacturing_year, mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type


class Truck(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof,
                 status, model, make, manufacturing_year, mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type
