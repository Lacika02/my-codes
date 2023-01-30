#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include <math.h>
double g(double a0, double a1, double a2, double x1[],double x2[],int step)
{
double ax=a0+(a1*x1[0+step]+(a2*x2[0+step]));
double gx=1/(1+exp(-ax));
return gx;
}
double cost(double a0, double a1, double a2, double x1[],double x2[],int y[],int step)
{
  double money=0;
  double g2=g(a0,a1,a2,x1,x2,step);
  if (y[0+step] == 1 )
{
  money=-log(g2);
}
else if(y[0+step]==0)
{
  money=-log(1-g2);
}
else
{
  printf("Something is wrong, I can feel it.");
}
return money;
}
double allofmymoney(double a0, double a1, double a2, double x1[],double x2[],int y[],int N)
{
  double whatIhavenow;
  for (int i = 0; i < N; i++)
  {
    whatIhavenow+=cost(a0,a1,a2,x1,x2,y,i);
    //printf("%f  %f\n",whatIhavenow,cost(a0,a1,a2,x1,x2,y,i)); 
  }
  return whatIhavenow/N;
}
double grad(double a0,double a1,double a2,double x1[],double x2[],int y[],int N,double x3[])
  {
    double Sum=0;
    for (int i = 0; i < N; i++)
    {
      double minplace=(g(a0,a1,a2,x1,x2,i)-y[i])*x3[i];
      Sum+=minplace;
    }
    return Sum/N ;
  }
  double grad2(double a0,double a1,double a2,double x1[],double x2[],int y[],int N)
  {
    double Sum=0;
    for (int i = 0; i < N; i++)
    {
      double minplace=(g(a0,a1,a2,x1,x2,i)-y[i])*1;
      Sum+=minplace;
    }
    return Sum/N ;
  }
  void gradiens(double x1[], double x2[], int y[],  int N,double alpha)
  {
    double a0,a1,a2;
    a0=-15;
    a1=0.2;
    a2=0.4;
    FILE *f1000=fopen("jgrid1000.dat","w");
    for (int  k = 0; k < 1000; k++)
    {
      a0=a0-(alpha*grad2(a0,a1,a2,x1,x2,y,N));
      a1=a1-(alpha*grad(a0,a1,a2,x1,x2,y,N,x1));
      a2=a2-(alpha*grad(a0,a1,a2,x1,x2,y,N,x2));
      double J=allofmymoney(a0,a1,a2,x1,x2,y,N);
      fprintf(f1000," %d %lf  \n",k,J);
    }
    return;
  }
  void gradiens2(double x1[], double x2[], int y[],  int N,double alpha)
  {
    double a0,a1,a2;
    a0=-15;
    a1=0.2;
    a2=0.4;
    FILE *f10002=fopen("j_alfa0.1grid1000.dat","w");
    for (int  k = 0; k < 1000; k++)
    {
      a0=a0-(alpha*grad2(a0,a1,a2,x1,x2,y,N));
      a1=a1-(alpha*grad(a0,a1,a2,x1,x2,y,N,x1));
      a2=a2-(alpha*grad(a0,a1,a2,x1,x2,y,N,x2));
      double J=allofmymoney(a0,a1,a2,x1,x2,y,N);
      fprintf(f10002," %d %lf  \n",k,J);
    }
    return;
  }
 double avg(double x[],int N)
  {
    double Sum=0;
    double average=0;
    for (int i = 0; i < N; i++)
    {
          Sum+=x[i];
    }
    average=Sum/N;
    return average;
    
  }
 int main(int argc, char const *argv[])
 {
   const char *filename=argv[1];
   const int  N= atof(argv[2]);
   const double alpha=atof(argv[3]);
   FILE *f = fopen(filename ,"r");
    if (f==0)
    {
    printf("Cant open file\n");
    exit(-1);
   }
   double *x1=(double *)malloc(N*sizeof(double));
   double *x2=(double *)malloc(N*sizeof(double));
   int *y=(int *)malloc(N*sizeof(int));
   double *x1_2=(double *)malloc(N*sizeof(double));
  double *x2_2=(double *)malloc(N*sizeof(double));

    for(int i=0;i<N; i++)
    {
        fscanf(f,"%lf ",&x1[i]);
        fscanf(f,"%lf",&x2[i]);
        fscanf(f,"%d",&y[i]);
        //printf("%f %f %d \n",x1[i],x2[i],y[i]); just to test if I was right, and yes I was
    } 
    for (int q = 0; q < N; q++)
{
  x1_2[q]=x1[q]-avg(x1,N);
  x2_2[q]=x2[q]-avg(x2,N);
 // printf("%lf,%lf\n",x1_2[q],x2_2[q]);
}
FILE * fout = fopen ("Jgrid.dat ","w");
FILE * fout2 = fopen ("Jgrid2.dat ","w");
for (int i = 0; i < 50; i++)
{
  for (int j = 0; j < 50; j++)
{
  double a0= -15+0.2*i;
  double a1=0+0.012*j;
 double J= allofmymoney(a0,a1,0,x1,x2,y,N) ;
fprintf ( fout , "%lf %lf %lf\n",a0,a1,J);
}
}
for (int i = 0; i < 50; i++)
{
  for (int j = 0; j < 50; j++)
{
  double a1_2=0+0.012*j;
  double a0_2=0+0.2*i;
 double J2=allofmymoney(a0_2,a1_2,0,x1_2,x2_2,y,N);
fprintf ( fout2 , "%lf %lf %lf\n",a0_2,a1_2,J2);
}
}
printf("my average of my x1 is:%f\n my average of my x2 is:%f\n",avg(x1,N),avg(x2,N));
   fclose ( fout );
   fclose(fout2);
   printf("the propability of success with a0=0.1 a1=0.01 and a2=0.01: %f\n",g(0.1,0.01,0.01,x1,x2,0));
   printf("my cost calculation with a0=0.1 a1=0.01 and a2=0.01: %f\n",cost(0.1,0.01,0.01,x1,x2,y,0));
   printf("my cost function to all of my data with a0=0.1 a1=0.01 and a2=0.01: %f\n",allofmymoney(0.1,0.01,0.01,x1,x2,y,N));
  gradiens(x1,x2,y,N,alpha);
   gradiens2(x1_2,x2_2,y,N,alpha);
    fclose(f);
    return 0;
 }