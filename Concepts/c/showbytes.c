#include <stdio.h>
#include <string.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
    for (int i = 0; i < len; ++i) {
        printf("%.2x", start[i]);
    }
    printf("\n");
}

void reverse_show_bytes(byte_pointer start, size_t len) {
    for (int i = len; i > 0; --i) {
        printf("%.2x", start[i]);
    }
    printf("\n");
}

void show_int(int x) {
    printf("Int Repr: ");
    show_bytes((byte_pointer) &x, sizeof(int));
}

void reverse_show_int(int x) {
    printf("Reverse Int: ");
    reverse_show_bytes((byte_pointer) &x, sizeof(int));
}

void show_unsigned_int(unsigned int x) {
    show_bytes((byte_pointer) &x, sizeof(unsigned int));
}

void show_pointer(void *x) {
    printf("Pointer: ");
    show_bytes((byte_pointer) &x, sizeof(void *));
}

void test_show_bytes(int val) {
    int ival = val;
    int *pval = &ival;
    show_int(ival);
    reverse_show_int(ival);
    show_pointer(pval);
    printf("\n");
}

void inplace_swap(int *x, int *y) {
    // No performance improvement over regular swapping
    // Ex: *x = 0000 0001, *y = 0000 0010
    *y = *x ^ *y; // *y = 0000 0011
    *x = *x ^ *y; // *x = 0000 0010
    *y = *x ^ *y; // *y = 0000 0001
}

void two_to_unisgned(int x) {
    // int *px = &x;
    unsigned int ux = (unsigned int) x;
    // unsigned int *pux = &ux;
    show_int(x);
    printf("%d\n", x);
    show_unsigned_int(ux);
    printf("%u\n", ux);
}

int tadd_ok(int x, int y) {
    if (x < 0 && y < 0) {

    }
    return 1;
}

int unroll_sum(const int arr[], int size) {
    int sum = 0;
    if (size % 2 == 0) {
        for (int i = 0; i < size; i+=2) {
            sum += arr[i];
            sum += arr[i+1];
        }
    }
    else {
        sum += arr[0];
        for (int i = 1; i < size; i+=2) {
            sum += arr[i];
            sum += arr[i+1];
        }
    }
    printf("%d", sum);
    return sum;
}

unsigned int floor_div_u(unsigned int x, unsigned int power_of_two) {
    unsigned int result = x >> power_of_two;
    printf("%u\n", result);
    return result;
}

int floor_div_t(int x, unsigned int power_of_two) {
    int result = x >> power_of_two;
    printf("%d\n", result);
    return result;
}

int main() {
    // Two Hex is 1 byte

    // Charrays repr
    //const char *m = "mnopqr";
    //show_bytes((byte_pointer) m, strlen(m)+1); // if add 1 to length the end 00 is printed
    // test_show_bytes(2607352);


    // Big and Little Endian testing
    unsigned int mybyte1 = 0x01234567;
    unsigned int mybyte2 = 0x00245610;
    test_show_bytes(mybyte1);
    test_show_bytes(mybyte2);
    
    
    // Inplace Swap
    /*
    int a = 54;
    int b = 32;
    printf("%d, %d", a,b);
    printf("\n");
    inplace_swap(&a, &b);
    printf("%d, %d", a,b);
    printf("\n");
    */

    /*
    // Two's to Unsigned:
    two_to_unisgned(-1);

    // Unsigned division (Unsigned right shift)
    floor_div_u(22, 3); // 22/2/2/2 == 11/2/2 == 5/2 = 2
    // Two's divison by two (Arithmetic right shit)
    floor_div_t(22, 3); // 2
    floor_div_t(-22, 3); // -3 (because rounds down not up)
    */

    // unrolled sum, don't need unrolling in all modern cases due to compiler being good
    // int array_one[10];
    // for (int i = 0; i < 10; ++i) {
    //     array_one[i] = i;
    // }
    // unroll_sum(array_one, 10);

    return 0;
}