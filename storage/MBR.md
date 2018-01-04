### Introduction
When you turn on a server, the processor attempts to begin the process of processing data. But, since the system memory is empty, the processor doesn't really have anything to execute, or even begin to know where to look for it. To ensure the server always boot regardless of the BIOS code, both chip and BIOS manufacturers developed their code so that the processor, once turned on, always starts executing at the same place, `FFFF0h`.

Similarly, every hard disk must have a consistent "starting point" where key information is stored about the disk, such as the number of partitions and what type they are. There also must be someplace where the BIOS can load the initial boot program that starts the process of loading the operating system.

Th eplace where this info is stored is called the the MBR (master boot record), also referred to as the master boot sector or the boot sector.

The MBR is always located at cylinder 0, head 0 and sector 1. This starting point is consistent for almost every disks. When a computer boots, it will always look at this sector 1 for instructions and info on how to proceed with the boot process.

### MBR Structures:
* Master Partition Table: A small bit of code that is referred to as a table contains a complete description of the disk partitions. When the developer designed the size of MPT, they only gave enough room for four disks, hence the four partition limit. For this reason, the hard disk may only have 4 true partitions. These 4 partitions are called primary or physical partitions. Any additional parition is logical partition that are linked to one of the primary partitions.
* Master Boot Code: The master boot code is the small bit of computer code that the BIOS loads and executes to start the boot process. When fully executed, it transfers control to the boot program stored on the boot (active) partition to load the OS.