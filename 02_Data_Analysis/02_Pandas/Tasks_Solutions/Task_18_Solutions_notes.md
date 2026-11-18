# Study Notes: Task_18_Solutions

Generated Automatically


## Code Cell 1

```python
import numpy as np
import pandas as pd

# to visualize all the column, run the below code
pd.options.display.max_columns = None
# to show all the records, use the below code
# pd.options.display.max_rows = None
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 2

## Fifa Worldcup - 2022 dataset.

You can find the dataset from [here](https://www.kaggle.com/datasets/sayanroy729/fifa-worldcup-2022-results).

Also you can directly use an url to read the dataset by using `pd.read_csv()` method. Check the below code cell.

## Code Cell 3

```python
# To get the details about the dataset, please visit
# https://www.kaggle.com/datasets/sayanroy729/fifa-worldcup-2022-results

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
df.head()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

### `Q-1:` Use the football dataset. Find out the total percentages that each team made on target. Display the result as a python dictionary where the keys are the team list and the values are the percentage values. Round off the percentage values up to 2 decimal places.

*Help:*
- First, find out how many total teams are participated in this worldcup. For that, you can use `unique()` method on the column "Team" or "Against".
- Loop through the teams list that you have found in previous section, and then filter the dataset according to that. After filtering the dataset, find out total attempts sum and total on target sum.
- After getting these values, find out the percentage by total on target divided by total attempts and multiply by 100. And store to a python dictionary where the key will be the team name and the values will be the percentages.
- At the end,sort the dictionary by the values (not by the keys) and print the result.


## Topic 5


**Sample Output:**
```bash
{'Costa Rica': 54.55,
 'Cameroon': 51.85,
 'Ecuador': 48.15,
 'Argentina': 46.99,
 'Brazil': 45.56,
 'England': 45.0,
 'Portugal': 40.32,
 'Ghana': 40.0,
 'Netherlands': 39.02,
 'Korea Republic': 36.73,
 'Australia': 36.0,
 'Mexico': 34.88,
 'Croatia': 34.78,
 'Germany': 34.33,
 'France': 32.97,
 'Spain': 32.69,
 'Belgium': 32.35,
 'Serbia': 32.26,
 'Iran': 31.43,
 'Uruguay': 31.25,
 'United States': 31.11,
 'Saudi Arabia': 31.03,
 'Senegal': 30.77,
 'Denmark': 30.56,
 'Switzerland': 30.56,
 'Japan': 30.23,
 'Wales': 29.17,
 'Qatar': 28.57,
 'Morocco': 28.3,
 'Tunisia': 26.67,
 'Poland': 25.0,
 'Canada': 17.65}
```

## Code Cell 6

```python
# code here
all_teams = df['Team'].unique()
on_target_percentage = {}
for team in all_teams:
    total_attempts = df[df['Team'] == team]["Total Attempts"].sum()
    total_on_target = df[df['Team'] == team]["On Target"].sum()
    on_target_percentage[team] = round(total_on_target / total_attempts * 100, 2)
dict(sorted(on_target_percentage.items(), key = lambda x: x[1], reverse=True))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

### `Q-2:` Find out how many times the teams are played in this Fifa Worldcup-2022. On top of this, find out the ranks of the teams.

Note: The `DataFrame.rank()` method takes an optiinal parameter named `method`. This parameter takes different values, but one of them is `average` which is by-default. So, when you do the rank, you will get some 2.5 like floating values. But if you change the value as `first`, then you will get in integers but the datatype will be float. So, try with `method="first"` parameter.

## Code Cell 8

```python
# code here
df['Team'].value_counts().rank(method="first")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 9

### `Q-3:` Find out these below topics:
- The information about the Fifa worldcup dataset.
- The description about the Fifa worldcup dataset
- Check is there any missing values, if there is any missing values, fill that value with the average value for that particular column.
- Drop all the duplicate rows permanently.
- Drop the columns: "Sl No", "Match No.", "Red Cards" and "Pts" permanently.

## Code Cell 10

