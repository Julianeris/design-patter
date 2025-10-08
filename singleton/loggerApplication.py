class LoggerApplication:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerApplication, cls).__new__(cls, *args, **kwargs)

        cls._instance.logs = []
        
        return cls._instance

    def log_message(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

    def show_all_logs(self):
        print("Todos os logs registrados: ")
        for log in self.logs:
            print(log)
            
logger1 = LoggerApplication()
logger2 = LoggerApplication()

logger1.log_message("Inicialização do sistema")
logger2.log_message("Conexão com o banco de dados bem-sucedida")
logger1.log_message("Erro ao carregar o arquivo de configuração")

print(logger1 is logger2)

logger1.show_all_logs()