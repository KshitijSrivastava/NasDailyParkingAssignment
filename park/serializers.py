from rest_framework import serializers

class CarParkSerializer(serializers.Serializer):
    car_number = serializers.CharField()


class UnparkCarSerializer(serializers.Serializer):
    slot = serializers.CharField()