class Singleton:
    """Classe Singleton que garante que apenas uma instância exista."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Cria uma nova instância se não existir."""
        if not cls._instance:
            """Cria uma nova instância se não existir."""
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            """Atribui um valor padrão."""
            cls._instance.value = None
        """Retorna a instância existente."""
        return cls._instance

    def __init__(self):
        """Inicializa a instância."""
        self.value = None


singleton1 = Singleton()
singleton2 = Singleton()
singleton1.value = 'Unique Value'


print(singleton1.value)
print(singleton2.value)
print(singleton1 is singleton2)


