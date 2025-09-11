from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict

from apps.todo.models import Task, Log
from apps.todo.api.v1.serializers import TaskSerializer


# Write your signals here


@receiver(pre_save, sender=Task)
def pre_logger_handler(sender, instance, **kwargs):
    if instance.id is not None:
        object = instance.__class__.objects.filter(id=instance.id).first()
        old_values = TaskSerializer(object).data
    else:
        old_values = TaskSerializer(instance).data
    setattr(instance, "old_values", old_values)


@receiver(post_save, sender=Task)
def post_logger_handler(sender, instance, created, **kwargs):
    actual_old_values = dict()
    actual_new_values = dict()
    new_values = TaskSerializer(instance).data
    if created:
        old_values = {}
        Log.objects.create(
            old_value=old_values,
            new_value=new_values,
            content_object=instance,
            user_id=instance.user_id,
        )
    else:
        old_values = getattr(instance, "old_values")
        print(old_values)
        print(new_values)
        for field in old_values.keys():  # type: ignore
            if old_values[field] != new_values[field]:  # type: ignore
                actual_new_values[field] = new_values[field]  # type: ignore
                actual_old_values[field] = old_values[field]  # type: ignore

        Log.objects.create(
            old_value=actual_old_values,
            new_value=actual_new_values,
            content_object=instance,
            user_id=instance.user_id,
        )
