## Process vs Thread

### General
A process is a program in execution with an assoicated context, address space, and thread of execution (stacks pointer, register, program counter). A process can also have multiple threads. Threads can be viewed as processes with the key difference that they share the same address space.

You can view a process as one thread with one address space. Creating a multiple-threaded process comes with advantages as thrads are cheaper to create and to context switch. Also communications between threads are more simple, as they can access the same memory space. 

One example is a "Chrome" process, you have "Chrome" process running, but inside this "Chrome" process, you can open tabs, set bookmarks and do other things with thread.

### Thread
The basic idea behind threading is very simple: just as the computer can run more than one process at a time, so too can our process run more than one thread at a time. When a running process wants to do something in the background, it launches a new thread. The main thread continues to run in the foreground.

So what's the difference betwen launching a new process and a new thread? A new process is completely independent: one process cannot affect or corrupt one anohter. This also gives you some less flexibility in data flow, it is not easy to flow data from one process to anohter compare to thread. This is becuase multiple threads in a process share data. 

