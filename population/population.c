#include <stdio.h>
#include <cs50.h>

int main(void)
{
 int s, e, i;

  do
  {
      s = get_int("begining num: ");
  }
  while (s < 9);

  do {

      e = get_int("ending num: ");
  }
  
  while (e < s);

  for (i = 0 ; s < e ; i++)

      s  = s + s / 3 - s / 4;

  printf("Years: %d", i);
}


