#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    while (1) {
        void* mem = malloc(4096);
        if (mem == NULL) {
            printf("Не удалось выделить память\n");
            break;
        }
        // Заполняем память нулями
        memset(mem, 0, 4096);
        //sleep(1); // Пауза в 1 секунду
        //free(mem); // Освобождаем память
    }
    return 0;
}
