from rest_framework import serializers

from .models import Positions, Employee


class PositionsSerializers(serializers.Serializer):
    position = serializers.CharField(max_length=250)
    department = serializers.CharField(max_length=222)


class EmployeeSerializers(serializers.Serializer):
    FIO = serializers.CharField(max_length=250)
    date_birth = serializers.DateField()
    position = serializers.IntegerField()
    zp = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        massage = Employee.objects.create(
            FIO=validated_data['FIO'],
            date_birth=validated_data['date_birth'],
            position=validated_data['position'],
            zp=validated_data['zp']
        )
        return massage

    def update(self, instance, validated_data):
        instance.FIO = validated_data['FIO']
        instance.date_birth = validated_data['date_birth']
        instance.position = validated_data['position']
        instance.zp = validated_data['zp']
        return instance

