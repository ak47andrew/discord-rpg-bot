BASE = str | int | float | bool
JsonSerializable = type("JsonSerializable", (), {})


def to_json(obj: JsonSerializable) -> dict:
    out = dict()

    for field_name in dir(obj):
        if field_name.startswith("_") or field_name.endswith("_"):
            continue
        field_value = getattr(obj, field_name)
        if isinstance(field_value, JsonSerializable):
            out.update({
                field_name: to_json(field_value)
            })
        elif isinstance(field_value, dict | BASE):
            out.update({
                field_name: field_value
            })
        elif isinstance(field_value, list):
            if len(field_value) == 0 or isinstance(field_value[0], dict | list | BASE | JsonSerializable):
                out.update({
                    field_name: field_value
                })

    return out
