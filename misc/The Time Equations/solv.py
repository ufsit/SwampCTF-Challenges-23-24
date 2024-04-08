import re
import numpy as np
from pwn import *

r = remote('chals.swampctf.com', 60001)

r.recvuntil(b'!!!\n\n')

l1 = r.recvline().decode().rstrip()
l2 = r.recvline().decode().rstrip()
l3 = r.recvline().decode().rstrip()
l4 = r.recvline().decode().rstrip()
l5 = r.recvline().decode().rstrip()

lines = [l1,l2,l3,l4,l5]

coef_list = []
const_list = []

for l in lines:
    result = re.search(r'(\d+)\*a \+ (\d+)\*b \+ (\d+)\*c \+ (\d+)\*d \+ (\d+)\*e = (\d+)', l)

    nums = list(map(int, result.groups()))
    const = nums.pop(-1)
    coef_list.append(nums)
    const_list.append(const)

coefficients = np.array(coef_list)
constants = np.array(const_list)

solution = np.linalg.solve(coefficients, constants)

for i in range(5):
    r.sendline(str(round(solution[i])))

r.interactive()
