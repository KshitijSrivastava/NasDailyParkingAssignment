from app.settings import PARKING_LOT_SIZE

from park.models import CarPark

class ParkingService():
    def __init__(self, data):
        self.car_number = data['car_number']
    
    def park_car(self):
        if self.is_parking_full():
            return {
                'error': 'Parking is full'
                }

        free_slots = self.find_free_slots()
        carpark = CarPark.objects.create(
            car_number=self.car_number, active = True, slot = free_slots[0])

        return {
            'slot': carpark.slot
        }


    def find_free_slots(self):
        busy_slots = [car.slot for car in CarPark.objects.filter(active = True)]
        free_slots = [ i for i in range(1, int(PARKING_LOT_SIZE) + 1) if i not in busy_slots]
        return free_slots

    def is_parking_full(self):
        if len(CarPark.objects.filter(active = True)) == int(PARKING_LOT_SIZE):
            return True
        else:
            return False


class UnparkService():
    def __init__(self, data):
        self.slot = data['slot']

    def unpark_car(self):
        try:
            carpark = CarPark.objects.get(
                slot=self.slot, active = True)
            carpark.active = False
            carpark.save()
            return {'message': 'Car unparked'}
        except:
            return {'error': 'Slot Not Present'}