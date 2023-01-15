
import numpy as np
import galois_example

#Taking the number of rows and columns from user

n=int(input("Enter the number of Rows\n"))
m=int(input("Enter the number of Columns\n"))

"""
 You can either use this loop method for below list comprehension;

a=[]
for i in range(n):
    a.append([0] * m )
"""

#Creating a Empty matrix as as per the instruction of user;

a = [ [0] * m for i in range(n) ]


#Taking the element for a matrix from user;

for i in range (n):
    for j in range(m):
        print("Enter Element No:",i,j)
        a[i][j] = int(input())
a = np.array(a)
print(a)

#Creating a galois field Z_2

GF = galois.GF(2)

m= GF(a)

#Rank of the vector space

Rank = np.linalg.matrix_rank(m)

print(Rank)