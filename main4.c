#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include <time.h>
double Random(double min, double max) 
{
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

int gimmeRandom(int lower, int upper)  //https://www.geeksforgeeks.org/generating-random-number-range-c/
{
        int num = (rand() %(upper - lower + 1)) + lower;
    return num;
}
int Ealfa(int lenght,double cold [])
{
    int sum=0;
        for (int i = 0; i < lenght-1; i++)
            {
                sum+=cold[i]*cold[i+1];
            }
    return (-sum);
}
double hasis(double cold[],int lenght,int n, int KbT,FILE *f)
{
     int E=Ealfa(lenght,cold);
     fprintf(f," %d\n",E);
    for (int i = 0; i < n; i++)
    {
        double *cold2 = (double *)malloc(lenght * sizeof(double));
        for (int q = 0; q < lenght; q++)
        {
            cold2[q]=cold[q];
        }
        
        int randomelem=gimmeRandom(0,lenght); // here I give integer random between the two number
        cold2[randomelem]=-1*cold2[randomelem];
        int E2=Ealfa(lenght,cold2);
        if (E2<E)
        {
            cold[randomelem]=-1*cold[randomelem];
            E=E2;
        }
        int deltaE=E2-E;
        double R=exp(-deltaE/KbT);
        double r;
        r=Random(0,1);  // here the random number is a float type
        //printf("%f\n",r); to see if it is really random.
        if (E2>E)
        {
            if (R>r)
            {
                cold[randomelem]=-1*cold[randomelem];
                E=E2;
            }  
        } 
        fprintf(f," %d\n",E);
 //printf("%d\n",E2);

    } 
}
double iterations(double temperature [],int lenght,int n,int KbT,FILE *f)
{
int E=Ealfa(lenght,temperature);
    for (int i = 0; i < n; i++)
    {
        double *cold2 = (double *)malloc(lenght * sizeof(double));
        for (int q = 0; q < lenght; q++)
        {
            cold2[q]=temperature[q];
        }
        
        int randomelem=gimmeRandom(0,lenght); // here I give integer random between the two number
        cold2[randomelem]=-1*cold2[randomelem];
        int E2=Ealfa(lenght,cold2);
        if (E2<E)
        {
          temperature[randomelem]=-1*temperature[randomelem];
            E=E2;
        }
        int deltaE=E2-E;

        double R=exp(-deltaE/KbT);
        double r;
        r=Random(0,1);  // here the random number is a float type
        //printf("%f\n",r); to see if it is really random.
        if (E2>E)
        {
            if (R>r)
            {
                temperature[randomelem]=-1*temperature[randomelem];
                E=E2;
            }  
        } 
                for (int j = 0; j < lenght; j++)
                {
                    fprintf(f," %d ",(int)temperature[j]);
                   //  printf(" %d ",(int)temperature[j]);
                }
            fprintf(f," \n");
           // printf(" \n");
        
      } 
}
double avgenergy(double cold[],int lenght, int n,double KbT,FILE *f)
{
    for (int j=0; j < 21; j++)
    {
        int E=Ealfa(lenght,cold);
   double Esum=0.0;
    for (int i = 0; i < n; i++)
    {
        double *cold2 = (double *)malloc(lenght * sizeof(double));
        for (int q = 0; q < lenght; q++)
        {
            cold2[q]=cold[q];
        }
        
        int randomelem=gimmeRandom(0,lenght); // here I give integer random between the two number
        cold2[randomelem]=-1*cold2[randomelem];
        int E2=Ealfa(lenght,cold2);
        if (E2<E)
        {
            cold[randomelem]=-1*cold[randomelem];
            E=E2;
        }
        int deltaE=E2-E;
        double R=exp(-deltaE/(KbT+j/5.0));
        double r;
        r=Random(0,1);  // here the random number is a float type
        //printf("%f\n",r); to see if it is really random.
        if (E2>E)
        {
            if (R>r)
            {
                cold[randomelem]=-1*cold[randomelem];
                E=E2;
            }  
        } 
         if (i>500)
        {
        Esum+=E;   
        }  
    } 
    Esum=Esum/7000;
    fprintf(f," %f %f\n",KbT+j/5.0,Esum);
    } 
}
int main(int argc, char const *argv[])
{
    int lenght=atof(argv[1]);
    int n=atof(argv[2]);
    double KbT=atof(argv[3]);
    double *cold = (double *)malloc(lenght * sizeof(double));
    for(int i=0;i<lenght; i++)
        {
            cold[i]=1;
        }
 double *hot = (double *)malloc(lenght * sizeof(double));
for (int i = 0; i < lenght; i++)
{
    double divider=Random(0,1);
    hot[i]=-1;
    if (divider>0.5)
    {
        hot[i]=1;
    } 
}   
hasis(cold,lenght,n,KbT,fopen("file2.dat","w")); 
hasis(hot,lenght,n,KbT,fopen("file4.dat","w"));
iterations(cold,lenght,256,KbT,fopen("file6.dat","w"));
avgenergy(cold,lenght,7500,0.1,fopen("file7.dat","w"));// with this there will be 2000 iterations, and the KbT will be 0,1->4.1
return 0;
}