# ============================================
# imc.py
# ============================================
# Lic. Ilian Joseph Felipez Vaca
# ============================================

import sys

def calc_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

def es_numero_valido(valor: str) -> bool:
    try:
        num = float(valor)
        return num > 0
    except ValueError:
        return False

def validar_argumentos():
    if len(sys.argv) != 3:
        print("Error: Se requieren exactamente 2 argumentos")
        print("Uso: python imc.py <peso_kg> <altura_m>")
        print("\t<peso_kg> : Numero positivo (ej: 70.5)")
        print("\t<altura_m> : Numero positivo (ej: 1.75)")
        sys.exit(1)

    peso_str = sys.argv[1]
    altura_str = sys.argv[2]

    if not es_numero_valido(peso_str):
        print(f"Error: '{peso_str}' no es un peso valido")
        print("El peso debe ser un numero positivo (ej: 70, 70.5)")
        sys.exit(1)

    if not es_numero_valido(altura_str):
        print(f"Error: '{altura_str}' no es una altura valida")
        print("La altura debe ser un numero positivo (ej: 1.75, 1.80)")
        sys.exit(1)

    return float(peso_str), float(altura_str)

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    peso, altura = validar_argumentos()
    imc = calc_imc(peso, altura)
    print(f"\tPeso: {peso:.2f} kg")
    print(f"\tAltura: {altura:.2f} m")
    print(f"\tIMC: {imc:.2f}")
