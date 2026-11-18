# Study Notes: Pracitce_Questions

Generated Automatically


## Topic 1

## **Problem-1: Breaking the records.**

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

**Example**

*scores \= \[12, 24, 10, 24\]*

Scores are in the same order as the games played. She tabulates her results as follows:

| Game | Score | Minimum | Maximum | Count Min | Count Max |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 12 | 12 | 12 | 0 | 0 |
| 1 | 24 | 12 | 24 | 0 | 1 |
| 2 | 10 | 10 | 24 | 1 | 1 |
| 3 | 24 | 10 | 24 | 1 | 1 |

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

**Function Description**

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

* n: no of games

* int scores\[n\]: points scored per game

**Returns**

* int\[2\]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.

**Input Format**

n, the number of games. Integers array osf scores describing the respective values of $scor{e}_{0},scor{e}_{1},scor{e}_{2},...,scor{e}_{n-1}$.

**Constraints**

* $1<=n<=1000$

* $0<=scores\left[{i}\right]<={10}^{8}$

**Sample Input 0**

10 5 20 20 4 5 2 25 1

**Sample Output 0**

2 4

**Explanation 0**

The diagram below depicts the number of times Maria broke her best and worst records throughout the season:

| Games | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Score** | 10 | 5 | 20 | 20 | 4 | 5 | 2 | 25 | 1 |
| **Highest Score** | 10 | 10 | **20** | 20 | 20 | 20 | 20 | **25** | 25 |
| **Lowest Score** | 10 | **5** | 5 | 5 | **4** | 4 | **2** | 2 | **1** |

She broke her best record twice (after games 2 and 7\) and her worst record four times (after games 1, 4, 6, and 8), so we print 2 4 as our answer. Note that she did not break her record for best score during game 3, as her score during that game was not strictly greater than her best record at the time.

*\#Solution* Provided

## **Problem-2: Student management system in Python**

Write a program to build a simple Student Management System using Python which can perform the following operations:

1. **Accept \-** This method takes details from the user like name, roll number, and marks for two different subjects.

2. **Display \-** This method displays the details of every student.

3. **Search \-** This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number

4. **Delete \-** This method deletes the record of a particular student with a matching roll number.

5. **Update \-** This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.

Operations used, 

1.Accept Student details  
2.Display Student Details  
3.Search Details of a Student  
4.Delete Details of Student  
5.Update Student Details  
6.Exit

List of Students

Name :  A  
RollNo :  1  
Marks1 :  100  
Marks2 :  100

Name :  B  
RollNo :  2  
Marks1 :  90  
Marks2 :  90

Name :  C  
RollNo :  3  
Marks1 :  80  
Marks2 :  80

Search method output:

 Student Found,   
Name :  B  
RollNo :  2  
Marks1 :  90  
Marks2 :  90

## **Problem-3: Get current times of different time zones in Python.**

## **Problem-4: Python program to count Even and Odd numbers in a List using list comprehension.**

Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

**Example:**

Input: list1 \= \[2, 7, 5, 64, 14\]  
Output: Even \= 3, odd \= 2

Input: list2 \= \[12, 14, 95, 3\]  
Output: Even \= 2, odd \= 2

## **Problem-5: Alphabet Rangoli**

You are given an integer, $N$. Your task is to print an alphabet rangoli of size

$N$. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

*\#size 3*

\----c----  
\--c-b-c--  
c-b-a-b-c  
\--c-b-c--  
\----c----

*\#size 5*

\--------e--------  
\------e-d-e------  
\----e-d-c-d-e----  
\--e-d-c-b-c-d-e--  
e-d-c-b-a-b-c-d-e  
\--e-d-c-b-c-d-e--  
\----e-d-c-d-e----  
\------e-d-e------  
\--------e--------

*\#size 10*

