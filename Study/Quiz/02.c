//Q2) 섭씨온도를 화씨온도로 변환하는 프로그램을 작성해 주세요.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	double f;
	int c;
	printf("섭씨 온도를 입력하세요: ");
	scanf("%d", &c);
	f = (9.0 / 5.0 * c) + 32;
	printf("화씨 온도는 %.2lf 입니다", f);
	return 0;
}
