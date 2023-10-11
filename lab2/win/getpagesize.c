#include <unistd.h>
#include <stdio.h>
 
int main(int argc, char* argv[])
{
        int mempagesize = sysconf(_SC_PAGESIZE);
        printf("размер страницы : %i\n", mempagesize);
        return 0;
}
