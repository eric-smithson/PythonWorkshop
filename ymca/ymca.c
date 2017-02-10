#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define A_SIZE 10

int main(void){
	int i;
	char **a;
	a = (char**)malloc(sizeof(char*) * A_SIZE);
	for(i = 0; i < A_SIZE; i++)
		a[i] = (char*)malloc(sizeof(char) * 4);

	strcpy(a[0], "IT'S");
	strcpy(a[1], "FUN");
	strcpy(a[2], "TO");
	strcpy(a[3], "STAY");
	strcpy(a[4], "AT");
	strcpy(a[5], "THE");
	strcpy(a[6], "YYYY");
	strcpy(a[7], "M");
	strcpy(a[8], "C");
	strcpy(a[9], "A");

	printf("*DA* *DA* *DA* *DA*\n");

	for(int i = 0; i < A_SIZE; i++){
		printf("%s\n", a[i]);
	}

	for(i = 0; i < A_SIZE; i++){
		free(a[i]);
	}
	free(a);
}

