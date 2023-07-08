from django.core.exceptions import BadRequest


def get_fields(instance):
    return {
        field.name: getattr(instance, field.name) for field in instance._meta.fields
    }


def get_ordering(*, data, options, default):
    key = data.get("ordering", default)
    as_dict = {
        prefix + option: prefix + option for prefix in ("", "-") for option in options
    }

    if key not in as_dict:
        raise BadRequest(f"Ordering by {key} is not supported!")

    return as_dict[key]