\------------------j------------------  
\----------------j-i-j----------------  
\--------------j-i-h-i-j--------------  
\------------j-i-h-g-h-i-j------------  
\----------j-i-h-g-f-g-h-i-j----------  
\--------j-i-h-g-f-e-f-g-h-i-j--------  
\------j-i-h-g-f-e-d-e-f-g-h-i-j------  
\----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----  
\--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--  
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j  
\--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--  
\----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----  
\------j-i-h-g-f-e-d-e-f-g-h-i-j------  
\--------j-i-h-g-f-e-f-g-h-i-j--------  
\----------j-i-h-g-f-g-h-i-j----------  
\------------j-i-h-g-h-i-j------------  
\--------------j-i-h-i-j--------------  
\----------------j-i-j----------------  
\------------------j------------------

The center of the rangoli has the first alphabet letter a, and the boundary has the ${N}^{th}$alphabet letter (in alphabetical order).

### **Problem-6: Compress a string\!**

You are given a string $S$. Suppose a character '$c$' occurs consecutively $X$ times in the string. Replace these consecutive occurrences of the character '$c$' with \$\$(X, c) in the string. For a better understanding of the problem, check the explanation.

**Input Format:**

A single line of input consisting of the string $S$.

**Output Format:**

A single line of output consisting of the modified string.

**Sample Input:**

1222311

**Sample Output:**

**(**1, 1**)** **(**3, 2**)** **(**1, 3**)** **(**2, 1**)**

**Explanation:**

First, the character occurs only once. It is replaced by (1, 1). Then the character 2 occurs three times, and it is replaced by (3, 2 )and so on. Also, note the single space within each compression and between the compressions.

### **Problem-7: Word order**

You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

*Note: Each input line ends with a **"\\n"** character.*

**Input Format:**

The first line contains the integer, $n$.

The next $n$ lines each contain a word.

**Output Format:**

Output $2$ lines.

On the first line, output the number of distinct words from the input.

On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

**Sample Input:**

4  
bcdef  
abcdefg  
bcde  
bcdef

**Sample output:**

3  
2 1 1

**Explanation:**

There are $3$ distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

## **Problem-8:Iterables & Iterators**

You are given a list of $N$ lowercase English letters. For a given integer $K$, you can select any $K$ indices (assume 1-based indexing) with a uniform probability from the list. Find the probability that at least one of the $K$ indices selected will contain the letter '$a$'.

**Input Format:**

The input consists of three lines. The first line contains the integer $N$, enoting the length of the list. The next line consists of \&N& space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer $K$, denoting the number of indices to be selected.

**Output Format:**

Output a single line consisting of the probability that at least one of the $K$ indices selected contains the letter '$a$'.

Note: The answer must be correct up to 3 decimal places.

**Sample Input:**

4   
a a c d  
2

**Sample Output:**

0.8333

**Explanation:**

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are: (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4\)

Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter '$a$'. Hence, the answer is $\frac{5}{6}$

## **Problem-9: The Captain's Room**

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel. The tourists consist of:

→ A Captain.

→ An unknown group of families consisting of $K$ members per group where $K\ne 1$

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear $K$ times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number. The total number of tourists or the total number of groups of families is not known to you. You only know the value of $K$ and the room number list.

**Input Format:**

The first line consists of an integer, $K$, the size of each group.

The second line contains the unordered elements of the room number list.

**Output Format:**

Output the Captain's room number.

**Sample Input:**

5  
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

**Sample Output**

8

**Explanation:**

The list of room numbers contains 31 elements. Since K is 5, there must be groups 6 of families. In the given list, all of the numbers repeat 5 times except for room number 8\. Hence, 8 is the Captain's room number.

## **Problem-10: Classes: Dealing with Complex Numbers**

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

**Input Format:**

One line of input: The real and imaginary part of a number separated by a space.

**Output Format:**

For two complex numbers $C$ and $D$, the output should be in the following sequence on separate lines:

* \$C \+ D

* \$C \- D

* $C*D$

* $C/D$

* $mod\left({C}\right)$

* $mod\left({D}\right)$

For complex numbers with non-zero real ($A$) and complex part (\$B), the output should be in the following format:

$A+Bi$

Replace the plus symbol ($+$) with a minus symbol ($-$) when $B<0$.

For complex numbers with a zero complex part i.e. real numbers, the output should be:

$A+0.00i$

For complex numbers where the real part is zero and the complex part ($B$) is non-zero, the output should be:

$0.00+Bi$

**Sample Input:**

2 1  
5 6

**Sample Output:**

