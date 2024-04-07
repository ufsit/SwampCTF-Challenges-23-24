The intended solution to the "Scratchpad" challenge was to take advantage of the missing negative bounds
check when selecting which scratchpad to interact with. By selecting a negative index, you were able
to read and write to the GOT table and artificially insert a system call.
