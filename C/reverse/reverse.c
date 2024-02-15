#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage - heck command-line arguments
    if (argc != 3)
    {
        printf("Usage: ./volume input.wav output.wav \n");
        return 1;
    }
    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER),1,input);

    if (!check_format(header)){
        printf("Not a wave format.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    // Write header to file
    fwrite(&header, sizeof(WAVHEADER),1,output);

    // Use get_block_size to calculate size of block
    int size = get_block_size(header);


    // Write reversed audio to file
    if(fseek(input, size, SEEK_END))
        return 1;

    BYTE buffer[size];
    while(ftell(input)-size > sizeof(header)){
        if(fseek(input, -2*size, SEEK_CUR)){
            return 1;
        }
        fread(buffer, size, 1, input);
        fwrite(buffer, size, 1, output);
    }

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    if (header.format[0] == 'W' && header.format[1] == 'A' &&header.format[2] == 'V' &&header.format[3] == 'E')
        return 1;
    return 0;
}

int get_block_size(WAVHEADER header)
{
    int size = header.numChannels * header.bitsPerSample / 8;
    return size;
}