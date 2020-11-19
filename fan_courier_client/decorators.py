import re


def validate(validation_fields):
    def decorator(func):
        def wrapper(self, **kwargs):
            for field, description in validation_fields.items():
                field_data = kwargs.get(field)

                default_value = description.get('default')
                if default_value and not field_data:
                    kwargs.update({field: default_value})
                    field_data = kwargs.get(field)

                field_type = description.get('type')
                if field_type and not isinstance(field_data, field_type):
                    raise Exception(f"'{field}' must be of the type '{description.get('type', str).__name__}'")

                choices = description.get('choices')

                if callable(choices):
                    choices = choices()

                if choices and field_data not in choices:
                    raise Exception(f"'{field}' its values are {choices}")

                regex_format = description.get('regex')
                if regex_format:
                    regex = re.compile(regex_format, re.I)
                    if not regex.match(field_data):
                        raise Exception(f"Invalid data format. '{regex_format}'")

                if field_data is None:
                    raise Exception(f"Field '{field}' is required")
            return func(self, **kwargs)
        return wrapper
    return decorator
