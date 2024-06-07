import string


class Parametro:
    _instance = None
    
    def __init__(self, path: string = None):
        self.path = path

    @classmethod
    def get_instance(cls, **kwargs):
        if cls._instance is None:
            cls._instance = cls(**kwargs)
        return cls._instance
    
    def __str__(self):
        return self.path
    