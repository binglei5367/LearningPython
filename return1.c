# include <stdio.h>

int main(int argc, char *argv[])
{
	int x = 2;
	printf("x is now %d\n", x);
	printf("incrementing...");
	x = increment(x);
	printf("incremented.");
	printf("x is now %d\n", x);
}

int
increment(int a)
{
	return a + 1;
}