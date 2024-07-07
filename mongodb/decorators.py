"""Decorators

All the decorators used in this project are defined here.....
"""


def find_many_decorator():
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            try:
                collection = self.get_collection(*args, **kwargs)
            except Exception as e:
                raise Exception("The following error occurred: ", e)
            else:
                if self.param is not None:
                    return collection.find(*self.param)
                else:
                    return collection.find()
        return wrapper
    return decorator

def list_find_decorator_items(func):
    def items(*args, **kwargs):
        return list(func(*args, **kwargs))
    return items