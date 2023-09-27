from rest_framework import serializers
from .models import Despesa

class DecimalSerializer(serializers.DecimalField):
    def to_representation(self, obj):
        return round(float(obj), 2)

class DespesaSerializer(serializers.ModelSerializer):
    saida = DecimalSerializer(max_digits=10, decimal_places=2)

    class Meta:
        model = Despesa
        fields = '__all__'

    def create(self, validated_data: dict) -> Despesa:
        return Despesa.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.saida = validated_data.get('saida', instance.saida)

        instance.save()
        return instance