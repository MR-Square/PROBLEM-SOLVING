'''
In this program you can find pascal triangle.The program will take number of rows as input
and then print pascal triangle upto that rows.
'''
rows = int(input('enter number of rows:'))
mat = []
for i in range(rows):
    a = []
    for j in range(i+1):
        if j == 0 or j == i:
            a.append(1)
        else:
            a.append(mat[i-1][j-1]+mat[i-1][j])
    mat.append(a)

for i in range(rows):

    for j in range(i+1):
        print(mat[i][j], end = " ")
    print()

'''
OWNER : MR SQUARE
DATE  : 06-06-2022
IF YOU WANT TO LEARN PROGRAMMING LANGUAGES THEN SUBSCRIBE MY CHANNEL "MR SQUARE" ON YOU-TUBE.
'''
