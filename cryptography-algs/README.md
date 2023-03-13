# Cryptography Algorithms

## Caesar Cipher

Rotates the alphabet x times, where x is the "key" of the cipher, so that every letter in the decoded message maps to 
the corresponding letter in the rotated alphabet.

### examples

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
     
Maps to 
     
DEFGHIJKLMNOPQRSTUVWXYZABC
```

you can see that the key would be 3

and then this message can be decoded by  matching the mapped alphabet to the regular alphabet

```text
BRX DUH DZHVRPH
YOU ARE AWESOME
```

And another, with a key of 9
```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
JKLMNOPQRSTUVWXYZABCDEFGHI
```

```text
CXX VJWH BNLANCB
TOO MANY SECRETS
```

### Weakness

Easy to hand crack, since you are only rotating the alphabet, you only have 26 options for keys. So the attacker could just
try decrypting with each key until they get something that makes sense to read.

So this leads to Kerckhoff's principle, Eve should not be able to break the cipher even if cipher is known
So if they know the algorithm, it should not give an advantage in breaking the cipher




## Substitution Cipher

This method is stronger than caesar because the space of keys is 26!
basically any random permutation of the alphabet can be a key.

## Cracking substitution cipher

Using frequency analysis of letters in the target language can be used
to estimate the mappings in a cipher



## Permutations

permutations of 4 items
1 2 3 4

[4] [3] [2] [1] # of options
You have 4 choices for the first item, 3 for the next, 2 for the next and 1 for the last

So 4 * 3 * 2 * 1 choices = 24 total choices

n! = n * (n-1)*...* 2 * 1

this is also factorial, so permutations of n items == factorial
