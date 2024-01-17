#include <stdio.h>
#include <stdlib.h>

int main(){
	int result = system("ping 8.8.8.8 -c 5");
	if (result == 0){
		printf("----------All done!-----------\n");
	} 
	else{
		printf("----------Error!----------\n");
	}
	return 0;
}


