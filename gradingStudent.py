def finalMarks(n,initialMarks):
    roundMarks = []
    j = 0
    for i in range(n):
        for k in range(1,11):
            j = initialMarks[i] + k
            if initialMarks[i] < 38:
                roundMarks.append(initialMarks[i])
                break
            elif j%5 == 0:
                if j-initialMarks[i] < 3:
                    roundMarks.append(j)
                    break
                else:
                    roundMarks.append(initialMarks[i])
                    break
    print(roundMarks)


n = int(input('enter number of students::'))
marks = []
for _ in range(n):
    marks.append(int(input('enter marks:')))

finalMarks(n,marks)






