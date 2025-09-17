import numpy as np

def main():
    my_array = np.arange(10, 70, 2)
    print(my_array)

    A = my_array.reshape(6, 5).T
    print(A)

    A = A * 2.5
    A[0] = A[0] - 5
    print(A)

    B = np.random.uniform(0, 10, (6, 3))
    print(B)

    a = A.sum(1)
    b = B.sum(1)
    print(a.shape, b.shape)

    AxB = A @ B
    print(AxB)

    A = np.delete(A, 2, 1)
    B = np.hstack((B, np.random.uniform(10, 20, (6, 3))))
    print(A,B)
    print(A.shape, B.shape)

    detA = np.linalg.det(A)
    detB = np.linalg.det(B)
    if detA != 0: 
        invA = np.linalg.inv(A)
        print(invA)
    if detB != 0: 
        invB = np.linalg.inv(B)
        print(invB)

    A = np.linalg.matrix_power(A, 6)
    print(A)
    B = np.linalg.matrix_power(B, 14)
    print(B)

    M = np.array([[2, -5, 1, 0], [1, -1, -13, 0], [3, -2, -2, -4], [4, 0, 2.7, -1.3]])
    V = np.array([-4, 2.6, 1, -2])
    S = np.linalg.solve(M, V)
    print("Решение: ", S)

main()
