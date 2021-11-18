# InvertibleDict
python dictionary with easy conversion of keys to values and vice versa

# Examples

1. Inherits from python dict, so use it like a normal dictionary
```
inv_dict = InvertibleDict({1:1, 2:2, 3:5})
for k, v in inv_dict.items():
    ...
inv_dict.update({4:9})
```

2. Swap the keys and values easily

```
swapped = ~inv_dict
original = ~(~inv_dict)
assert original == inv_dict
```

3. Handles strings and other iterable keys and values appropriately

```
d = InvertibleDict({'abc':1, 'def':2})
e = ~d
print(d, e, ~e == d)
```

`>>> {'abc': 1, 'def': 2} {1: 'abc', 2: 'def'} True`
