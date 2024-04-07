The issue when it comes to breaking out of the "Old School" binary for this challenge was the lack
of gadgets or linked procedures. The only two instructions that modify rax and take advantage of the
available syscall gadget set it to the constants 1 (read) and 60 (exit).

The only way to make an execve syscall was to take advantage of the fact that the read syscall will
set rax to the number of bytes read. By writing a 59 byte payload, you could set rax to 59 and call
execve.
