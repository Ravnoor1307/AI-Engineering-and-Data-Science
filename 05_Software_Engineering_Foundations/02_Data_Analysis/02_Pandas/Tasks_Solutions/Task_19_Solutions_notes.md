# Study Notes: Task_19_Solutions

Generated Automatically


## Topic 1

## **Questions based on Titanic Dataset:**

To read the dataset as csv, use the below code:

```python
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv"
titanic_df = pd.read_csv(url)
```

## Code Cell 2

```python
import pandas as pd
import numpy as np

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv"
titanic_df = pd.read_csv(url)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 3

### `Q-1:` Using `groupby` make groups using the `"Pclass"` column and find out the average age and total number of missing values in the `"Age"` column for every group.

## Code Cell 4

```python
# code here
pclass_groups = titanic_df.groupby("Pclass")
for group in list(pclass_groups.groups.keys()):
    print(f"Pclass {group} : Avg Age {pclass_groups.get_group(group)['Age'].mean()} and total missing value {pclass_groups.get_group(group)['Age'].isna().sum()}")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 5

### `Q-2:` Using `groupby` make groups using the `"Pclass"` column and fill every group's `"Embarked"` column's missing values with the mode value of that group. After that, print every group's `"Embarked"` column's value counts in ascending order.

## Code Cell 6

```python
# code here - Done in session
for group in list(pclass_groups.groups.keys()):
    mode = pclass_groups.get_group(group)["Embarked"].mode()
    pclass_groups.get_group(group)["Embarked"].fillna(mode)
    print(pclass_groups.get_group(group)["Embarked"].value_counts(ascending = True))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

* Nan value is not updated in the dataframe in the above approach.

## Code Cell 8

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 9

```python
# Updated Code : Approach 1
titanic_df1 = titanic_df.copy(True)

# Step 1: Group by 'Pclass' and fill missing values in 'Embarked' with the mode value of that group
titanic_df1['Embarked'] = titanic_df1.groupby('Pclass')['Embarked'].transform(lambda x: x.fillna(x.mode()[0]))

# Step 2: Print the value counts of 'Embarked' for each group in ascending order
grouped = titanic_df1.groupby('Pclass')[['Embarked']]
grouped.value_counts().sort_index(ascending=True)
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
# Updated Code : Approach 2

titanic_df2 = titanic_df.copy(True)
pclass_groups=titanic_df2.groupby('Pclass')
for group in list(pclass_groups.groups.keys()):
    mode_val=pclass_groups.get_group(group)['Embarked'].mode()
    titanic_df2.loc[pclass_groups.get_group(group).index, 'Embarked'] = pclass_groups.get_group(group)['Embarked'].fillna(mode_val[0])
    print(pclass_groups.get_group(group)['Embarked'].value_counts())
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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 12

### `Q-3:` Make groups based on `"Embarked"` column. And for each of this embarked group, make another group based on `"Pclass"` and find out the average fare (round off up to 2 decimal places) for each "Pclass" for each group of "Embarked".

**Sample Output:**

```bash
{'C': {1: 105, 2: 25, 3: 11},
 'Q': {1: 90, 2: 12, 3: 11},
 'S': {1: 70, 2: 20, 3: 15}}
```

## Code Cell 13

```python
# code here
my_dict = {}

embarked_groups = titanic_df.groupby("Embarked")
for embarked_group in list(embarked_groups.groups.keys()):
    pclass_groups = embarked_groups.get_group(embarked_group).groupby("Pclass")
    my_dict[embarked_group] = {}
    for pclass_group in list(pclass_groups.groups.keys()):
        my_dict[embarked_group][pclass_group] = round(pclass_groups.get_group(pclass_group)["Fare"].mean(), 2)
my_dict
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 14

## **Questions Based on Fifa Worldcup - 2022 Dataset:**

You can read the dataset by using the below sample code

```python
import pandas as pd

fifa_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv")
```

## Code Cell 15

```python
import pandas as pd

fifa_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

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

## Code Cell 17

