# Bit manipulation

### **Bit Manipulation Summary**

Bit manipulation involves directly working with binary representations of numbers to perform operations like shifting, flipping, and masking. It's a highly efficient way to solve problems related to integers, such as checking even/odd numbers, finding unique elements, or performing arithmetic efficiently.

---

### **Key Operations in Bit Manipulation**

#### 1. **Bitwise Operators in Python**
| **Operator** | **Symbol** | **Example**        | **Explanation**                                          |
|--------------|------------|--------------------|----------------------------------------------------------|
| AND          | `&`        | `a & b`           | Sets a bit to 1 if both corresponding bits are 1.         |
| OR           | `|`        | `a | b`           | Sets a bit to 1 if either of the corresponding bits is 1. |
| XOR          | `^`        | `a ^ b`           | Sets a bit to 1 if the corresponding bits are different.  |
| NOT          | `~`        | `~a`              | Flips all the bits (1 becomes 0, and vice versa).         |
| Left Shift   | `<<`       | `a << n`          | Shifts bits to the left by `n`, equivalent to `a * 2^n`.  |
| Right Shift  | `>>`       | `a >> n`          | Shifts bits to the right by `n`, equivalent to `a // 2^n`.|

---

### **Common Bit Manipulation Techniques**

#### 1. **Check if a Number is Odd or Even**
- **Odd**: The least significant bit (LSB) is 1.
- **Even**: The LSB is 0.

**Python Code**:
```python
def is_odd(n):
    return n & 1 == 1

print(is_odd(5))  # True
print(is_odd(4))  # False
```

---

#### 2. **Get or Set a Specific Bit**

- **Get a Bit**: Check if a specific bit is 1.
  ```python
  def get_bit(num, i):
      return (num >> i) & 1

  print(get_bit(5, 0))  # 1 (LSB of 5 is set)
  print(get_bit(5, 1))  # 0
  ```

- **Set a Bit**: Make a specific bit 1.
  ```python
  def set_bit(num, i):
      return num | (1 << i)

  print(set_bit(5, 1))  # 7 (5 becomes 7 when bit 1 is set)
  ```

---

#### 3. **Clear a Specific Bit**
Make a specific bit 0, regardless of its initial value.
```python
def clear_bit(num, i):
    return num & ~(1 << i)

print(clear_bit(5, 0))  # 4 (5 becomes 4 when bit 0 is cleared)
```

---

#### 4. **Toggle a Specific Bit**
Flip the value of a specific bit (1 becomes 0, and 0 becomes 1).
```python
def toggle_bit(num, i):
    return num ^ (1 << i)

print(toggle_bit(5, 0))  # 4
print(toggle_bit(5, 1))  # 7
```

---

#### 5. **Count the Number of 1s in a Binary Representation**
(Hamming Weight or Population Count)
```python
def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

print(count_ones(5))  # 2 (binary 101 has 2 ones)
```

Alternatively, use Python's built-in:
```python
print(bin(5).count('1'))  # 2
```

---

#### 6. **Find the Only Non-Duplicated Number**
In a list where every number appears twice except one, find the unique number using XOR:
```python
def find_unique(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(find_unique([4, 3, 2, 4, 3]))  # 2
```

**Explanation**:
- XOR of a number with itself is 0 (`x ^ x = 0`).
- XOR of a number with 0 is itself (`x ^ 0 = x`).

---

#### 7. **Check if a Number is a Power of Two**
A number is a power of two if it has exactly one bit set (e.g., `1`, `10`, `100`).

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(4))  # True
print(is_power_of_two(6))  # False
```

---

#### 8. **Reverse the Bits of a Number**
```python
def reverse_bits(num, bit_length=32):
    result = 0
    for i in range(bit_length):
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

print(reverse_bits(5, 3))  # 5 (binary 101 becomes binary 101)
```

---

#### 9. **Find the Most Significant Bit (MSB)**
```python
def most_significant_bit(n):
    msb = 0
    while n > 1:
        n >>= 1
        msb += 1
    return 1 << msb

print(most_significant_bit(10))  # 8
```

---

### **Python-Specific Bitwise Functionality**

1. **`bin(x)`**: Converts an integer to its binary representation as a string.
   ```python
   print(bin(5))  # '0b101'
   ```

2. **`int(x, base)`**: Converts a binary string back to an integer.
   ```python
   print(int('101', 2))  # 5
   ```

3. **Bit Length**:
   ```python
   print((5).bit_length())  # 3 (binary 101 has 3 bits)
   ```

4. **Right-Aligned Binary String**:
   ```python
   print(format(5, 'b'))  # '101'
   print(format(5, '08b'))  # '00000101' (8 bits)
   ```

5. **Integer to Binary Representation with Padding**:
   ```python
   print(f"{5:08b}")  # '00000101'
   ```

---

### **Applications of Bit Manipulation**

1. **Optimization**: Used in low-level programming for performance-critical code (e.g., toggling hardware registers).
2. **Cryptography**: Operations like XOR are used in encryption algorithms.
3. **Competitive Programming**: Problems like subset generation, toggling switches, or finding unique elements.
4. **Graphics**: Bitfields are used in color manipulation and encoding metadata.

By mastering these techniques, you'll be prepared to tackle problems that require efficient computation and manipulation of integer data. Let me know if you'd like examples for specific applications!