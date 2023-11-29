#include <stdio.h>
#include <sys/mman.h>

int main(){
    while(1){
        int N = 100*1024*1024;
        int *ptr = mmap(NULL, N*sizeof(int), PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);
        for (int i=0; i<N; i++)
            ptr[i] = 1;
    }
    return 0;
}