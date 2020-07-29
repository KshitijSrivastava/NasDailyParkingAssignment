
from park.models import CarPark


class ParkingInfoService():
    def __init__(self, slot, car_number):
        self.slot = slot
        self.car_number = car_number

    def get_info(self):
        if self.slot:
            try:
                carpark = CarPark.objects.get(
                    slot=self.slot, active = True)
                return {'car_number': carpark.car_number}
            except:
                return {'error': 'No Car parked'}

        if self.car_number:
            try:
                carpark = CarPark.objects.get(
                    car_number=self.car_number, active = True)
                return {'slot': carpark.slot}
            except:
                return {'error': 'No Car parked'}