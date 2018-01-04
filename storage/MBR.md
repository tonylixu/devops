### Introduction
When you turn on a server, the processor attempts to begin the process of processing data. But, since the system memory is empty, the processor doesn't really have anything to execute, or even begin to know where to look for it. To ensure the server always boot regardless of the BIOS code, both chip and BIOS manufacturers developed their code so that the processor, once turned on, always starts executing at the same place, `FFFF0h`.

Similarly, every hard disk must have a consistent "starting point" where key information is stored about the disk, such as the number of partitions and what type they are. There also must be someplace where the BIOS can load the initial boot program that starts the process of loading the operating system.

Th eplace where this info is stored is called the the MBR (master boot record), also referred to as the master boot sector or the boot sector.

The MBR is always located at cylinder 0, head 0 and sector 1. This starting point is consistent for almost every disks. When a computer boots, it will always look at this sector 1 for instructions and info on how to proceed with the boot process.

### MBR Structures:
* Master Partition Table: A small bit of code that is referred to as a table contains a complete description of the disk partitions. When the developer designed the size of MPT, they only gave enough room for four disks, hence the four partition limit. For this reason, the hard disk may only have 4 true partitions. These 4 partitions are called primary or physical partitions. Any additional parition is logical partition that are linked to one of the primary partitions.
* Master Boot Code: The master boot code is the small bit of computer code that the BIOS loads and executes to start the boot process. When fully executed, it transfers control to the boot program stored on the boot (active) partition to load the OS.


### MBR Record and ASCII
```bash
Entire MBR record in hex and ASCII 
OFFSET 0 1 2 3  4 5 6 7  8 9 A B  C D E F  *0123456789ABCDEF*
000000 fa33c08e d0bc007c 8bf45007 501ffbfc *.3.....|..P.P...*
000010 bf0006b9 0001f2a5 ea1d0600 00bebe07 *................*
000020 b304803c 80740e80 3c00751c 83c610fe *.....t....u.....*
000030 cb75efcd 188b148b 4c028bee 83c610fe *.u......L.......*
000040 cb741a80 3c0074f4 be8b06ac 3c00740b *.t....t.......t.*
000050 56bb0700 b40ecd10 5eebf0eb febf0500 *V.......^.......*
000060 bb007cb8 010257cd 135f730c 33c0cd13 *..|...W.._s.3...*
000070 4f75edbe a306ebd3 bec206bf fe7d813d *Ou...........}.=*
000080 55aa75c7 8bf5ea00 7c000049 6e76616c *U.u.....|..Inval*
000090 69642070 61727469 74696f6e 20746162 *id partition tab*
0000a0 6c650045 72726f72 206c6f61 64696e67 *le.Error loading*
0000b0 206f7065 72617469 6e672073 79737465 * operating syste*
0000c0 6d004d69 7373696e 67206f70 65726174 *m.Missing operat*
0000d0 696e6720 73797374 656d0000 00000000 *ing system......*
0000e0 00000000 00000000 00000000 00000000 *................*
0000f0 TO 0001af SAME AS ABOVE
0001b0 00000000 00000000 00000000 00008001 *................*
0001c0 0100060d fef83e00 00000678 0d000000 *...........x....*
0001d0 00000000 00000000 00000000 00000000 *................*
0001e0 00000000 00000000 00000000 00000000 *................*
0001f0 00000000 00000000 00000000 000055aa *..............U.*
```