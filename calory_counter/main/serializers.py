import io
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Profile, Vegetable, Record

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_age(self, value, age=None):
        if value > 100 or age < value:
            raise serializers.ValidationError('Неверный возраст')
        return age

    class Meta:
        model = Profile
        fields = "__all__"

class VegetableSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def create(self, validated_data):
        return Vegetable.objects.create(**validated_data)

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название овоща должно содержать как минимум 2 символа")
        return value

    def validate_calories(self, value):
        if value <= 0:
            raise serializers.ValidationError("Значение калорий должно быть положительным числом")
        return value

    def validate_protein(self, value):
        if value <= 0:
            raise serializers.ValidationError("Значение белков должно быть положительным числом")
        return value

    def validate_fat(self, value):
        if value <= 0:
            raise serializers.ValidationError("Значение жиров должно быть положительным числом")
        return value

    def validate_carbohydrates(self, value):
        if value <= 0:
            raise serializers.ValidationError("Значение углеводов должно быть положительным числом")
        return value
    class Meta:
        model = Vegetable
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"

    # сериалайзер на базе класса Serializer (получает данные в json-формате, добавляет и изменяет их)
    # name = serializers.CharField(max_length=200)
    # calories = serializers.IntegerField()
    # proteins = serializers.FloatField()
    # fats = serializers.FloatField()
    # carbohydrates = serializers.FloatField()
    #
    # def create(self, validated_data):
    #     return Vegetable.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.calories = validated_data.get("calories", instance.calories)
    #     instance.proteins = validated_data.get("proteins", instance.proteins)
    #     instance.fats = validated_data.get("fats", instance.fats)
    #     instance.carbohydrates = validated_data.get("carbohydrates", instance.name)
    #     instance.save()
    #     return instance

# class VegetableModel:
#     def __init__(self, name, calories, proteins, fats, carbohydrates):
#         self.name = name
#         self.calories = calories
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates

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