7.00+7.00i  
\-3.00-5.00i  
4.00+17.00i  
0.26-0.11i  
2.24+0.00i  
7.81+0.00i

**Concept:**

Solve this problem using Object Oriented way. Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

\_\_add\_\_-\> Can be overloaded for \+ operation

\_\_sub\_\_ \-\> Can be overloaded for \- operation

\_\_mul\_\_ \-\> Can be overloaded for \* operation

## **Problem-11: Find the Torsional angle**

You are given four points $A,B,C$ and $D$ in a 3-dimensional Carterian coordinate system. You are required to print the angle between the plane made by the points $A,B,C$ and $B,C,D$ in degrees (**not radians**). Let the angle be $\phi$.

$cos\left({\phi }\right)=\left({X.Y}\right)/\left|{X}\right|\left|{Y}\right|$ where $X=AB*BC$ and $Y=BC*CD$

Here, $X.Y$ means the dot product of $X$ and $Y$ and $AB*BC$ means the cross product of vectors $AB$ and $BC$. Also, $AB=B-A$

**Input Format:**

One line of input containing the space separated floating number values of the $X,Y$ and $Z$ coordinates of a point.

**Output Format:**

Output the angle correct up to two decimal places.

**Sample Input:**

0 4 5  
1 7 6  
0 5 9  
1 7 2

**Sample Output:**

8.19

from math import sqrt

### **Problem-12: Maximize it**

You are given a function $f\left({X}\right)={X}^{2}$. You are also given $K$ lists. The ${i}^{th}$ list consists of ${N}_{i}$ elements. You have to pick one element from each list so that the value from the equation below is maximized:

\$S \= (f(X\_1) \+ f(X\_2) \+ ... \+ f(N\_k)) % M \$

${X}_{i}$ denotes the element picked from the ${i}^{th}$ list. Find the maximized value ${S}_{max}$ obtained.

$%$ denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

**Input Format:**

The first line contains 2 space separated integers $K$ and $M$.

The next $K$ lines each contains an integer ${N}_{i}$, denoting the number of elements in the ${i}^{th}$ list, followed by ${N}_{i}$ space separated integers denoting the elements in the list.

**Output Format:**

Output a single integer denoting the value ${S}_{m}ax$

**Sample Input:**

3 1000  
2 5 4  
3 7 8 9   
5 5 7 8 9 10 

**Sample Output:**

206

**Explanation:**

Picking 5 from ${1}^{st}$ list, 9 from the ${2}^{nd}$ list and 10 from the ${3}^{rd}$ list gives the maximum $S$ value equal to $\left({{5}^{2}+{9}^{2}+{10}^{2}}\right)%1000=206$

## **Problem-13: Diamond shape**

Write a python program to print the diamond shape. Given a number n, write a program to print a diamond shape with 2n rows.

![Sample][image1]

          

## **Problem-14: Write a python function to print the half-diamond star pattern.**

Given an integer N, the task is to print half-diamond-star pattern.

\*  
\*\*  
\*\*\*  
\*\*\*\*  
\*\*\*\*\*  
\*\*\*\*\*\*  
\*\*\*\*\*  
\*\*\*\*  
\*\*\*  
\*\*  
\*

### **Problem-15: Write a Python program to find the power of a given number using recursion.**

Given a number $N$ and power $P$, the task is to find the power of a number ( i.e. ${N}^{P}$ ) using recursion.

## **Problem-16: Largest number in a list**

Write a Python program to find the largest number in a list without using built-in methods.

### **Problem-17: Reverse integer**

Write a python function that accepts any length of the integers and prints that integer in a reverse manner. Don't use any python trick or python special syntax.

## **Problem-18: Celsius to Farenhight**

Write a Python function that can convert the degree of Celsius to the Farenhight scale.

## **Problem-19: is it right?**

You are given two values $a$ and $b$. Perform integer division and print $a/b$.

**Input Format:**

The first line contains $T$, the number of test cases.

The next $T$ lines each contain the space separated values of $a$ and $b$.

**Output Format:**

Print the value of $a/b$.

In the case of *ZeroDivisionError* or *ValueError*, print the error code.

**Sample Input:**

