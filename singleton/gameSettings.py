class GameSettingsSingleton:
    _settings = None

    def __new__(cls, *args, **kwargs):

        """ Configura o 'settigns' """
        if not cls._settings:
            cls._settings = super(GameSettingsSingleton, cls).__new__(cls, *args, **kwargs)

            """ Aqui que eu adiciono as variaveis com os valores de padrão """
            cls._settings.volume = 50
            cls._settings.resoluton = "1920x1080"
            cls._settings.difficulty = "normal"

        """ Retorna o 'settigns' """
        return cls._settings
    
    def set_volume(self, value):
        self.volume = value

    def set_resoluton(self, resolution):
        self.resolution = resolution
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

#teste na implementação

settings1 = GameSettingsSingleton()
settings2 = GameSettingsSingleton()

settings1.set_volume(30)
settings1.set_resoluton("1280x720")
settings1.set_difficulty("hard")

print(settings1.volume)
print(settings2.resolution)
print(settings1.difficulty)
print(settings1 is settings2)