```python
# code here
print(df.info())
print(df.describe())
print(df.isna().sum())
df.drop_duplicates(inplace=True)
df.drop(columns=["Sl. No", "Match No.", "Red Cards", "Pts"], inplace=True)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

### `Q-4:` Do these below operations:
- Find out the rank based on the "Team" column and save the result by adding a new column named "Rank".
- Change the datatype of this column to integer by using `np.int16`
- Set the index of the DataFrame by using this "Rank" column permanently.
- After that, sort the dataframe based on the "Rank" index.

## Code Cell 12

```python
# code here
df["Rank"] = df["Team"].rank(method='first')
df["Rank"] = df["Rank"].astype(np.int16)
df.set_index("Rank", inplace=True)
df.sort_index()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 13

## Questions on Titanic dataset.

You can get the dataset from [here](https://www.kaggle.com/competitions/titanic). This is the competition page on Kaggle. To download the dataset from here, I guess you have to register for the compition. So, do so and then download the dataset.

Also, for now you can use this url to read the dataset like before:
- dataset 1: https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv
- dataset 2: https://docs.google.com/spreadsheets/d/e/2PACX-1vQcPvQsSC9aNFogvbUG08nu0bGHlOclGYaOlhND_LE5Ff7ZnHQ5VYzAgpyT5XNklgiT54SsNgHePsUa/pub?gid=1656109608&single=true&output=csv

## Topic 14

### `Q-5:` Do the below tasks:
1. With dataset 1, drop those records which only have missing values of the "Age" column permanently.

2. With the dataset 2, fill the missing values with 20 to the only "Age" column permanently.

## Code Cell 15

```python
# code here
titanic_df1 = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv")
titanic_df2 = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQcPvQsSC9aNFogvbUG08nu0bGHlOclGYaOlhND_LE5Ff7ZnHQ5VYzAgpyT5XNklgiT54SsNgHePsUa/pub?gid=1656109608&single=true&output=csv")

titanic_df1.dropna(subset=["Age"], inplace=True)
titanic_df2["Age"] = titanic_df2["Age"].fillna(20)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

## Questions on IPL wala dataset

matches dataset = https://drive.google.com/file/d/1yKVUuexl6lIKuFQy7uIPgDgXhJ0L4SIg/view?usp=share_link

Code to directly use in colab
```
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"

```




## Topic 17

### `Q-6:` Make a dataframe of each team in IPL with details like - Team Name, Matches Played, Win%, Home Win%, Away Win%.
Show sorted dataframe on Win%

Replace old team name as new name before performing any tasks.
```
Delhi Daredevils ->Delhi Capitals
Kings XI Punjab -> Punjab Kings
Rising Pune Supergiants -> Rising Pune Supergiant
```

Note: Team1 represents Home team. Exclude not result matches.


## Code Cell 18

```python
# code here
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)
changed_name = {'Delhi Daredevils':'Delhi Capitals',
                'Kings XI Punjab':'Punjab Kings',
                'Rising Pune Supergiants':'Rising Pune Supergiant'}
matches.replace(changed_name.keys(), changed_name.values(),inplace=True )
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
df = matches[~matches.WinningTeam.isna()]
new_df = pd.DataFrame()
teams = df.Team1.unique()
data = []
for team in teams:
    played = df[(df.Team1 == team) | (df.Team2 == team)].shape[0]
    wins = df[df.WinningTeam == team].shape[0]
    home_win = df[(df.WinningTeam == team) | (df.Team1 == team)].shape[0] / df[df.Team1 == team].shape[0] * 100
    away_win = df[(df.WinningTeam == team) | (df.Team2 == team)].shape[0] / df[df.Team2 == team].shape[0] * 100
    data.append([team, played, wins/played*100, home_win, away_win])
new_df[["Team", "Matches Played", "Win Percentage", "Home Win Percentage", "Away Win Percentage"]] = data
new_df.sort_values("Win Percentage", inplace=True, ascending=False)
new_df
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 20

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 21

### `Q-7:` Venues with most "no result" matches.

## Code Cell 22

```python
# code here
matches[matches.WonBy == "NoResults"].Venue.value_counts().index[0]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

### `Q-8:` Player with most appearance in final match.

`Team1Players` and `Team2Players` have all players name. It is not a list of players name instead it is str. So handle it as string.

Hint: split and strip will help; Make a series of all players in final and do value counts


## Code Cell 24

```python
# code here

def getPlayers(l):
    return pd.Series(list(map( lambda x: x.strip("'"), l.lstrip("'[").rstrip("]'").split(", "))))

