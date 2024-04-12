#crypto 
# Description
I found Mr. Slapdash's notes file where he keeps track of his credit cards.

He seems to have written down the CVV numbers in some sort of encoding. Can you crack it?

```
4929 2428 3716 8341   11/27  visa  
5209 2330 7086 6970   02/28  mastercard  
3793 568767 90378     03/28  amex  
6011 3798 6234 9679   07/27  discover  
  
cvv:  
4/1/3 3/2/5 2/2/2  
3/2/3 4/4/1 1/3/2   
1/4/4 4/4/1 4/1/4 1/1/1  
2/3/3 2/2/3 3/1/1  
```

🚩 Flag

- concatenated CVV numbers, no spaces
- `he2024{99...99}` (`99` is just a placeholder, not part of the flag)
# Solution
The first thing was seeing that an amex card does indeed have those uneven set of numbers, so that being out of place is normal and not a lead of any kind.

The amount of numbers in CVVs is also different for amex, which is also the third row in the CVV that is unlike the others. So There must be a correlation between the rows.

Could this be coordinates for how to get a number?

Ok, so let's grab the first row:
4/1/3 3/2/5 2/2/2

And assume that something is a row, something is a group of digits and something else is the position within the group for the number.

1. So row 4, `6011 3798 6234 9679`
2. Group 1 `6011`
3. Digit 3 `1`
Could be the first digit of the CVV for the visa card.

The second digit:
1. Row 3 `3793 568767 90378`
2. Group 2 `568767`
3. Digit 5 `6`
And this is the second digit of the CVV for the visa card. This assumption seems to be going well because the condition of a fifth digit could only happen in the row that corresponds to group 2 or 3 in the amex numbers.

The third digit:
1. Row 2 `5209 2330 7086 6970`
2. Group 2 `2330`
3. Digit 2 `3`
So the first CVV is 163

Working under this assumption leads to the digits:
`1638971914833`
And the flag indeed is `he2024{1638971914833}`
