#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    int cl = count_letters(text);
    int cw = count_words(text);
    int cs = count_sentences(text);

    float L = (float)cl / cw * 100 ;
    float S = (float)cs / cw * 100 ;

    int index = round((0.0588 * L) - (0.296 * S) - 15.8) ;

    if (index <= 1)
        printf("Before Grade 1\n");

    else if (index >= 16)
        printf("Grade 16+\n");

    else
        printf("Grade %d\n", index);

return 0 ;
}

int count_letters(string text){
    int count = 0 ;

    for(int i= 0; i < strlen(text); i++)
        if isalpha(text[i])
            count++ ;

    return count;
}

int count_words(string text){

    int count = 0 ;

    for(int i= 0; i < strlen(text); i++)
        if isspace(text[i])
            count++ ;

    count++;

    return count ;
}

int count_sentences(string text){

    int count = 0;

    for(int i= 0; i < strlen(text); i++)
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            count++ ;

    if (count == 0 && strlen(text) > 0)
        return 1 ;
        
    return count ;
}
