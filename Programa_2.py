def DPLL(B, I):
    if not B:
        return True, I

    if any(not clausula for clausula in B):
        return False, None

    L = seleccionar_literal(B)

    B_prima = simplificar(B, L)
    I_prima = I.copy()
    I_prima[L] = True
    resultado, I1 = DPLL(B_prima, I_prima)
    if resultado:
        return True, I1

    B_prima = simplificar(B, -L)
    I_prima = I.copy()
    I_prima[L] = False
    return DPLL(B_prima, I_prima)

def seleccionar_literal(B):
    for clausula in B:
        for literal in clausula:
            return min(clausula, key=abs)
    return None

def simplificar(B, L):
    nuevas_clausulas = []
    for clausula in B:
        if L in clausula:
            continue  
        nueva_clausula = [l for l in clausula if l != -L]
        nuevas_clausulas.append(nueva_clausula)
    return nuevas_clausulas

def mostrar_formula(B, mapa_de_literales):
    formula = []
    for clausula in B:
        clausula_formateada = []
        for literal in clausula:
            if literal > 0:
                clausula_formateada.append(mapa_de_literales[literal])
            else:
                clausula_formateada.append(f"¬{mapa_de_literales[-literal]}")
        formula.append(clausula_formateada)
    return formula



B = [[-1, -2], [2, -4], [-1, 4], [-2, 4]]  
I = {}  

mapa_de_literales = {
    1: 'p',
    2: 'q',
    3: 'r',
    4: 's'
}

resultado, asignacion_final = DPLL(B, I)

if resultado:
    print("La fórmula es satisfacible con la asignación:", asignacion_final)
else:
    print("La fórmula es insatisfacible")

print("Forma clausal de la fórmula booleana:", mostrar_formula(B, mapa_de_literales))
