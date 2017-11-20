### strace
One of the most useful tools in the sysadmin's arsenal is `strace`, a command that will show you most of the standard library and system calls a program makes while it executes.

To get a taste of it, just fireup a bash shell on your Linux server and type `strace bash`. You might need to install `strace` package if it is not available already.

Examples:
```bash
$ strace pwd
line 1: execve("/bin/pwd", ["pwd"], [/* 21 vars */]) = 0
line 2: brk(0)                                  = 0x21b8000
line 3: access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
line 4: mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x:7f7fa2e7c000
line 5: access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
line 6: open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
line 7: fstat(3, {st_mode=S_IFREG|0644, st_size=39306, ...}) = 0
line 8: mmap(NULL, 39306, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f7fa2e72000
line 9: close(3)                                = 0
line 10: access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
line 11: open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
line 12: read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200\30\2\0\0\0\0\0"..., 832) = 832
line 13: fstat(3, {st_mode=S_IFREG|0755, st_size=1811128, ...}) = 0
line 14: mmap(NULL, 3925176, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f7fa289d000
line 15: mprotect(0x7f7fa2a52000, 2093056, PROT_NONE) = 0
line 16: mmap(0x7f7fa2c51000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b4000) = 0x7f7fa2c51000
line 17: mmap(0x7f7fa2c57000, 17592, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f7fa2c57000
line 18: close(3)                                = 0
line 19: mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f7fa2e71000
line 20: mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f7fa2e70000
line 21: mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f7fa2e6f000
line 22: arch_prctl(ARCH_SET_FS, 0x7f7fa2e70700) = 0
line 23: mprotect(0x7f7fa2c51000, 16384, PROT_READ) = 0
line 24: mprotect(0x606000, 4096, PROT_READ)     = 0
line 25: mprotect(0x7f7fa2e7e000, 4096, PROT_READ) = 0
line 26: munmap(0x7f7fa2e72000, 39306)           = 0
line 27: open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
line 28: fstat(3, {st_mode=S_IFREG|0644, st_size=3165552, ...}) = 0
line 29: mmap(NULL, 3165552, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f7fa2598000
line 30: close(3)                                = 0
line 31: brk(0)                                  = 0x21b8000
line 32: brk(0x21d9000)                          = 0x21d9000
line 33: getcwd("/home/tony", 4096)              = 11
line 34: fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
line 35: mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f7fa2e7b000
line 36: write(1, "/home/tony\n", 11/home/tony)            = 11
line 37: close(1)                                = 0
line 38: munmap(0x7f7fa2e7b000, 4096)            = 0
line 39: close(2)                                = 0
line 40: exit_group(0)                           = ?
```

### Appendix: "strace pwd" output analysis
Holy crap, a simle `pwd` call generated 40 lines of output! Have you ever realized that so much is going on behind the scene? 

Let analysis line by line. You might feel going through each line is very tedious, but trust me, you will need to get a good standing of this if you really want to learn `strace` like a real system enginner :)

`line 1: execve("/bin/pwd", ["pwd"], [/* 21 vars */]) = 0`
This is a Linux system call, the `execve(const char *filename, char *const argv[], char *const envp[])` function executes the program pointed to by filename parameter. In this case, file `/bin/pwd` is executed, with the argument strings contain `pwd` only. We don't have any environment parameters for `envp` array.

`line 2: brk(0)                                  = 0x21b8000`
This `brk(0)` sets the end of data segment to `0x21b8000`

`line 3: access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)`
The `access(const char *path, int amode)` system call determines the accessibility of a file. `F_OK` argurment is the existence test. File `/etc/ld.so.nohwcap` is just a file that when it is present the dynamic linker will load the non-optimized version of a library, ven if the CPU supports the optimized version. 