def get_fields(instance):
    return {
        field.name: getattr(instance, field.name) for field in instance._meta.fields
    }
