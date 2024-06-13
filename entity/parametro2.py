import string


class Parametro2:
    _instance = None
    
    def __init__(self, path2: string = None):
        self.path2 = path2

    @classmethod
    def get_instance(cls, **kwargs):
        if cls._instance is None:
            cls._instance = cls(**kwargs)
        return cls._instance
    
    def __str__(self):
        return self.path2