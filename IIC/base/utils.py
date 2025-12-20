import random


def generate_otp():
    return str(random.randint(100000 , 999999))



def get_file_fields(instance):
    return [
        field.name
        for field in instance._meta.fields
        if field.get_internal_type() in ('FileField', 'ImageField')
    ]


def delete_file(file_field):

    if file_field and file_field.name:
        file_field.storage.delete(file_field.name)