3  
1 0  
2 5  
3 1

**Sample Output:**

Error Code: integer division or modulo by zero  
Error Code: invalid literal for int**()** with base 10: '\$'  
3

### **Problem- 20: Piling Up\!**

There is a horizontal row of $n$ cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if $cube\left[{i}\right]$ is on top of $sube\left[{j}\right]$ then $sideLength\left[{j}\right]>=sigeLength\left[{i}\right]$.

When stacling the cubes, you can only pick up either leftmost or the rightmost cube each time. Print Yes if it possible to stack the cubes. Otherwise, print No.

**Example:**

$blocks=\left[{1,2,3,8,7}\right]$

Result: No

After choosing the rightmost element 7, choose the leftmost element, 1\. After than, the choices are 2 and 8\. These are both larger than the top block of size 1\.

$blocks=\left[{1,2,3,7,8}\right]$

Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

**Input Format:**

The first line contains a single integer $T$, the number of test cases.

For each test case, there are 2 lines.

The first line of each test case contains $n$, the number of cubes.

The second line contains $n$ space separated integers, denoting the sideLengths of each cube in that order.

**Output Format:**

For each test case, output a single line containing either Yes or No.

**Sample Input:**

STDIN        Function  
\-----        \--------  
2            T \= 2  
6            blocks\[\] size n \= 6  
4 3 2 1 3 4  blocks \= \[4, 3, 2, 1, 3, 4\]  
3            blocks\[\] size n \= 3  
1 3 2        blocks \= \[1, 3, 2\]

**Sample Output:**

Yes  
No

**Explanation:**

In the first test case, pick in this order: *left-4, right-4, left-3, right-3,left-2, right-1*

In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2\.

### **Problem- 21 The following Python code represents a Tic-Tac-Toe board as a list of**

lists: \[ \[ '\#' , 'o' , 'x' \] , \[ '\#' , '\#' , 'o' \] , \[ 'x' , '\#' , 'o' \] \]

The \# symbols represent blank squares on the board. Write a function print\_board that takes a list of lists as an argument and prints out a Tic-Tac-Toe board in the following format:

   \| o \| x  
\------------  
   \|   \| o  
\------------  
 x \|   \| o

\------------

### **Problem- 22: Wobbly Number**

A “wobbly” number is one in which the digits alternate between being higher and lower than the preceding one. Here are some wobbly numbers: 19284756242, 90909, 0909. Write a function that accepts a list of digits to be checked for wobbliness. If the sequence of digits is wobbly, the function should return True, otherwise False.

### **Problem- 23-25**

Imagine a fictional land where monetary units aren’t based on decimal orders. In this land, we have 3 basic units of currency:

* The Blink. The smallest unit of currency.

* The Hoojim. Worth 12 Blinks.

* The Bung. Worth 20 Hooja (plural of Hoojim) or 240 Blinks.

## **Problem- 23 Write a function called deBung** 

Write a function called deBung that accepts an integer representing a number of Bungs and displays the number of Hooja and Blink it is worth.

For example,calling the function like this:

deBung ( 4 )

Will produce the following output: 4 Bungs is worth 80 Hoojim or 960 Blinks.

*\#Code here*

## **Problem- 24 Write a function called enBlinkHoojaBung** 

Write a function called enBlinkHoojaBung that takes a number of Blinks and outputs its equivalent in Blink, Hooja and Bung, using the smallest number of coins. Coins in our imaginary land are made of a very heavy metal, so this is important.

If the function is called with the value 506, the output should be: 506 Blinks is worth 2 Bung, 1 Hoojim and 6 Blinks.

*\#Code here*

## **Problem- 25 Rewrite enBlinkHoojaBung()**

Rewrite enBlinkHoojaBung so that it returns a tuple of Blinks, Hooja and Bung values instead of writing to the screen. The last example would return ( 2 , 1 , 6 ).

*\#code here*

## **Problem- 26-28**  

Convert the following iterative functions into recursive functions:

P-26:

def sum\_even ( n : int) :  
    total \= 0  
    for i in range ( 2 , n \+ 1 , 2 ) :  
        total \+= i  
    return total

P-27:

