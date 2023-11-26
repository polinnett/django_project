import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Vegetable

# class VegetableModel:
#     def __init__(self, name, calories, proteins, fats, carbohydrates):
#         self.name = name
#         self.calories = calories
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
class VegetableSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    calories = serializers.IntegerField()
    proteins = serializers.FloatField()
    fats = serializers.FloatField()
    carbohydrates = serializers.FloatField()

# def encode():
#     model = VegetableModel('tomato', 23, 1.0, 1.0, 4.0)
#     model_sr = VegetableSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"name": "tomato", "calories": 23, "proteins": 1.0, "fats": 1.0, "carbohydrates": 4.0}')
#     data = JSONParser().parse(stream)
#     serializer = VegetableSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)