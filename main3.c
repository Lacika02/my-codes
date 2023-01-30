#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>


double *alloc_matrix(int N)
{ // memoria foglalo fuggveny
    double *matr = (double *)malloc(N * N * sizeof(double));
    if (matr == 0)
    {
        printf(" Memory allocation error .\n");
        exit(EXIT_FAILURE);
    }
    return matr;
}
void read_matrix(FILE *f, double *m, int N)
{ // matrix elemeit beolvaso fuggveny
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            fscanf(f, "%lf", &m[i * N + j]); // egyszeru beolvasas fscanf - fel
        }
    }
}
void read_vector(FILE *d,double *v, int N)
{
     for(int i=0;i<N; i++)
    {
        fscanf(d,"%lf ",&v[i]);
    }
}
void printArray(double *v, int N)
{
    for (int i = 0; i < N; ++i)
    {
        printf("%f  ", v[i]);
        printf("\n");
    }
}
void writematrix(double *matr,int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%lf ", (double)matr[i * N + j]);
        }

        printf("\n");
    }
}
void Gauss(double matr[],double v[], int N)
{
for(int i = 0; i < N; i++)
{
    double Ratio=matr[i*N+i];
    v[i]=v[i]/Ratio;
    for(int j=0;j<N;j++)
    {
        matr[i*N+j]=matr[i*N+j]/Ratio; 
    }
    for(int j=0; j<N;j++){
        if(j!=i){
            double Ratio2=(matr[j*N+i]/matr[i*N+i]);
            for(int k = i; k < N;k++){
                matr[j*N+k]-=Ratio2*matr[i*N+k];       
               }       
               v[j]-=Ratio2*v[i];
            }
        } 
    } 
 printf("my b vector is :\n");
   printArray(v,N);
}
void pivoting(double matr[],double v[],int N)  /*https://www.bragitoff.com/2018/02/gauss-elimination-c-program/*/
{
printf("\n");
writematrix(matr,N);
printf("\n");
printArray(v,N);
printf("\n");
for ( int i = 0; i < N; i++)
{ 
    double biggest=0;
    for ( int j = i; j < N; j++)
    { 
        if (abs(matr[i*N+i])<0.00000001)
            {
            printf("\nin this column I have a very little number%f\n%d\n%d\n",matr[i*N+j],i+1,j+1);
            if (abs(matr[j*N+i])>abs(biggest))
                {
                    biggest=matr[j*N+i];
                }
            }
        if(abs(matr[j*N+i])>abs(matr[i*N+i]))
            
        {double temp2;
        temp2=v[i];
        v[i]=v[j];
        v[j]=temp2;
            for (int  k = 0; k < N; k++)
            {
                double temp;
                temp=matr[i*N+k];
                matr[i*N+k]=matr[j*N+k];
                matr[j*N+k]=temp;
            }  
        }
    } if(abs(matr[i*N+i])<0.00000001)
    {
      printf("my biggest pivot element is:%f\n ",biggest);
    }
   double Ratio1=matr[i*N+i];
   v[i]=v[i]/Ratio1;
    for ( int q = 0; q< N; q++)
    {
        matr[i*N+q]=matr[i*N+q]/Ratio1;
    }
    for ( int w = 0; w < N; w++)
        {if(w!=i)
            {
                double Ratio2=matr[w*N+i];
                for ( int r = i; r < N; r++)
            {
                matr[w*N+r]-=Ratio2*matr[i*N+r];
               
            }
             v[w]-=Ratio2*v[i];
        }
   }
}
printf("\n");
writematrix(matr,N);
printf("\n");
printArray(v,N);
printf("\n");
}
int main(int argc, char const *argv[])

{
    FILE *f = fopen(argv[1], "r");
    FILE *f2 = fopen(argv[1], "r");
    FILE *f3 = fopen(argv[1], "r");
    FILE *d = fopen(argv[2], "r");
    FILE *d2 = fopen(argv[2], "r");
    FILE *d3 = fopen(argv[2], "r");
    const int N = atof(argv[3]);
    double *matr = alloc_matrix(N);
    double *v = (double *)malloc(N * sizeof(double));
    double * matr2=alloc_matrix(N);
    double *v2 = (double *)malloc(N * sizeof(double));
    double * matr3=alloc_matrix(N);
    double *v3 = (double *)malloc(N * sizeof(double));
    read_matrix(f, matr, N); // I wanna see  what am I working with
    read_matrix(f2,matr2,N);
    read_matrix(f3,matr3,N);
    printf("\nmy matrix looks like this: \n");
    writematrix(matr,N);
    read_vector(d,v,N);
    read_vector(d2,v2,N);
    read_vector(d3,v3,N);
    printf("\nmy vector looks like this:\n");
    printArray(v,N);
    Gauss(matr, v, N);
    pivoting(matr2,v2,N);
    
}
