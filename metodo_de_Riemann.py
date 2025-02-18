from math import *

# Dariangel Tovar
# C.I: 30.277.316

def f(t):
    return (t - 2)**2 + 1  # Función de ejemplo

def metodo_riemann(f, a, b, n):
    print("\nMétodo de Riemann\n")
    print("|\ti\t||\txi\t||\tf(xi)\t||\tÁrea\t|")
    delta_x = (b - a) / n  # Ancho de cada rectángulo
    area_total = 0.0
    for i in range(n):
        xi = a + i * delta_x  # Punto izquierdo del rectángulo
        f_xi = f(xi)          # Altura del rectángulo
        area_rectangulo = f_xi * delta_x  # Área del rectángulo
        area_total += area_rectangulo     # Sumar al área total
        print(f"|\t{i}\t||\t{xi:.4f}\t||\t{f_xi:.4f}\t||\t{area_rectangulo:.4f}\t|")
    return area_total


if __name__ == '__main__':
    a = 2  # Límite inferior
    b = 3  # Límite superior
    n = 5  # Número de rectángulos
    area = metodo_riemann(f, a, b, n)
    print(f"\nÁrea total aproximada: {area:.4f}")
    print('Fin')