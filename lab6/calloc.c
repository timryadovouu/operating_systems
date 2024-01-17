#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    char *memory = NULL;

    for (int i = 0; i <= 2000   ; i += 128){
        clock_t start = clock();
        for (int j = 0; j <= 1000; ++j){
            memory = calloc(1024*1024*i, sizeof(char));
            free(memory);
        }
        clock_t end = clock();
        printf("%d mb in %f seconds\n", i, ((double)(end - start) / CLOCKS_PER_SEC));
    }
    return 0;
}
