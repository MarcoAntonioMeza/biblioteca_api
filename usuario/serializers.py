from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

        read_only_fields  = ('is_active',)
        #fields = ('__all__') 
        exclude = (
            "is_superuser",
            "last_login",
            "is_staff",
            "groups",
            "user_permissions"
        )

    def create(self,data):
        user = Usuario(**data)
        user.set_password(data['password'])
        user.save()
        return user 
        
    def update(self,instance,data):
        update_user = super().update(instance,data)
        update_user.set_password(data['password'])
        update_user.save()
        return update_user
    




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = f'{user.name} {user.last_name}'
        return token