# Enter your code here
def rotate(m):
    mat = [x[:] for x in m] 
    n = len(m)
    for i in range(int(n/2)):
        for j in range(i,n-i):
            mat[i][j] = m[n-j-1][i]
            mat[n-j-1][i] = m[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = m[j][n-i-1]
            mat[j][n-i-1] = m[i][j]
    return mat
