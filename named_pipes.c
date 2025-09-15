#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>



int main(){

    mkfifo("/tmp/named_pipe_1", 0666);
    int fd;
    char *my_pipe = "/tmp/named_pipe_1";

    fd = open(my_pipe, O_RDWR);
    write(fd, "Hello World!\n", 13);

    char buffer[20] = {0};
    read(fd, buffer, 13);
    printf("%s",buffer);

    close(fd);

    return 0;

}
