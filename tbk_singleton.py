"""tbk_singleton"""
class Singleton(type):
    """design pattern SINGLETON : ensure that only one instance of hero exist"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
