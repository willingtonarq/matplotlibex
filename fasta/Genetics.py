
import matplotlib.pyplot as plt

def comparar(seq1, seq2):
    diferencias = []
    diferencias2 = sum(1 for a, b in zip(seq1, seq2) if a != b)

    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            diferencias.append(i)
    return diferencias, diferencias2


def leer_fasta(ruta_archivo):
    with open(ruta_archivo) as f:
        lineas = f.readlines()
    secuencia = ""
    for linea in lineas:
        if not linea.startswith(">"):
            secuencia += linea.strip()
    return secuencia

humano = leer_fasta("fasta/human.fasta")
chimpance = leer_fasta("fasta/chimpance2.fasta")


diferencias, diferencias2 = comparar(humano, chimpance)

longitud = len(humano)
porcentaje_diferente = (diferencias2 / longitud) * 100
porcentaje_igual = 100 - porcentaje_diferente




plt.figure(figsize=(12, 2))
plt.scatter(diferencias, [1]*len(diferencias), color='red', marker='|')
plt.title("Diferencias genéticas entre humano y chimpancé")
plt.xlabel("Posición en la secuencia")
plt.yticks([])
plt.grid(True, axis='x')
plt.show()

