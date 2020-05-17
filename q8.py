# LU decomposition


import scipy.linalg
A = scipy.array([[1, 2, 3],
             [4, 5, 6],
             [10, 11, 9]])

P, L, U = scipy.linalg.lu(A)
print("P matrix -")
print(P)
print("\n")
print("L matrix -")
print(L)
print("\n")
print("U matrix -")
print(U)
print("\n")

#to verify

print("After verfying : Matrix A-")
mult = P.dot((L.dot(U)))
print(mult)
