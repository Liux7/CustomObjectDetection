#include<stdlib.h>
#include<stdio.h>
int main()
{
    FILE *fp, *fp2;
    char* s[100];
    fp = fopen("pos.txt","r");
    fp2 = fopen("pos_.txt","w");
    while(fscanf(fp, "%s", s)!=EOF)
    {
        fprintf(fp2,"%s 1 0 0 24 24\n",s);
    }

    fclose(fp);
    fclose(fp2);
}