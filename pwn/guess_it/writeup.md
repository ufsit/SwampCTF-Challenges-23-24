The "Guess It" challenge gives quite the bit of free room to modify the stack at will, with the problem
being the stack canary in the way with no obvious way to leak it from within the function.

However, due to the way that GCC creates stack canaries, their value is shared across all functions in
the program. The most straightforward way to solve the challenge was to leak the canary from the
"verify" function with the format string vulnerability and then use it in your payload for the main function.
