#include<stdio.h>
#include<string.h>
#include <stdlib.h>
 #include <math.h>
double * alloc_matrix ( int cols , int rows ) { // memoria foglalo fuggveny
    double * matr = ( double *) malloc ( cols * rows * sizeof ( double ));
    if ( matr == 0) {
        printf (" Memory allocation error .\n");
        exit (EXIT_FAILURE);
    }
    return matr ;
}

void read_matrix ( FILE * f, double *m, int cols , int rows ) { // matrix elemeit beolvaso fuggveny
    for ( int i = 0; i < rows ; i ++) {
        for ( int j = 0; j < cols ; j ++) {
            fscanf (f, "%lf", &m[i * cols + j ]); // egyszeru beolvasas fscanf - fel
        }
    }
}

void write_matrix ( FILE * f, double *m, int cols , int rows ) { // matrix kiirasa
    for ( int i = 0; i < rows ; i ++) {
        for ( int j = 0; j < cols ; j ++) {
            fprintf (f, "%f ", m[i * cols + j]);
        }
        fprintf (f, "\n");
    }
}



double correlation(double mA[], int colsA, int rowsA, double mB[], int colsB, int rowsB,int stepx,int stepy )
{ //I need the first matrix, how many rows and colums there are, the same with the second matrix
// and the stepx and stepy is for the search later, if I just want a single correlaton give them 0
    double x = 0;
    double y = 0;
    double xy = 0;
    double x2 = 0;
    double y2 = 0;
        for (int i =0; i < rowsA; i++)
        {
            for (int j = 0; j < colsA; j++)
            {
                x+= mA[i * colsA + j]; // declaration of the x,y,xy,x^2 and y^2 for later use
                y+= mB[(i+stepy) * colsB + j+stepx]; 
                xy+= mA[i * colsA + j] * mB[(i+stepy) * colsB + j+stepx];
                x2+=pow(mA[i * colsA + j],2);
                y2+=pow(mB[(i+stepy) * colsB + j+stepx],2);
            }
         }  
int size = colsA * rowsA; // the use of it
        double corr = (size *xy - x * y)
            / sqrt((size * x2 - x * x)
                * (size * y2 - y * y));
return corr;
}


void readcatto(FILE*f,double m[])  // reader with headliners
{char str[69]; // i give them how long it can be at max
int vektorindx=0; 
while ( fgets ( str , 69 , f )!= NULL )
 {
 if ( str [0]== '#')  // if it is # then just print it out
 { printf ("%s", str );}
 else if ( strlen ( str ) >1) // if it is just a white space skip it
 { // I break it at the spaces, and read them in. I found this at the website below, and modified it a little to my liking
 char * token = strtok(str, " ");  // https://www.educative.io/answers/splitting-a-string-using-strtok-in-c
   // loop through the string to extract all other tokens
   while( token != NULL ) {
    m[vektorindx]=atof(token);
    vektorindx++;
      token = strtok(NULL, " ");
   }
 }
}
} 


int main(int argc, char const *argv[]) // I give it how many I want and give them
{
    const int rows = atof(argv[3]); // const says that it remains the same
    const int cols = atof(argv[2]); // I first declared it in the wrong order, thats why it is messy
    const int rows2 = atof(argv[6]);
    const int cols2 = atof(argv[5]);
    double *matr = alloc_matrix(cols, rows); // read in the two matrixes
    double *matr2 = alloc_matrix(cols2, rows2);
    FILE *fptr = fopen(argv[1], "r"); // the two files
    FILE  *dptr= fopen(argv[4],"r");
   read_matrix(fptr, matr, cols, rows); // normal read in
   read_matrix(dptr, matr2, cols2, rows2); // normal read in
    readcatto(fptr, matr); // read in if it has a headline

   
    
    if (rows < 20 && cols < 20)
    {
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                printf("%d ", (int)matr[i * cols + j]);
            }
         
            printf("\n");
        }
    }
    else
    {
        printf("The matrix is too big to make sense to write it out. \n\n");
    }
    
    printf("\n\n");
    readcatto(dptr, matr2); 
    if (rows2 < 20 && cols2 < 20)
    {
        for (int i = 0; i < rows2; i++)
        {
            for (int j = 0; j < cols2; j++)
            {
                printf("%d ", (int)matr2[i * cols2 + j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("The  matrix is too big to make sense to write it out. \n\n");
    }
    
    
    fclose(dptr);
    fclose(fptr);
    double c; // this will be the correlation result 
    int step=5;  // this is the steps i will take 
    int catto; // y coordinate( I hope, to be honest I am not sure)
    int catto2; // x coordinate 
    double v;
    double w=0;
for (int i = 0; i < cols2-cols; i+=step)
{
    for (int  j = 0; j < rows2-rows; j+=step) 
    {
        c= correlation(matr,cols,rows,matr2,cols2,rows2,i,j);
       if (c>0.4)
       {
        if(c>w)
        {
        catto=i;
        catto2=j;
        w=c;
       }
       }
       
       
    }
}
        double my_best_so_far=0; // declare it beforehand
        int x3=0;
        int y3=0;
for (int i = 0; i <10; i++)
{
    for (int  j = 0; j < 10; j++)
    {

        v= correlation(matr,cols,rows,matr2,cols2,rows2,catto-5+i,j+catto2-5);
        if (v>my_best_so_far) // if its bigger than the previous biggest, then make it the new biggest
        {
            my_best_so_far=v; 
            x3=j+catto2-5; // also save its coordinates
            y3=i-5+catto;
        }
        

    }
}
printf("\nCome here my first cat, here you are! with the correlation of%fat the x coordinate of %d and the y coordinate of%d",my_best_so_far,y3,x3);
    return 0;
}
