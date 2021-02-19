#include <stdio.h>

int rev_num(int num) {
    int x = 0;
    int place = 1;
    while (num) {
        x += (num % 10) * place;
        num /= 10;
        place *= 10;
    }
    return x;
}

int main() {
    int n;
    // scanf("%d", n);
    n = rev_num(100);
    printf("%d", n);
    return 0;
}