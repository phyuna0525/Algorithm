#include <stdio.h>

void av(int a, int b, int c) {
	printf("%d\n", (a + b) % c);
	printf("%d\n", ((a%c)+(b%c))%c);
	printf("%d\n", (a*b)%c);
	printf("%d\n", ((a%c) *(b%c))%c);
}

int main() {
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	av(a, b, c);
}