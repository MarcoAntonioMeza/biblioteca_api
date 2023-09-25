from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Usuario

@receiver(post_save, sender=Usuario)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        match instance.tipo:
            case "Administrador":
                usuario, _ =  Group.objects.get_or_create(name='ADMINISTRADOR')
            case "Cliente":
                usuario, _ =  Group.objects.get_or_create(name='CLIENTE')
        instance.groups.add(usuario)


@receiver(pre_save, sender=Usuario)
def update_user_to_group(sender, instance, **kwargs):
    #Elimina sus grupos
    instance.groups.clear()
    match instance.tipo:
        case "Administrador":
            usuario, _ =  Group.objects.get_or_create(name='ADMINISTRADOR')
        case "Cliente":
            usuario, _ =  Group.objects.get_or_create(name='CLIENTE')
    instance.groups.add(usuario)