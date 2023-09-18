from rest_framework import serializers

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
    