from django.core.exceptions import BadRequest


def get_fields(instance):
    return {
        field.name: getattr(instance, field.name) for field in instance._meta.fields
    }


def get_ordering_field(*, key, options):
    as_dict = {
        prefix + key: prefix + field
        for prefix in ("", "-")
        for key, field in options.items()
    }

    if key not in as_dict:
        raise BadRequest(f"Ordering by {key} is not supported!")

    return as_dict[key]
