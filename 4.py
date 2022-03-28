def find(A, B):

    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            C.append(B[j])
            j += 1
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[i])
            C.append(B[j])
            i += 1
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1

    if (len(A) + len(B)) % 2 == 1:
        return C[(len(A) + len(B)) // 2]
    else:
        return (C[(len(A) + len(B)) // 2] +  C[((len(A) + len(B)) // 2) - 1]) / 2.0
if __name__ == '__main__':
    A = [1,2,3]
    B = [2,4,5]
    print(find(A ,B))
