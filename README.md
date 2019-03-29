# bsn
Generate or validate bsn (burger service nummer, dutch social security number)

A bsn (burger service number, dutch social security number) is used in Netherlands to identify a person for governmental organisations. The numbers are subject to an algorhitm.

## Verification algorhitm

mod(sum(Position_of_digit * digit),11) = 0

whereas the first position should be considered as negative

## Example

Consider the following number: 319072356
```
(9 x 3) + (8 x 1) + (7 x 9) + (6 x 0) + (5 x 7) + (4 x 2) + (3 x 3) + (2 x 5) + (-1 x 6) = 154
154 mod 11 = 0
```

## Install bsn

Run from Command Line:

`pip install bsn`

## Initiate the module and create instance

```
import bsn
a = bsn.bsn()
```

### Validate number

```
a.validate_bsn(number)
```

### Generate n numbers

```
a.generate_bsn(n)

```



