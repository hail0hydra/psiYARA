#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int main(void){

    //
    //
    // JUST WRITING TO THE PIPE
    //
    //
    mkfifo("myPipe", 0666);
    // int fd;
    // char *myPipe = "myPipe";

    // fd = open(myPipe, O_RDWR);

    // write(fd, "Hello from new.c!\n", 18);

    return 0;

}
