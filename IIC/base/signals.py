from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from rnd.models import facult , patent , book , bookChapter , copyright , journal
from .models import achievement, notice, activity, gallery, teamMember, certificate , iicInfo , ipr , incubation , meeting
from .utils import get_file_fields, delete_file


# 🔄 Delete old file when file is changed
@receiver(pre_save, sender=facult)
@receiver(pre_save, sender=achievement)
@receiver(pre_save, sender=notice)
@receiver(pre_save, sender=activity)
@receiver(pre_save, sender=gallery)
@receiver(pre_save, sender=teamMember)
@receiver(pre_save, sender=certificate)
@receiver(pre_save, sender=iicInfo)
@receiver(pre_save, sender=ipr)
@receiver(pre_save, sender=incubation)
@receiver(pre_save, sender=meeting)
@receiver(pre_save, sender=patent)
@receiver(pre_save, sender=book)
@receiver(pre_save, sender=bookChapter)
@receiver(pre_save, sender=journal)
@receiver(pre_save, sender=copyright)
def delete_old_files_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in get_file_fields(instance):
        old_file = getattr(old_instance, field)
        new_file = getattr(instance, field)

        if old_file and old_file != new_file:
            delete_file(old_file)


# 🗑️ Delete files when instance is deleted
@receiver(post_delete, sender=facult)
@receiver(post_delete, sender=achievement)
@receiver(post_delete, sender=notice)
@receiver(post_delete, sender=activity)
@receiver(post_delete, sender=gallery)
@receiver(post_delete, sender=teamMember)
@receiver(post_delete, sender=certificate)
@receiver(post_delete, sender=iicInfo)
@receiver(post_delete, sender=ipr)
@receiver(post_delete, sender=incubation)
@receiver(post_delete, sender=meeting)
@receiver(post_delete, sender=patent)
@receiver(post_delete, sender=book)
@receiver(post_delete, sender=bookChapter)
@receiver(post_delete, sender=journal)
@receiver(post_delete, sender=copyright)
def delete_files_on_delete(sender, instance, **kwargs):
    for field in get_file_fields(instance):
        delete_file(getattr(instance, field))