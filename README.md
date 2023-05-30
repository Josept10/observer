# observer
Ejemplo lo que viene hacer el metodo observer 
En este ejemplo, creamos una clase KeyboardInput que hereda de Observable. 
Dentro de esta clase, se crea un bucle infinito que solicita al usuario ingresar un dato por teclado utilizando la función input(). 
Luego, se notifica a los observadores registrados llamando al método notify_observers y pasando el dato ingresado como argumento.
También creamos las clases DataPrinter y DataLogger que heredan de Observer e implementan el método update. 
En el ejemplo, simplemente imprimimos el dato ingresado por pantalla y lo registramos en un archivo de registro, respectivamente.
Luego, creamos instancias de los objetos KeyboardInput, DataPrinter y DataLogger. Registramos los observadores en la entrada de teclado utilizando el método add_observer. 
Finalmente, iniciamos la entrada de teclado llamando al método start() de KeyboardInput, lo que permite al usuario ingresar datos continuamente.
