#include<stdio.h>
int prime[10001];
void SieveOfEratosthenes(int n)
{
    int i,p;
    for( i=0;i<n;i++)
    {
        prime[i]=1;
    }
  
 prime[1]=0;
 for ( i=2*2; i<=n; i += 2)
                prime[i] = 0;
    for ( p=3; p*p<=n; p=p+2)
    {
        if (prime[p] == 1)
        {
            for ( i=p*2; i<=n; i += p)
                prime[i] = 0;
        }
    }
}
void deleter(int i,int j,int m,int n, int a[101][101])
{
	a[i][j]=0;
	if(j && a[i][j-1]==1)
		deleter(i,j-1,m,n,a);
	if(i && a[i-1][j]==1)
		deleter(i-1,j,m,n,a);
	if(j<n && a[i][j+1]==1)
		deleter(i,j+1,m,n,a);
	if(i<m && a[i+1][j]==1)
		deleter(i+1,j,m,n,a);
}
int main()
{
	SieveOfEratosthenes(10001);
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int m,n,a[101][101],count=0;
		scanf("%d",&m);
		scanf("%d",&n);
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				scanf("%d",&a[i][j]);
				a[i][j]=prime[a[i][j]];	
			}
		}
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(a[i][j]==1)
				{
					count++;
					deleter(i,j,m-1,n-1,a);
				}
			}
		}
		printf("%d\n",count);
	}
	return 0;
}
