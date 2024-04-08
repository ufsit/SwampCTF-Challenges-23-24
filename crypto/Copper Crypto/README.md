# Copper Crypto


## Solution Rationale


This is a typical coppersmith attack, except we need to account for the padding at the end of the flag.

Typically, when an exponent is small (e=3) is common, we can take the e-th root of c in order to get the plaintext, as it is possible that the exponent is so small that the modules doesn't have an impact on the ciphertext when calculating `c = pow(m,e,n)`

Because the padding function is adding entirely null bytes to the end of the plaintext, it is essentially just left-shifting m.

This means we can essentially guess the unpadded value of c and cube-root until it returns a plaintext.

### Resources

- [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Coppersmith Attack](https://en.wikipedia.org/wiki/Coppersmith_method)
- [Stereotyped Message Attack](https://gsdt.github.io/blog/2018/07/20/stereotyped-message-attack/)
