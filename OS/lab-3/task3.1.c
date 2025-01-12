#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h> // Include this header for wait()

int value = 5;

int main() {
    pid_t pid;

    pid = fork();
    if (pid < 0) {
        fprintf(stderr, "Fork Failed");
        return 1;
    } else if (pid == 0) {
        execlp("/bin/ls", "ls", NULL);
        printf("LINE J");
    } else if (pid > 0) {
        wait(NULL);`
        printf("CHILD complete");
    }
    return 0;

}