#incomplete
#_---------------------------------------------------------------------------------------------------------------------------------------------#
puzzle = [[0 for i in range(9)] for j in range(9)]
probs = [[[] for i in range(9)] for j in range(9)]
F = open("Sudoku_Question.txt",'r')
row = 0
while L != ['']:
    col = 0
    for k in L:
        try:
            puzzle[row][col] = int(k)
        except:
            None
        col += 1
    row += 1
    L = F.readline().rstrip('\n').split(" ")
#-----------------------------------------------------------------------------------------------------------------------------------------------#
def show(P):
    for i in range(9):
        for j in range(9):
            print(P[i][j],end="\t")
        print('\n')
    print("------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------#
def second_row(pr,value,r,c):
    for i in range(1,9):
        if pr[r][(c+i)%9] != []:
            if value in pr[r][(c+i)%9]:
                return 0
    return 1

def second_column(pr,value,r,c):
    for j in range(1,9):    
        if pr[(r+j)%9][c] != []:
            if value in pr[(r+j)%9][c]:
                return 0
    return 1

def second_matrix(pr,value,r,c):
    mod_col = 0
    mod_row = 0
    if c > 5:
        mod_col = 6
    elif c>2:
        mod_col = 3
    if r > 5:
        mod_row = 6
    elif r>2:
        mod_row = 3
    row = [r,(r+1)%3 + mod_row,(r-1)%3 + mod_row ]
    col = [c,(c+1)%3+mod_col,(c-1)%3+mod_col]
    for i in row:
        for j in col:
            if i != r and  j != c:
                if value in pr[i][j]:
                    return 0
    return 1
#----------------------------------------------------------------------------------#
def check_row(P,A,r,c):
    for j in range(1,9):
        if P[r][(c+j)%9] in A:
            A.remove(P[r][(c+j)%9])
    return A

def check_col(P,A,r,c):
    for j in range(1,9):
        if P[(r+j)%9][c] in A:
            A.remove(P[(r+j)%9][c])
    return A

def check_matrix(P,A,r,c):
    mod_col = 0
    mod_row = 0
    if c > 5:
        mod_col = 6
    elif c>2:
        mod_col = 3
    if r > 5:
        mod_row = 6
    elif r>2:
        mod_row = 3
    row = [r,(r+1)%3 + mod_row,(r-1)%3 + mod_row ]
    col = [c,(c+1)%3+mod_col,(c-1)%3+mod_col]
    for i in row:
        for j in col:
            if i != r and  j != c:
                if P[i][j] in A:
                    A.remove(P[i][j])
    return A
#----------------------------------------------------------------------------------------#
def ver(P):
    #ROW&column
    for i in range(9):
        A = [n for n in range(1,10)]
        B = [n for n in range(1,10)]
        for j in range(9):
            if P[i][j] in A:
                A.remove(P[i][j])
            else:
                return 0
            if P[j][i] in B:
                B.remove(P[j][i])
            else:
                return 0
    #matrix
    for r in range(0,3,6):
        A = [n for n in range(1,10)]
        for c in range(0,3,6):
            x = [r+n for n in range(3)]
            y = [r+n for n in range(3)]
            for i in x:
                for j in y:
                    if P[i][j] in A:
                        A.remove(P[i][j])
                    else:
                        print("Grids failed")
                        return 0
    return 1

def zeros(P):
    for i in range(9):
        for j in range(9):
            if P[i][j] == 0:
                return 0
    return 1

def valid_numbers(P,probs):
    progress = 0
    for i in range(9):
        for j in range(9):
            A = [n for n in range(1,10)]
            if P[i][j] == 0:
                val_A = check_matrix(P,(check_col(P,(check_row(P,A,i,j)),i,j)),i,j)
                probs[i][j] = val_A
                if len(val_A) == 1:
                    progress = 1
                    probs[i][j] = []
                    P[i][j] = val_A[0]
    if progress >= 1:
        valid_numbers(P,probs)
    return P

def second_constraints(P,pr): #check for repititions in probs
    for i in range(9):
        for j in range(9):
            L = pr[i][j]
            if L != []:
                for k in L:
                    if second_column(pr,k,i,j) == 0 or second_row(pr,k,i,j) == 0 or second_matrix(pr,k,i,j) == 0:
                        continue
                    pr[i][j] = []
                    P[i][j] = k

valid_numbers(puzzle,probs)
second_constraints(puzzle,probs)
valid_numbers(puzzle,probs)
# show(probs)

multiples = []
def mult(z,m,c):
    m.append(z)
    m.append(z)

    for i in range(9):
        for j in range(9):
            if len(z[i][j]) == c:
                a = z[i][j][1]
                b = z[i][j][0]
                m[0][i][j] = [b]
                m[0][i][j] = [a]
                return m
z = [[ y for y in x] for x in probs]
mult(z,multiples,2)
