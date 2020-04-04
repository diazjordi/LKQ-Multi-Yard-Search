class LKQYard:

    def __init__(self, name, address, distance, homepage, vehicle_inventory):
        self.name = name
        self.address = address
        self.distance = distance
        self.homepage = homepage
        self.vehicle_inventory = vehicle_inventory

    def yard_info(self):
        print(self.name + ' ' + self.distance)