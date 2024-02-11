#include <cs50.h>
#include <stdio.h>


int main(void)
{ int h = 0;
    do{
        h = get_int("height: ");
    }while (h > 8 || h<1);

for (int i = 1; i<= h ; i++){

    for (int j=0; j< h; j++)
        if (j>=h-i)
            printf("#");
        else
            printf(" ");

    printf ("  ");

    for (int j= 0 ; j< i; j++)
        printf("#");

    printf("\n");
}


}