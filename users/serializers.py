from rest_framework import serializers
from receitas.serializers import ReceitaSerializer
from despesas.serializers import DespesaSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    receitas = ReceitaSerializer(many=True, read_only=True)
    despesas = DespesaSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "password",
            "telefone",
            "receitas",
            "despesas"
        ]
        read_only_fields = [
            "receitas",
            "despesas"
        ]
    
    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)    

        instance.save()

        return instance