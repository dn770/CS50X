#include <cs50.h>
#include <stdio.h>

int main(void)
{
int len = 0;
int sum1 = 0;
int dig = 0;
int head = 0 ;
long n = get_long("number: ");

while (n > 1){

   dig = n % 10 ;
   n = n / 10;

   if (len % 2 == 1){
      dig *= 2;

      if (dig >=  10)
         sum1 = sum1 + ( dig / 10 ) + (dig % 10) ;
      else
         sum1 += dig ;
   }
   else
      sum1 += dig;

   len++;

   if (n < 100 && n > 9)
      head = n ;
}

if (sum1 % 10 != 0 || len < 13 || len > 16|| len == 14){
    printf("INVALID\n");
    return 0 ;
}

if (len == 15  && (head == 34 || head == 37) ){

   printf("AMEX\n");
   return 0;
}

if (len == 16 && (head > 50 && head < 56)) {

   printf("MASTERCARD\n");
   return 0;
}

if ((len == 13 || len ==16) && (head /10 == 4 )) {

   printf("VISA\n");
   return 0;
}y

printf("INVALID\n");
return 0;

}