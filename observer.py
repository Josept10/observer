class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


# Ejemplo de uso

class KeyboardInput(Observable):
    def start(self):
        while True:
            user_input = input("Ingrese un dato: ")
            self.notify_observers(user_input)


class DataPrinter(Observer):
    def update(self, data):
        print("Dato ingresado:", data)


class DataLogger(Observer):
    def update(self, data):
        with open("log.txt", "a") as file:
            file.write("Dato ingresado: " + data + "\n")


# Crear instancias de los objetos

keyboard = KeyboardInput()
printer = DataPrinter()
logger = DataLogger()

# Registrar los observadores en la entrada de teclado

keyboard.add_observer(printer)
keyboard.add_observer(logger)

# Iniciar la entrada de teclado

keyboard.start()
