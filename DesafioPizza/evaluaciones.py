from pizza import Pizza

# Punto a
print(f"Todas las pizzas tienen un tamaño {Pizza.tamano} y un precio {Pizza.precio}")

# Punto b
print(Pizza.validar_elemento("Salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Punto c
pizza1 = Pizza()
pizza1.pedir()

# Punto d
print(f"Vegetales: {pizza1.vegetales}, Tipo de masa: {pizza1.tipo_masa}, ¿Es una pizza válida?: {pizza1.es_una_pizza_valida}")

# Punto e
print(f"¿Es la clase Pizza una pizza válida?: {Pizza.es_una_pizza_valida}")