from sympy import prime
p, q = prime(50), prime(54) # Waehle zwei grosse Primzahlen
n = p * q
p, q, n
print("Erste gewaehlte Primzahl p: " + str(p))
print("Zweite gewaehlte Primzahl q: " + str(q))
print("n = p * q = " + str(n))

from sympy import factorint
phi = (p-1)*(q-1)  
print("phi(n) = (p-1)*(q-1) = " + str(phi))
print("Die Primfaktorzerlegung von phi ist: " )
print(factorint(phi))
e = 7 * 11 * 13  # Irgendeine Zahl e, die teilerfremd zu phi(n) ist
print("Suche irgendeine Zahl e welche teilerfremd zu phi ist: ")
print("Die folgende Zahl besteht aus Primfaktoren, die nicht in phi vorkommen")
print("e = 7 * 11 * 13 = "+ str(e))
print("Die Zahl phi kann also nicht durch e ohne Rest geteilt werden, wenn e gewaeht wird zu " + str(e))
print("Oeffentlicher Schluessel:  n = " + str(n) + " und e = " + str(e))

print("Suche eine Zahl d, so dass e * d dividiert durch phi den Rest = 1  ergibt")
print("das heisst e * d = 1 (mod phi)")

from sympy import mod_inverse

d = mod_inverse(e, phi)

print("d = 16001 erfuellt die Bedingung insofern als dass ")
print("das Produkt (1001 * 16001) ganzzahlig geteilt mit phi mit dem Wert 57000 ein Resultat ")
print("mit dem Rest 1 ergibt, naemlich 281 Rest 1 ")

print("Privater Schluessel:  d = " + str(d))

N= 51234
print("Nachricht sei N = " + str(N))
print("verschickt wird die verschluesselte Zahl S = N^e mod n")

crypt = lambda M, k: M ** k % n
S= crypt(N, e)
print("Verschluesselte Nachricht:  S = " + str(S))

print("Entschluesselte Zahl X wird mit der  Funktion X = S^d mod n berechnet")
print("d.h. es wird die gleiche Funktion genommen, aber es werden die Argumente S und d in die Funkion eingesetzt.")
X = crypt(S,d)

print("Entschluesselte Nachricht:  X = " + str(X))

print("Da  X und N identisch sind, wurde der Empfaenger identifiziert ")



