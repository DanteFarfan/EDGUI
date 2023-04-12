def contar_a(frase):
    N_a = 0
    for a in frase:
        if a.lower() in "a":
            N_a += 1

    return N_a

def contar_e(frase):
    N_e = 0
    for e in frase:
        if e.lower() in "e":
            N_e += 1

    return N_e

def contar_i(frase):
    N_i = 0
    for i in frase:
        if i.lower() in "i":
            N_i += 1

    return N_i

def contar_o(frase):
    N_o = 0
    for o in frase:
        if o.lower() in "o":
            N_o += 1

    return N_o

def contar_u(frase):
    N_u = 0
    for u in frase:
        if u.lower() in "u":
            N_u += 1

    return N_u

frase = input("Escriba la frase deseada")
N_a = contar_a(frase)
N_e = contar_e(frase)
N_i = contar_i(frase)
N_o = contar_o(frase)
N_u = contar_u(frase)
print(f"En la frase '{frase}' hay {N_a} a, {N_e} e, {N_i} i, {N_o} o, {N_u} u ")

