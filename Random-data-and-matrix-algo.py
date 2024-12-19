import random
import tracking_usage as tu

n = 10
# — Soit T un tableau trie. Ecrire la fonction rechercheDicho qui effectue une recherche dichotomique de la valeur x dans le tableau T, elle retourne 1 si x se trouve dans T et 0 sinon.
# — Evaluer et comparer les complexites des deux fonction de recherches en comparant leurs
# courbes pratiques et leurs complexites theoriques.
# — Ecrire une fonction genererMat qui permet de generer aleatoirement une matrice de(n×m)
# entre 0 et k, 0 ≤ M[i][j] ≤ k.
# — Ecrire la fonction de multiplication de matrices et etudier sa complexite.
# — Etudier la complexit´e de la fonction puissanceMat qui calcul la n eme puissance d’une matrice.

# — En utilisant la fonction rand , ecrire une fonction genererTab qui permet de generer aleatoirement un tableau de n entiers compris entre 0 et k, 0 ≤ T[i] ≤ k.
def genererTab(n, k):
    return [random.randint(0, k) for _ in range(n)]


# — Ecrire la fonction rechercheSeq qui effectue une recherche sequentielle de la valeur x dans le tableau T, elle retourne 1 si x se trouve dans T et 0 sinon.
def rechercheSeq(T, x):
    for element in T:
        if element == x:
            return 1
    return 0

# — Ecrire la fonction Trier qui permet de trier le tableau T.
def trier(T):
    return sorted(T)

# Soit T un tableau trie. Ecrire la fonction rechercheDicho qui effectue une recherche dichotomique de la valeur x dans le tableau T, 
# elle retourne 1 si x se trouve dans T et 0 sinon.

#IL FAUT QUE T SOIT TRIE
def rechercheDichoRec(T, x, left=0, right=None):
    if right is None:
        right = len(T) - 1
    if left > right:
        return 0
    mid = (left + right) // 2
    if T[mid] == x:
        return 1
    elif T[mid] < x:
        return rechercheDichoRec(T, x, mid + 1, right)
    else:
        return rechercheDichoRec(T, x, left, mid - 1)
    
    
def compare_search_complexities(T, TT, n=10):
    with open("complexity.csv", "w") as a:
        a.write("VALUE, SEQ, DICHO\n")
        for i in range(100000):
            track1 = sum(tu.track_time(lambda: rechercheDichoRec(TT, i)) for _ in range(n)) / n
            track2 = sum(tu.track_time(lambda: rechercheSeq(T, i)) for _ in range(n)) / n
            a.write(f"{i}, {track2:.5f}, {track1:.5f}\n")

# =================================================================================

def genererMat(n, m, k):
    return [[random.randint(0, k) for _ in range(m)] for _ in range(n)]


def multiplicationMat(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

def compare_multiplication_complexities():
    with open("complexityMul.csv", "w") as a:
        a.write("SIZE, TIME\n")
        for i in range(5, 500):
            A = genererMat(i, i, 30)
            B = genererMat(i, i, 30)
            temps = sum(tu.track_time(lambda: multiplicationMat(A, B)) for _ in range(n)) / n
            a.write(f"{i}x{i}, {temps:.10f}\n")

# =================================================================================

def puissanceMat(M, n):

    result = [[1 if i == j else 0 for j in range(len(M))] for i in range(len(M))]
    base = M

    while n > 0:
        if n % 2 == 1:
            result = multiplicationMat(result, base)
        base = multiplicationMat(base, base)
        n //= 2

    return result

A = genererMat(15, 15, 30)
with open("complexityPow.csv", "w") as a:
    a.write("POWER, TIME\n")
    for i in range(5, 100):
        temps = sum(tu.track_time(lambda: puissanceMat(A, i)) for _ in range(n)) / n
        a.write(f"^{i}, {temps:.10f}\n")



