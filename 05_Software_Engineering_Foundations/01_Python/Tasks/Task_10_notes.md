# Study Notes: Task_10

Generated Automatically


## Topic 1

### `Q-1:` Write a function `get_final_line(filename)`, which takes filename as input and return final line of the file.

Note: You can choose any file of your choice.

## Code Cell 2

```python
# Write code here
def get_final_line(filename):
    final_line = ''
    for i in open(filename,'r'):
        final_line = i
    return final_line
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 3

```python
get_final_line(r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\sample.txt")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

### `Q-2:` Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation -- dictionary.

## Code Cell 5

```python
# Write code here
def count_vowels(filename):
    vowels = ['a','e','i','o','u']
    d = {i:0 for i in vowels}
    for i in open(filename,'r'):
        for ch in i:
            if ch in vowels:
                d[ch]+=1
    return d
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 6

```python
count_vowels(r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\sample.txt")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

### `Q-3:` Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python to read through the file you’ve created. For each line, multiply each first number by the second and include it in the file in third column. In last add a line Total, by summing the value of third column



## Topic 8

Input File example: That you need to create
```
1   2
3   4
5   6
7   8
9   10

```

Output File Example:
```
1   2   2
3   4   12
5   6   30
7   8   56
9   10  90
Total   190
```


## Code Cell 9

```python
# write code here

file_name = r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\Q3.txt"
f = open(file_name, "w")
for i in range(1, 11, 2):
    line = '{}\t{}\n'.format(i, i+1)
    f.writelines(line)
f.close()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 10

```python
with open(file_name, 'r') as f:
    lines = f.read().splitlines()
    print(lines)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 11

```python
total = 0
with open(file_name, 'w') as f:
    for line in lines:
        a,b = line.split(sep="\t")
        res = int(a) * int(b)
        total+= res
        f.write("{}\t{}\t{}\n".format(a,b, res))
    f.write("Total\t"+str(total))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 12

### `Q-4:` Create line wise reverse of a file
Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).

## Topic 13

For example, if a file looks like
 ```
abc def
ghi jkl
```
then the output file will be
```
fed cba
lkj ihg
```
**Notice**: The newline remains at the end of the string, while the rest of the characters are all reversed.

## Code Cell 14

```python
# write code here
# write code here
input_file = r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\sample.txt"
output_file = r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\sample_reversed.txt"

def reverse_lines(infilename, outfilename):
    with open(infilename, 'r') as infile, open(outfilename, "w") as outfile:
        for one_line in infile:
            outfile.write(one_line[::-1]+"\n")
reverse_lines(input_file, output_file)

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 15

### `Q-5:` Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.

* List of word will be given



## Topic 16

Given String

```
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']
```

## Code Cell 17

```python
# write code here
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 18

```python
with open (r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\string.txt",'w') as f:
    f.write(strings)
    
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 19

```python
filename = r"D:\GENAI\DSMP_Course\04_Advanced_Python\Tasks_Solutions\Data\string.txt"

for i in open(filename,'r'):
    word_list = ['alice', 'wonder', 'natural']
    d = {i:0 for i in word_list}
    for word in i:
        if word in word_list:
            d[word]+=1
    print(d)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

### **`Q-6:`** Given a string calculate length of the string using recursion.

**Example 1:**

Input:
```bash
"abcd"
```

Output:

```bash
4
```

**Example 2:**

Input:
```bash
DataScience
```

Output:

```bash
11
```


## Code Cell 21

```python
# Write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 22

### **`Q-7:`** Write a function that accepts two numbers and returns their greatest common divisior. Without using any loop

def gcd(int, int) => int

```
gcd(16,24) will give 8
```

## Code Cell 23

```python
# Write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 24

 ### `Q-8:` String Edit Distance

 Use your recursive function to write a program that reads two strings from the
user and displays the edit distance between them.

*The edit distance between two strings is a measure of their similarity—the smaller the edit distance, the more similar the strings are with regard to the minimum number of insert, delete and substitute operations needed to transform one string into the other.*

Consider the strings `kitten` and `sitting`. The first string can be transformed
into the second string with the following operations:
* Substitute the `k` with an `s`,
* substitute the `e` with an `i`,
* and insert a `g` at the end of the string.

This is the smallest number of operations that can be performed to transform kitten into sitting. As a result, the edit distance is `3`.


Write a recursive function that computes the edit distance between two strings.

Use the following algorithm:

```
Let s and t be the strings
    If the length of s is 0 then
        Return the length of t
    Else if the length of t is 0 then
        Return the length of s
    Else
        Set cost to 0
        If the last character in s does not equal the last character in t then
            Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all characters except the last one in t, plus 1

        Set d3 equal to the edit distance between all characters except the last one in s, and all characters except the last one in t, plus cost
        Return the minimum of d1, d2 and d3
```





## Code Cell 25

```python
# write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 26

###`Q-9:` Run-Length Encoding

Run-length encoding is a simple data compression technique that can be effective when repeated values occur at adjacent positions within a list. Compression is achieved by replacing groups of repeated values with one copy of the value, followed by the number of times that the value should be repeated. For example, the list
```
["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
```
would be compressed as `["A", 12, "B", 4, "A", 6, "B", 1]`.

Write a recursive function that implements the run-length compression technique
described above. Your function will take a list or a string as its only parameter. It should return the run-length compressed list as its only result. Include a main program that reads a string from the user, compresses it, and displays the run-length encoded result.

## Code Cell 27

```python
# Write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 28

###`Q-10:` Write a recursive function to convert a decimal to binary

## Code Cell 29

```python
# Write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

