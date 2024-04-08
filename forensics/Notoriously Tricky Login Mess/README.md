# Notoriously Tricky Login Mess

This was a challenge that had ntlmv2 authenticitation packets in a pcap.
The challenge name was supposed to be a hint to NTLM.

## Part 1

For this, we simply need to find the username for the unprivileged account. If we filter for `ntlmssp` in wireshark, the only users we see are `Administrator` and `adamkadaban`


## Part 2

For this, we also need to filter by `ntlmssp` packets. The goal is to manually construct the ntlmv2 hash from the authentication, negotiate, and challenge packets. 

The `adamkadaban` user authenticates several times, so there will be multiple correct hashes.

One of them, however, is:


```
adamkadaban:::1fed9e8e0ca470a3:98ebffae0b77865893846dfadb757cfb:0101000000000000801c50dbc266da0188d48d08eff230a80000000002001e0045004300320041004d0041005a002d00450033003300530047004c00380001001e0045004300320041004d0041005a002d00450033003300530047004c00380004001e0045004300320041004d0041005a002d00450033003300530047004c00380003001e0045004300320041004d0041005a002d00450033003300530047004c003800070008005783ebd6c266da010000000000000000
```

We can crack this with `hashcat <hash file> /usr/share/wordlists/rockyou.txt`

This gets us a password of `emilyyoudontknowmypassword`
