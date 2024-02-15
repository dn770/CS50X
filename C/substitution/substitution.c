#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2){
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    string key = argv[1];

    if (strlen(key) != 26){
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0; i < 26 ; i++){
        if(!isalpha(key[i])){
            printf("Error: invalid key\n");
            return 1;
        }
        if (islower(key[i]))
            key[i] = toupper(key[i]);
    }

         for (int i = 0; i < strlen(key)-1; i++)
            for( int j = i+1; j < strlen(key); j++ )
            if (key[i] == key[j]) {
            printf("Error: invalid key\n");
            return 1;
        }

    string text = get_string("plaintext: ");

    for (int i =0; i< strlen(text); i++){

        if (isupper(text[i]))
            text[i] = key[(int)text[i]-65];

        else if (islower(text[i])){
            text[i] = key[(int)text[i]-97];
            text[i] = tolower(text[i]);
        }
    }
    printf("ciphertext: %s\n", text);
    return 0 ;
}