#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg = 0 ;
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++){
            avg = round(((float)image[i][j].rgbtRed +  (float)image[i][j].rgbtGreen + (float)image[i][j].rgbtBlue) /  3) ;

            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
        float red = 0 ;
        float green = 0;
        float blue = 0;

    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++){

            red = 0.393*image[i][j].rgbtRed + 0.769*image[i][j].rgbtGreen + 0.189*image[i][j].rgbtBlue;
            green = 0.349*image[i][j].rgbtRed + 0.686*image[i][j].rgbtGreen + 0.168*image[i][j].rgbtBlue;
            blue = 0.272*image[i][j].rgbtRed + 0.534*image[i][j].rgbtGreen + 0.131*image[i][j].rgbtBlue;

            image[i][j].rgbtRed =(round(red) < 255 ) ? round(red) : 255 ;
            image[i][j].rgbtGreen =(round(green) < 255 ) ? round(green) : 255 ;
            image[i][j].rgbtBlue =(round(blue) < 255 ) ? round(blue) : 255 ;
        }
    return;
}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp ;
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width/2; j++){

            temp.rgbtRed = image[i][j].rgbtRed;
            temp.rgbtGreen = image[i][j].rgbtGreen;
            temp.rgbtBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width -j-1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width -j-1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width -j-1].rgbtBlue;

            image[i][width -j-1].rgbtRed = temp.rgbtRed;
            image[i][width -j-1].rgbtGreen = temp.rgbtGreen;
            image[i][width -j-1].rgbtBlue = temp.rgbtBlue;

        }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy [height][width];

    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            copy[i][j] = image[i][j] ;

    int count = 0 ;
    int red = 0;
    int green = 0;
    int blue = 0;

    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            for (int col = i-1 ; col <= i + 1 ; col++){
                for (int row = j-1; row <= j + 1 ; row++){
                    if ((col >= 0) && (col < height) && (row >= 0) && (row < width)){
                        red += copy[col][row].rgbtRed;
                        green += copy[col][row].rgbtGreen;
                        blue += copy[col][row].rgbtBlue;
                        count++ ;
                    }
                }
            }

            image[i][j].rgbtRed = round((float) red / count);
            image[i][j].rgbtGreen = round((float) green / count);
            image[i][j].rgbtBlue = round((float) blue / count);

            red = 0;
            green = 0;
            blue = 0;
            count = 0;
        }
    }


    return;
}


