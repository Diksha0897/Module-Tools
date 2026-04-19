Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 1110
We have to divide the number by 2 repeatedly and write down the remainders:

14 ÷ 2 = 7 remainder 0
7 ÷ 2 = 3 remainder 1
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

Then we have to read the remainders from bottom to top: 1110.

Convert the binary number 101101 to decimal:
Answer: 45
Each digit in binary represents a power of 2, starting from the right:

1 × 2⁵ = 32
0 × 2⁴ = 0
1 × 2³ = 8
1 × 2² = 4
0 × 2¹ = 0
1 × 2⁰ = 1

we have to add them all together: 32 + 0 + 8 + 4 + 0 + 1 = 45.

Which is larger: 1000 or 0111?
Answer: 1000
These are binary numbers. In binary, each digit represents a power of 2:

1000 = 1×2³ + 0×2² + 0×2¹ + 0×2⁰ = 8
0111 = 0×2³ + 1×2² + 1×2¹ + 1×2⁰ = 4 + 2 + 1 = 7

Since 8 is bigger than 7, 1000 is larger number.

Which is larger: 00100 or 01011?
Answer:01011
We ignore the zeros as prefix as they don’t change the value.

00100 = 4 in decimal
01011 = 11 in decimal

As, 11 is bigger than 4, 01011 is larger.

What is 10101 + 01010?
Answer:11111
1+0=1, 0+1=1, 1+0=1, 0+1=1, 1+0=1
No carries here, so the answer is 11111.

What is 10001 + 10001?
Answer:100010
Starting from the right: 1 + 1 = 2 in decimal, which is 10 in binary. Write down 0 and carry over 1.
Move to the next column: 0 + 0 + 1 (carry) = 1.
Next column: 0 + 0 = 0
Next column: 0 + 0 = 0
Leftmost column: 1 + 1 = 2 → write 0, carry 1.

After adding the carry at the front, we get 100010.

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 15

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 8 bits (2^8=256)

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer:2 bits
(because 2² = 4 values → 0, 1, 2, 3)

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 10 bits
(2¹⁰ = 1024)

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer:

Convert the decimal number 14 to hex.
Answer:E (Hex goes from 0–15 using digits 0–9 and A–F.
14 corresponds to E.)

Convert the decimal number 386 to hex.
Answer: 182
386 ÷ 16 = 24 remainder 2
24 ÷ 16 = 1 remainder 8
1 ÷ 16 = 0 remainder 1

Read the remainders backwards and we get 182

Convert the hex number 386 to decimal.
Answer:902
Each position is a power of 16:

3 × 16² = 3 × 256 = 768
8 × 16¹ = 8 × 16 = 128
6 × 16⁰ = 6

Add them:
768 + 128 + 6 = 902

Convert the hex number B to decimal.
Answer:11
(In hex:A = 10,B = 11)

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 33 (2 × 16 + 1 = 33)

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer:! (ASCII maps numbers to characters.
Decimal 33 corresponds to ! (exclamation mark))

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: dark grey (n greyscale:
0 = black
255 = white
33 is close to 0, so it’s a very dark grey (almost black).)

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:bright purple (magenta) (Split into three bytes:
AA = red = 170
00 = green = 0
FF = blue = 255

High red + high blue = purple/magenta)

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer:170,0,255
Each pair is one byte:

AA = 170
00 = 0
FF = 255
