class VehicleType:
    Car = "Car"
    Bus = "Bus"
    Truck = "Truck"
    OtherVehicle = "Other vehicles"


class Tollbooth:

    # class members/ static members
    __no_of_vehicles = 0
    __total_amount = 0

    def __init__(self):
        # self.__no_of_vehicle = 0
        # self.__total_amount = 0
        self.vehicle_toll_price = {
            VehicleType.Car: 70,
            VehicleType.Bus: 100,
            VehicleType.Truck: 150,
            VehicleType.OtherVehicle: 70
        }

    @property
    def no_of_vehicles(self):

        return Tollbooth.__no_of_vehicles

    # Getter
    @property
    def get_total_amount(self):
        return Tollbooth.__total_amount

    def __calculate_amount(self, vehicle_type):
        price = self.vehicle_toll_price[vehicle_type]
        Tollbooth.__total_amount += price

    def __count_vehicle(self):
        Tollbooth.__no_of_vehicles += 1

    def collect_toll(self, owner_type, vehicle_type):
        if owner_type != "VIP":
            self.__calculate_amount(vehicle_type)

        self.__count_vehicle()


t1 = Tollbooth()
t1.collect_toll("xyz", VehicleType.Truck)
print(f'Total number of vehicles passed via t1 tollgate : {t1.no_of_vehicles}')
print(f'Total amount collected from t1 tollgate: {t1.get_total_amount}')

# t1.collect_toll("VIP", "car")
# print(f'Total number of vehicles passed via t1 tollgate : {t1.no_of_vehicles}')
# print(f'Total amount collected from t1 tollgate : {t1.get_total_amount}')

# t2 = Tollbooth()
# t2.collect_toll("xyz", "Truck")
# print(f'Total number of vehicles passed via t1 tollgate : {t2.no_of_vehicles}')
# print(f'Total amount collected from t1 tollgate: {t2.get_total_amount}')

# t2.collect_toll("VIP", "car")
# print(f'Total number of vehicles passed via t1 tollgate : {t2.no_of_vehicles}')
# print(f'Total amount collected from t1 tollgate : {t2.get_total_amount}')


# static variable in python
