// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table 26
const unsigned int N = 26*26;
unsigned int counter = 0 ;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    for (node *n = table[hash(word)] ; n != NULL ; n = n->next){
        if (strcasecmp(word, n->word) == 0)
            return true;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (word[1] != '\0')
        return toupper(word[0]) -'A' + toupper(word[1]) - 'A' ;
    else
        return toupper(word[0]) -'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char word [LENGTH + 1];
    // Open files and determine scaling factor
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not opeמ dictionary.\n");
        return false;
    }
    while (fscanf(input,"%s",word) != EOF){
        node *n = malloc(sizeof(node));
        if (n == NULL){
            printf("memory cannot be allocated");
            return false;
        }
        strcpy(n->word, word);
        n->next = NULL;
        int index = hash(word);
        n->next = table[index];
        table[index] = n ;
        counter ++ ;
        }
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0 ; i < N ; i++){
        node *n = table[i] ;
        while (n != NULL){
            node *nd = n ;
            n = n->next ;
            free(nd);

        }
    }
    return true ;
}
