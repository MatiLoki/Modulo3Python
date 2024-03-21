class Pizza:
    tamano = "familiar"
    precio = 10000

    @classmethod
    def validar_elemento(cls, solicitado, posibles):
        return solicitado.lower() in posibles

    def __init__(self):
        self.proteico = None
        self.vegetales = []
        self.tipo_masa = None
        self.es_una_pizza_valida = False

    def pedir(self):
        self.proteico = self._input_validado("Ingresar qué proteína desea. Las posibilidades son: ", proteicos)
        self.vegetales.append(self._input_validado("Ingresar el primer vegetal. Las opciones son: ", vegetales))
        self.vegetales.append(self._input_validado("Ingresar el segundo vegetal. Las opciones son: ", vegetales))
        self.tipo_masa = self._input_validado("Ingresar el tipo de masa. Las opciones son: ", masas)

        self.es_una_pizza_valida = True

    @staticmethod
    def _input_validado(mensaje, opciones):
        while True:
            seleccion = input(mensaje)
            if seleccion.lower() in opciones:
                return seleccion.lower()
            print("Por favor, ingrese una opción válida.")

vegetales = ["tomate", "aceitunas", "champiñones"]
proteicos = ["pollo", "vacuno", "carne vegetal"]
masas = ["tradicional", "delgada"]