# Código en Python

# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

articulos = [
    [101, "Cuadernos", 10, 20],
    [102, "Lapices", 30, 25],
    [103, "Borradores", 5, 15],
    [104, "Marcadores", 8, 10],
    [105, "Colores", 12, 12]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def main():
    print("LISTA DE PEDIDOS")
    for articulo in articulos:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

        print(f"Artículo: {nombre} (Código: {codigo})")
        print(f"Cantidad a pedir: {cantidad_pedir}")
        print("---------------------------")


if __name__ == "__main__":
    main()
