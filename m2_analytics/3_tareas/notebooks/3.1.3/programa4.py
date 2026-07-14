# ============================================
# programa4.py
# ============================================
# Lic. Ilian Joseph Felipez Vaca
# ============================================

import sys
import imc

def clasificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def main():
    if len(sys.argv) != 3:
        print("Error: Se requieren exactamente 2 argumentos")
        print("Uso: python programa4.py <peso_kg> <altura_m>")
        sys.exit(1)

    try:
        peso = float(sys.argv[1])
        altura = float(sys.argv[2])

        if peso <= 0 or altura <= 0:
            print("Error: Peso y altura deben ser valores positivos")
            sys.exit(1)

        imc_resultado = imc.calc_imc(peso, altura)
        clasificacion = clasificar_imc(imc_resultado)

        print("\t=================================")
        print("\t       CALCULADORA DE IMC")
        print("\t=================================")
        print(f"\tPeso: {peso:.2f} kg")
        print(f"\tAltura: {altura:.2f} m")
        print(f"\tIMC: {imc_resultado:.2f}")
        print(f"\tClasificacion: {clasificacion}")
        print("\t=================================")

    except ValueError:
        print("Error: Los argumentos deben ser numeros")
        print("Uso: python programa4.py <peso_kg> <altura_m>")
        sys.exit(1)

# ========== ENTRY POINT ==========
if __name__ == '__main__':
    main()
