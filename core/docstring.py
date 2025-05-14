def auto_docstring():
    def dec(instance):
        if instance.__doc__:
            instance.__doc__ += """\n\n"""
        else:
            instance.__doc__ = """"""

        if instance.__dict__.get("ordering"):
            instance.__doc__ += "```сортировка по умолчанию```: \n\n * "
            instance.__doc__ += "\n * ".join(instance.ordering)
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("ordering_fields"):
            instance.__doc__ += (
                "```ordering``` сортировка по следующим категориям: \n\n * "
            )
            instance.__doc__ += "\n * ".join(instance.ordering_fields)
            instance.__doc__ += "\n\n"

        if instance.__dict__.get("search_fields"):
            instance.__doc__ += "```search``` поиск по полям: \n\n * "
            instance.__doc__ += "\n * ".join(instance.search_fields)
            instance.__doc__ += "\n\n"

        return instance

    return dec
