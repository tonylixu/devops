### Process vs Thread
A process is a program in execution with an assoicated context, address space, and thread of execution (stacks pointer, register, program counter). A process can also have multiple threads. Threads can be viewed as processes with the key difference that they share the same address space.

You can view a process as one thread with one address space. Creating a multiple-threaded process comes with advantages as thrads are cheaper to create and to context switch. Also communications between threads are more simple, as they can access the same memory space. 

One example is a "Chrome" process, you have "Chrome" process running, but inside this "Chrome" process, you can open tabs, set bookmarks and do other things with thread.