```python
# code here
def z_normalization(group, cols_to_perform):
    for col in cols_to_perform:
        std = group[col].std()
        mean = group[col].mean()
        group[f"{col}_z_norm"] = (group[col] - mean)/std
    return group


cols_to_perform = ["Passes", "Passes Completed", "Attempted Line Breaks", "Completed Line Breaks"]
groups = fifa_df.groupby("Team")
groups = groups.apply(z_normalization, cols_to_perform = cols_to_perform).groupby("Team")
groups.agg(
{
    "Passes": ["min", "max"],
    "Yellow Cards": ["min", "max", "mean"],
    "Attempted Line Breaks": ["max", "min", "std"],
    "Possession (%)": "mean"
})
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 18

## **Questions on IPL wala dataset**

ball by ball dataset - https://drive.google.com/file/d/1-kvv_9KCSAFWcrhS9WgTxSrURkRh6GNt/view?usp=share_link





## Code Cell 19

```python
balls = pd.read_csv("ipl_deliveries - ipl_deliveries.csv")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

### `Q-5:` Find batsman in below category-
* Highest score while chasing
* Best Strike rate while chasing and have faced 100+ balls


> Chasing mean team batting in second inning

## Code Cell 21

```python
# code here
#1
df = balls[balls.innings == 2]
df.groupby(["ID", "batter"]).sum().sort_values(by = "batsman_run", ascending = False)["batsman_run"].head()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 22

```python
#2
temp_df = df[~(df.extra_type == "wides")]
temp_df = temp_df.groupby("batter").agg(
{
    "batsman_run": "sum",
    "ballnumber": "count"
})
temp_df["strike_rate"] = temp_df["batsman_run"] / temp_df["ballnumber"] * 100
temp_df[temp_df["ballnumber"] >= 100].sort_values("strike_rate", ascending = False).reset_index().head()

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

### `Q-6` Most Successful bowler against any batsman. Find that pair of bowler and batsman.
> Most Successful in terms of dissmissal. A bowler who have dissmissed any batsman most no of times. If any two pairs have same no of dissmisal, consider runs conceded by bowler to that batsman. Those who have concede lesser runs is more successful.

## Code Cell 24

```python
# code here

balls["IsBatterOut"] = (balls.batter == balls.player_out)&(~balls.kind.isin(['run out', 'retired hurt', 'retired out']))
balls.groupby(["bowler", "batter"]).agg({
    "IsBatterOut": "sum",
    "batsman_run": "sum"
}).sort_values(by=["IsBatterOut", "batsman_run"], ascending = [False, True]).head(10)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 25

### `Q-7`: Most successful batting pair in IPL. Batting pair who have scored most runs playing together.


## Code Cell 26

```python
# code here
def func(x):
    return '-'.join(list(np.sort(x.values)))
balls["batter-pair"] = balls[["batter", "non-striker"]].apply(func, axis = 1)
balls.groupby("batter-pair")["total_run"].sum().sort_values(ascending = False).head()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 27

### `Q-8:` Make a dataframe for all batting pairs played together.
```
Batsman1 Batsman2 Runs Avg StrikeRate
```

> Just to ease this question you can count wide-balls for strike rate.

## Code Cell 28

```python
# code here
temp_df = balls.groupby("batter-pair").agg(
{
    "total_run": "sum",
    "ballnumber": "count",
    "isWicketDelivery": "sum"
}).reset_index()
temp_df["Batsman 1"] = temp_df["batter-pair"].apply(lambda x: x.split("-")[0])
temp_df["Batsman 2"] = temp_df["batter-pair"].apply(lambda x: x.split("-")[1])
temp_df.rename(columns = {"total_run": "Runs"}, inplace=True)
temp_df["StrikeRate"] = temp_df["Runs"] / temp_df["ballnumber"] * 100
temp_df["Avg"] = temp_df["Runs"] / temp_df["isWicketDelivery"]
temp_df.sort_values("Runs", ascending = False, inplace=  True)
temp_df[["Batsman 1", "Batsman 2", "Runs", "Avg", "StrikeRate"]]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 29

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

