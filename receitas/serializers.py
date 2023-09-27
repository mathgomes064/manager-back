from receitas.models import Receita
from rest_framework import serializers

class DecimalSerializer(serializers.DecimalField):
    def to_representation(self, obj):
        return round(float(obj), 2)

class ReceitaSerializer(serializers.ModelSerializer):
    entrada = DecimalSerializer(max_digits=10, decimal_places=2)

    class Meta:
        model = Receita
        fields = '__all__'

    def create(self, validated_data: dict) -> Receita:
        return Receita.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.entrada = validated_data.get('entrada', instance.entrada)
        
        instance.save()
        return instance