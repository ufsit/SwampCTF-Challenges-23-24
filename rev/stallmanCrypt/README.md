# stallmanCrypt Command Line File Encryptor

Richard Stallman has finally gone off the deep end! He hacked Microsoft and deleted all copies of the Windows 11 source code except for one, but it's encrypted! Can you save it?


# Solution

This challenge worked by creating a new internal state for the ChaCha stream cipher using the rand() function seeded by srand(time()). So once you figure out the time the files were encrypted you could either regenerate ChaCha's internal state and decrypt it using your own ChaCha20 decryptor or substitute the integer returned by time() into 

1. Download the tar.xz file and extract with `tar --atime-preserve -xvf encrypted.tar.xz`
2. Use that `stat` command to view the creation time & dates of each encrypted file
3. Use https://time.is/Unix_time_converter to convert the date times to unix time
4. Use GDB to replace the srand unix time seed right before srand is called

`echo "testdata" > test.txt` - create a dummy file to run the encryption call on

`gdb --args ./stallmanCrypt -re test.txt` - go to encrypt that file

`b* 0x55555555559c` - breakpoint right before the srand call

`set $rax = INT NUM HERE` - right before rax is moved to rdi set it equal to the hex representation of the unix time of the creation of the files

`c` - let the program finish

5. stallmanCrypt will now spit out the hex key used to encrypt the file
6. Use the hex key to decrypt it's associated file


# Example

Encrypting a file with a random key and nonce -
`stallmanCrypt -r -e example.txt`

Decrypting a file - 
`stallmanCrypt -d example.txt.enc -k 6e6f2074686973206973206e6f742074686520666c616720627574206e69636520747279206c6d616f212120476574206f757474612068657265212121203a50`

# Compiling
Compile with your compiler of choice.

`gcc -O3 main.c chacha.c chacha.h hex.c hex.h -o stallmanCrypt`

# Sources
Here are a list of references that I used to guide me along with their accompanying license. I try not to copy paste code.

https://tools.ietf.org/html/rfc8439 - Main reference

The three sources below are "GPL-2.0-or-later"
https://www.oryx-embedded.com/doc/chacha_8c_source.html

https://www.oryx-embedded.com/doc/chacha_8h_source.html

https://www.oryx-embedded.com/doc/cpu__endian_8h_source.html
