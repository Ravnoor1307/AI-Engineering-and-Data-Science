# Study Notes: Task_19

Generated Automatically


## Topic 1

## **Questions based on Titanic Dataset:**

To read the dataset as csv, use the below code:

```python
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv"
titanic_df = pd.read_csv(url)
```

## Topic 2

### `Q-1:` Using `groupby` make groups using the `"Pclass"` column and find out the average age and total number of missing values in the `"Age"` column for every group.

## Code Cell 3

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

### `Q-2:` Using `groupby` make groups using the `"Pclass"` column and fill every group's `"Embarked"` column's missing values with the mode value of that group. After that, print every group's `"Embarked"` column's value counts in ascending order.

## Code Cell 5

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 6

### `Q-3:` Make groups based on `"Embarked"` column. And for each of this embarked group, make another group based on `"Pclass"` and find out the average fare (round off up to 2 decimal places) for each "Pclass" for each group of "Embarked".

**Sample Output:**

```bash
{'C': {1: 105, 2: 25, 3: 11},
 'Q': {1: 90, 2: 12, 3: 11},
 'S': {1: 70, 2: 20, 3: 15}}
```

## Code Cell 7

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

## **Questions Based on Fifa Worldcup - 2022 Dataset:**

You can read the dataset by using the below sample code

```python
import pandas as pd

fifa_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv")
```

## Topic 9

### `Q-4:` Perform `groupby` based on the `"Team"` column and then perform Z Normalization on top of the below columns of each group:
1. Passes
2. Passes Completed
3. Attempted Line Breaks
4. Completed Line Breaks

You have to make a python function named `z_normalization` which takes two arguments:

1. *group:* Every group that you have created
2. *cols_to_perform:* This parameter takes a list of columns on which you have to perform the Z-Normalization.

For this problem, you have to use th `apply()` method.

$\Large Z \ - \ Normalization = \frac{X_i - \mu}{std} $

After that find out the below values for each group:
- minimum "Passess"
- maximum "Passess"
- minimum "Yellow Cards"
- maximum "Yellow cards"
- average "Yellow Cards"
- maximum "Attempted Line Breaks"
- minimum "Attempted Line Breaks"
- standardard deviation of "Attempted Line Breaks"
- average Possession

## Code Cell 10

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

## **Questions on IPL wala dataset**

ball by ball dataset - https://drive.google.com/file/d/1-kvv_9KCSAFWcrhS9WgTxSrURkRh6GNt/view?usp=share_link





## Topic 12

###`Q-5:` Find batsman in below category-
* Highest score while chasing
* Best Strike rate while chasing and have faced 100+ balls


> Chasing mean team batting in second inning

## Code Cell 13

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 14

###`Q-6` Most Successful bowler against any batsman. Find that pair of bowler and batsman.
> Most Successful in terms of dissmissal. A bowler who have dissmissed any batsman most no of times. If any two pairs have same no of dissmisal, consider runs conceded by bowler to that batsman. Those who have concede lesser runs is more successful.

## Code Cell 15

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

###`Q-7`: Most successful batting pair in IPL. Batting pair who have scored most runs playing together.


## Code Cell 17

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 18

###`Q-8:` Make a dataframe for all batting pairs played together.
```
Batsman1 Batsman2 Runs Avg StrikeRate
```

> Just to ease this question you can count wide-balls for strike rate.

## Code Cell 19

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

