/*
In this program you can find pascal triangle.The program will take number of rows as input
and then print pascal triangle upto that rows.
*/

#include<stdio.h>
void main ()
{
    int rows;
    printf("enter number of rows:");
    scanf("%d",&rows);
    int a[rows][rows];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (j == 0 || j == i)
            a[i][j] = 1;

            else
            a[i][j] = a[i-1][j-1] + a[i-1][j];
        }
        
    }

    // Now let's print the triangle.
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <=i; j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    
}

/*
OWNER : MR SQUARE
DATE  : 06-06-2022
IF YOU WANT TO LEARN PROGRAMMING LANGUAGES THEN SUBSCRIBE MY CHANNEL "MR SQUARE" ON YOU-TUBE.
*/