def min ( l:list ) :  
    m \= 0  
    for i in l :  
        if i\<m :   
            m \= i  
    return m

P-28:

def prod ( l : list ) :  
    product , i \= 1 , 0  
    while i \< len ( l ) :  
        product \*= l\[i\]  
        i \+= 1  
    return product

## **Problem- 29-31** 

Convert the following iterative functions into recursive functions: P-29:

def sum\_odd ( n , total ) :  
    if n \== 1 :   
        return total  
    elif n % 2 \== 0 :   
        return sum\_odd ( n \- 1 , total )  
    else :   
        return sum\_odd ( n \- 2 , total \+ n )

P-30:

def max ( l , n ) :  
    if l \== \[ \] :   
        return n  
    elif l\[0\] \> n :   
        return max ( l\[1:\] , l\[0\] )  
    else :   
        return max ( l\[1:\] , n )

P-31:

def mylen ( l , n ) :  
    if l \== \[\] :   
        return n  
    else :   
        return mylen ( l\[1:\] , n \+1 )

## **Problem- 32-35** 

P-32: \> Use map and lambda to turn a list of integers from1 to 100into a list of even numbers from2 to 200\`.

P-33:

Use filter to generate a list of odd numbers from 0 to 100

P-34:

Use a list comprehension to generate a list of odd numbers from 0 to

P-35:

Write a generator function (using the yield keyword) that generates factorial numbers.

## **Problem- 36 : Ackermann’s Function**

Ackermann’s Function is defined as:

          n+1 if m \= 0  
 A(m,n) \= A(m−1,1) if m \> 0 and n \= 0  
          A(m−1,A(m,n−1)) if m \> 0 and n \> 0

i. Write a recursive Python function to implement Ackermann’s Function.

ii. How many recursive calls will be required to evaluate A(2,3)?

## **Problem- 37 : Palindrome String** 

Write a recursive function implementation of isPalindrome to test whether or not a string is a palindrome.

a man, a plan, a canal, panama\! is a palindrome – so we do not make spaces and special characters(\! here) significant.

## **Problem- 38  Create a module for playing Tic-Tac-Toe.** 

Hint: You may want to consider the following functions:

1. print\_board ( ) – from the programming exercise above, except that you will want to use a global board variable, rather than a function argument.

2. has\_won ( ) – check to see whether either player has won. This function should return the string ’o’ or ’x’ if either the o or x player has won and ’\#’ if neither player has won. A player wins in Tic-Tac-Toe if they have three of their counters in a row, a column or a diagonal.

3. place\_counter ( sq , counter ) – place the counter on a particular square of the board. The first argument should be a number between 0 and 8 and the second argument should be either ’o’ or ’x’. You should consider the squares on the board to be numbered as in the diagram below.

    0 \| 1 \| 2  
    \----------  
    3 \| 4 \| 5  
    \----------  
    6 \| 7 \| 8

Using a numbering such as this one makes the answer to this challenge simpler\!

1. next\_play ( ) – This function should ask the user for the next move they want to play. You should make sure that the user knows whether x or o is currently playing. You can assume that the user will enter an integer value. You should still check that the integer the player has provided is between 0 and 8 inclusive.

*\#Think yourself for answers*

## **Problem- 39 : Die class** 

Create a class to represent a single die that can have any positive integer number of sides. This kind of die might be used when playing role-playing games (RPGs).

##  **Problem- 40  Account class** 

Write a class Account that stores the current balance, interest rate and account number of a bank account. Your class should provide methods to withdraw, deposit and add interest to the account. The user should only be allowed to withdraw money up to some overdraft limit. If an account goes overdrawn, there is fee charged.

Extend Above class, (self doing);

* Create a subclasses of your Account class (from problem 40\) called CreditAccount in which the user is charged a set amount for every withdrawal that is made. If the user is overdrawn, the withdrawal charge is doubled.

* Create a subclasses of your Account class (from problem 40\) called StudentAccount in which new accounts start off with a balance of 500 and an overdraft of up to 3000 is allowed, with no charges for withdrawal

Consider other assumptions yourself if required.

Thank you\!

# **Happy Learning\!\!**

[image1]: <data:image/png;base64,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>

## Code Cell 2

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