df_final = matches[matches["MatchNumber"] == "Final"]
playerSeries = pd.Series()
for player_list in df_final.Team1Players:
    x = getPlayers(player_list)
    playerSeries = playerSeries.append(x)
for player_list in df_final.Team2Players:
    x = getPlayers(player_list)
    playerSeries = playerSeries.append(x)
playerSeries.value_counts().head()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 25

### `Q-9:` IPL Point Table

Make a function `point_table` which take `season` as parameter and show points table in non-ascendng order of points and in ascending order of team name.

For winning - 2 Ponits;
For loosing - 0 Point
For not result both team gets 1 points.

Make dataframe which will have
`TeamName` `MatchesPlayed` `MatchesWon` `NoResult` `Points`
make `TeamName` as index.

```
season parametr should be one of these->
['2022', '2021', '2020/21', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2009/10', '2009', '2007/08']
```


## Topic 26

Output of two Top 2 in season 2022
```
TeamName    MatchesPlayed	MatchesWon	NoResult	Points

Gujarat Titans	    16	   12	       0	     24
Rajasthan Royals	  17	   10	       0	     20

```

## Code Cell 27

```python
# code here
def matches_played(df, team):
    return df[(df.Team1 == team) | (df.Team2 == team)].shape[0]
def matches_won(df, team):
    return df[df.WinningTeam == team].shape[0]
def matches_no_result(df, team):
    return df[((df.Team1 == team) | (df.Team2 == team)) & (df.WinningTeam.isnull())].shape[0]

def point_table(season):
    df = matches[matches.Season == season]
    new_df = pd.DataFrame()
    new_df['Team Name'] = df.Team1.unique()
    new_df["Matches Played"] = new_df["Team Name"].apply(lambda x: matches_played(df, x))
    new_df["Matches Won"] = new_df["Team Name"].apply(lambda x: matches_won(df, x))
    new_df["No Result"] = new_df["Team Name"].apply(lambda x: matches_no_result(df, x))
    new_df["Points"] = new_df["Matches Won"]*2 + new_df["No Result"]
    new_df.sort_values("Points", ascending = False, inplace=True)
    new_df.set_index("Team Name", inplace=True)
    return new_df
point_table("2022")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 28

### `Q-10:` IPL Point Table cont.
Extend the above IPL Point Table with an extra column as `SeasonPosition`

Team below top 4 after sorting on `Points` and then on `TeamName` Will have same `SeasonPosition` as there rank. use rank function.

Teams in Top four will have `SeasonPosition` as:
```
    'Winner' - Team won final
    'Runner' - Team lost Final
    3 - Losing Team in Qualifier2
    4 - Losing Team in Eliminator
```

For changing value of pariticular cell use `df.at[row_index, col_label] = value`

Output of two Top 2 in season 2022. Your result should have all teams.
```
TeamName    MatchesPlayed	MatchesWon	NoResult	Points   SeasonPosition

Gujarat Titans	    16	   12	       0	     24         Winner
Rajasthan Royals	  17	   10	       0	     20         Runner

```

Note: If you try to chnage value of view of any dataframe a warnig will be shown. To avoid it, make a copy of the dataframe you want to change in by `df.copy()`

## Code Cell 29

```python
# code here
def point_table_extension(season):
    df3 = point_table(season)
    df = matches[matches.Season == season].copy()
    df3["SeasonPosition"] = df3.Points.rank(ascending=False, method= 'first').astype('object')
    df["LoosingTeam"] = df[df.WinningTeam == df.Team1]["Team2"].append(df[df.WinningTeam == df.Team2]["Team1"])
    final = df[df["MatchNumber"] == "Final"]
    wining_team = final.WinningTeam.values[0]
    runner = final.LoosingTeam.values[0]
    df3.at[wining_team, "SeasonPosition"]="Winner"
    df3.at[runner, "SeasonPosition"]="Runner"
    q = df[df["MatchNumber"] == "Qualifier 2"]
    e = df[df["MatchNumber"] == "Eliminator"]
    third = q.LoosingTeam.values[0]
    fourth = e.LoosingTeam.values[0]
    df3.at[third, "SeasonPosition"] = "Third"
    df3.at[fourth, "SeasonPosition"] = "Fourth"
    return df3
point_table_extension("2022")

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 30

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

