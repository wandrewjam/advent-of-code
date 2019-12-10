def permute(k, A) -> list:
    output = list()
    if k == 1:
        output.append(A)
    else:
        for i in range(k):
            output.extend(permute(k - 1, A))
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
    return output


if __name__ == '__main__':
    A = list(range(3))
    k = len(A)
    out = permute(k, A)
    print(len(out))
