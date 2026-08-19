a = (10 / 5) ** 4 > 15 and (8 + 4) == 12
print(a)

P = 4
Q = 8
print(not(P <= Q / P) and not(P < 5))

A = True
B = False
C = False
print(not(A and not C or B))

print(("Bio" + "ingeniería" + "de" + "la" + "UdeA") == "Bio ingenieria de la UdeA") 

print((10 / 2) * 3)

print(5 + 3 * 8 - 18 / 6)

print((5 + 3) * (8 - 18) / 6)

M = 5
print(M > 5)

x = 2
y = 10
print((x > 3 and x < 2) or (y > 10 or x == 2))

x = 9
y = 5
print(not(x > 9 and x < 1) or (y > 10 or x != 9))
print(not(x > 9 and x < 1) and (y > 10 or x != 9))

P = True
Q = False
R = False
print(not(P or Q) and (not Q or P))
print((P and R) or (Q or R) or (P and not Q))