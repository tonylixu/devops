#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    pid t pid;
    /* Fork a child process */
    if(pid <= 0) { /* Error occured */
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if(pid == 0) { /* Child process */
        execlp("/bin/ls", "ls", NULL);
    }
    else { /* Parent process */
        /* Parent wil wait for the child to complete */
        wait(NULL);
        printf("Child Complete");
    }
    return 0;
}

