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
    
    
T = genererTab(1000000,1000000)

TT = trier(T)

# print(tu.track_time(lambda: rechercheDichoRec(TT, 100)))
# print(tu.track_time(lambda: rechercheSeq(T, 100)))
a = open("complexity.csv", "w")
a.write("VALUE, SEQ, DICHO\n")
for i in range(100000):
    track1 = sum(tu.track_time(lambda: rechercheDichoRec(TT, i)) for _ in range(n)) / n
    track2 = sum(tu.track_time(lambda: rechercheSeq(T, i)) for _ in range(n)) / n
    a.write(f"{i}, {track2:.5f}, {track1:.5f}\n")



