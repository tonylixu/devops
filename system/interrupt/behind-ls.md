### What happens under the hood after typing 'ls'?
First of all, this is an `interrupt` triggerred by the hardware (keyboard).

When CPU is interrupted, it stops what it is doing and immediately transferes execution to a fixed location. Then the interrupt service routine executes. So when you press the first key `l` on your keyboard, the keyboard device driver loads the appropriate registers within the device controller. The device controller then examines the contents of these registers to determine what action to take, in this case, the action is "read the character from the keyboard". Then the controller starts the transfer of data from the keyboard to the local buffer. Once the transfer of data is complete, the device controller informs the device driver via an interrupt that it has finished. Then the device driver returns the control back to CPU.


### References:
First of all, whenever we press a key on keyboard, the keyboard controller will emit an interrupt to processor(CPU) indicating there is an event that needs immediate attention. As interrupts usually have high priority, the processor will suspending its current execution, save its state, and call an interrupt handler(should be the one that handles keyboard interrupt). Suppose we type 'l' then this character will be written the file that fd stdout points to, while shell's stdout usually points to screen (a device, in *nix familiy, everything "looks" like a file), then "l" will be shown on the screen. After the interrupt handler finishes its job, the process will resume its original work.

We type 'ls' and hit enter, then shell will first check out $PATH environment variable to see if there is a program 'ls' under each given path. Suppose we find /usr/bin/ls. Shell will call fork(), followed by execve("/usr/bin/ls"). fork() will create an identical child process and return twice. In parent(shell), it will typically call wait() to wait child process to complete. In child, it will execute execve() and a successful execve() will replace original data(including text, data, heap and stack, etc) in the child process's address space with new data in order to run the new executable. Note that file descriptors opened by parent will be kept(that is why output from ls will be displayed on screen like shell).

Then the child process will be one that runs "/usr/bin/ls" code, it will make system calls(open(2), printf(3c) etc.) to list directory entries in the current working directory. After the child process finishes its job, it will call exit()(usually called implicitly by 'return' in main()). Then all of the fds, streams will be closed. The parent process(in this case the shell) will be notified of child's termination, so wait() will be return and child exit code could be read from wait(). Then parent process(the shell) can proceed, waiting for next command to run.

Follow ups:

What will happen if another interrupt is received while the processor is running interrupt handler code?
* A: Different OS may have different ways to deal with this situation. For linux, task of an interrupt handler is split into two halves, top half and bottom half. Top half runs with interrupts disabled and respond to the interrupt as fast as possible, then bottom half runs with interrupts enabled for as long as it needs and could be preempted.

What do we call a child process when it terminates but its status has not been read by its parent which calls wait()?
* A: Zombie process.

what is value of fd(in most case) will be returned by open() calling in the child process("/usr/bin/ls")?
* A: 3, because stdin, stdout, stderr, will be 0, 1, 2 respectively, and lowest available fd will be returned.

How is parent process notified when its children terminate?
* A: SIGCHLD will be sent to the parent process.

How does shell implement I/O redirection if we want to redirect output of ls to another command as its input? like "ls | sort"
* A: Briefly speaking, shell will call a pipe() before fork() to get two fds, rfd for read end and wfd for write end, then call dup2(wfd, 1) in ls and dup2(rfd, 0) in sort.