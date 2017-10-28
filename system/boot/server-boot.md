## What happens during the boot process from the moment you turn on the machine until you get a login prompt? 
There are 6 high level statges of a typical Lnux boot process.
* BIOS: BIOS stands for "Basic Input/Output System", it performs some system integrity checks first, then it will search, load and execute the boot loader program. It looks for boot loader in floppy, cd-rom and hard drive. You can change the boot sequence even. Once the boot loader is located, it will be loaded into memory, then BIOS passes the control to boot loader.
* MBR: MBR stands for "Master Boot Record". It is located in the first sector of bootable disk. In Liux env, its tupically /dev/hda or /dev/sda. MBR is <= 512 Bytes and contians three components:
  * primary boot load info, usually 446 bytes
  * partition table in next 64 bytes
  * mbr validation check in last 2 bytes
The "GRUB" boot loader or "LILO" also conained in MBR, at this point, the MBR will pass the process to GRUB.
* GRUB: Stands for "Grand Unified Bootloader". GRUB displays a splsh screnn with choices of which kernel image you want to boot from. It will wait few seconds, if no choice given it will load the default one. The GRUB configuration file is located at /boot/grub. GRUB boots kernel then pass the access to kernel.
* Kernel: kernel will perform the following steps:
  * Mounts the root fs
  * Execute the /sbin/init program
Then process will be passed to Init.
* Init: init will look at the /etc/inittab file to decide the Linux runlevel. A typical runlevel explanation:
  * 0 - halt
  * 1 - Single user mode
  * 2 - Multiuser without NFS
  * 3 - Full multiuser mode
  * 4 - unused
  * 5 - X11
  * 6 - reboot
Once runlevel is identified, init will load all the appropriate program.
* Runlevel: When Linux system is booting, you can see various services getting started. Depends on the runlevel, the system will execute the programs from one of the following directories:
  * runlevel # - /etc/rc.d/rc#.d/