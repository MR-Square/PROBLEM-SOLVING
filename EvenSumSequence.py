'''
In this program you can find out the minimum number 
of elements to remove from the sequence such that after
the removal,the sum of every two consecutive elements is even.

You can check more than one sequence at the same time.
'''

no = int(input('How many sequence you want to check::'))

for x in range(no):
    lis = list(map(int,input('inter elements saperated by space::').split()))
    c1 = c2 = 0
    for i in lis:
        if i % 2 !=0:
            c1 = c1+1
        else:
            c2 = c2 +1
    print(min(c1,c2))

'''
OWNER : MR SQUARE
DATE  : 05-06-2022
IF YOU WANT TO LEARN PROGRAMMING LANGUAGES THEN SUBSCRIBE MY CHANNEL "MR SQUARE" ON YOU-TUBE.
'''