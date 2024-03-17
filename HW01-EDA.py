# -*- coding: utf-8 -*-
"""김주송 - HW01-EDA의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FZIoU_N5CTXsZorCYSDsLHvwiv6ED80h

# HW01. Exploratory Data Analysis

Your task is to complete the codes marked with "To Do" from T1 to T5.

## Titanic dataset

Seaborn에 포함된 토이 데이터셋 중 타이타닉 데이터셋을 사용한다. 아래 코드를 통해서 데이터셋을 로딩한다.

Here we use a toy dataset included in Seaborn.
You can load the dataset with the following codes.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')

"""아래 코드를 실행해보면 로드된 데이터의 타입이 Pandas DataFrame인 것을 확인할 수 있다.

You can see the data type of the dataset is Pandas DataFrame with the following code.
"""

type(titanic)

"""데이터셋의 크기를 확인해보자.

Let's check the size of the dataset.

"""

titanic.shape

"""891개의 행과 15개의 열로 이뤄진것을 확인하였다. 타이타닉 데이터셋이 어떤 내용을 포함했는지 처음 열개의 행을 출력해보자.

There are 891 rows and 15 columns in the dataset. You can check the content of the first 10 rows with the code below.

"""

titanic.head(10)

"""위에 출력된 테이블을 통해서 각 열의 데이터 타입을 유추해보고, 아래 코드를 실행해서 확인해보자. int64, float64로 표기된 열은 수치형 자료이고, object, category, bool은 범주형 자료임을 알 수 있다. 일부 열은 범주형 자료가 수치형으로 저장된 것을 확인할 수 있다.


You might want to check the data type of each column. Execute the code below. There are numerical data marked with [int64], [float64], and categorical data marked with [object], [category], [bool]. You may notice some of the categorical data are saved in numerical data types.


[참조: titatnic dataset description](https://data.world/nrippner/titanic-disaster-dataset)

[참조: pandas dtype](https://pbpython.com/pandas_dtypes.html)
"""

titanic.dtypes

"""수치형 자료의 경우 아래 코드를 통해서 기초통계량을 확인해 볼 수 있다.

With the following code, you can generate descriptive statistics for numerical data.
"""

titanic.describe()

"""데이터셋의 전체 행 갯수가 891인데 일부 변수들은 count가 891보다 작은 것으로 보아 일부 값이 누락되었음을 확인할 수 있다. head()로 출력한 테이블에서 NaN으로 표기된 값들이 누락된 값들이다. 테이블에 계산된 평균, 표준편차 등은 누락된 값을 제외하고 계산한 값이다. info() 메소드를 사용하면 모든 변수들에 대한 dtype과 count를 확인할 수 있다.

See the count row at the top. Data counts of some columns are less than 891, from which we can guess there are some missing values. Recall the output of the head() function, missing values are marked with NaN. Descriptive statistics (mean, std, etc.) above are calculated with missing values omitted. With the info() method you can check dtype and count of all variables (columns).
"""

titanic.info()

"""확인해보니 deck에는 누락된 값이 너무 많다. 제거하자.

hmm... deck has too many missing values. let's remove the column deck.

"""

titanic.drop('deck', inplace=True, axis=1)
titanic.info()

"""## T1. Create a frequency distribution table
We are wondering about the ratio of men and women aboard the Titanic. Let's make a frequency distribution table using the [crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html) method.
"""

## To Do

table = pd.crosstab(index=titanic["sex"].values, colnames=["sex"], columns='frequency')
table.index = ["female", "male"]
print(table)
table

"""간단히 빈도를 확인할때는 crosstab보다 value_counts 메소드가 더 적합하다.

You may check it with value_counts() methods instead of the crosstab method.
"""

titanic["sex"].value_counts()

titanic["survived"].value_counts()

titanic["class"].value_counts().sort_index()

titanic["embark_town"].value_counts().sort_index()

"""대략 남자가 더 많이 탔고, 과반수 이상이 사망했으며, 2등객실 승객이 가장 적었고, Southampton에서 대다수의 승객이 탑승한 것을 확인할 수 있다.

From the steps above, we can notice that there were more men on board and more than half of the passengers were dead, and the Second class has the lowest number of passengers, the majority of passengers were embarked at Southampton.

## T2. 파이차트
한눈에 남녀 비율을 파악하고 싶다.
아래 그림 처럼 파이차트를 출력하는 코드를 작성해 보자.

Now, you want to check the ratio of men and women with the pie chart.
Complete code to generate a pie chart similar to the one below.



![picture](https://drive.google.com/uc?id=1-SnmdWshpBsnZAlBkVNp02PZQj2mUuDd)
"""

## To Do

table2 = pd.crosstab(index=titanic["sex"].values, colnames=["sex"], columns='Sex')
table2.index = ["Female", "Male"]
table2.plot.pie(y="Sex", autopct='%0.1f%%', legend=None)
plt.show()

#오류있는 방법(대문자 아님)
#titanic["sex"].value_counts().sort_index().plot(kind="pie", autopct="%.1f%%")
#plt.show()

"""
영화 타이타닉에서 아이들과 여성들을 먼저 구명보트에 태우는 장면이 있었다. 정말 그랬었는지 확인해보자. 우선 아이와 어른으로 그룹을 나눠서 확인해보자.

두개의 시리즈를 이용해서 DataFrame을 만들 수 있다. 생성된 DataFrame을 df라고 할때, df.T 를 통해서 Transpose된 데이터셋에 접근할 수 있다. df.index를 인덱스 이름을 df.columns를 이용해서 열 이름을 변경할 수 있다.

If you watched the movie Titanic, you might remember the scene in which women and children were evacuated to the rescue boats first. Let's check if that was true.
First, you may want to make two data series, each representing adults and children.
With those two series, you can construct DataFrame.
Let df be the created DataFrame, you can transpose the DataFrame by df.T or change the names by df.index or df.columns.
See the below code."""

child = titanic[titanic['who']=='child']['survived'].value_counts()
adult = titanic[titanic['who']!='child']['survived'].value_counts()
df = pd.DataFrame([child, adult])
df.index = ['child', 'adult']
df.columns = ['died', 'survived']
print(df)

"""아래와 같은 파이차트를 그려보자.

Let's draw a piechart similar to the one below.

![picture](https://drive.google.com/uc?id=1-XTGHMrTMEuCBU_kyFxQT0LB0IiPmIPv)

[참조: pandas visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
"""

## To Do

df = df.transpose()
df.plot.pie(subplots=True, figsize=(8,4))

"""파이차트로 그려보니 아이들의 생존율이 어른보다 약간 더 높아 보인다.
동일하게 성별 별로 그려보면 아래와 같은 파이차트를 얻을 수 있다.
아래 차트를 보면 남녀별로 생존율에 큰 차이를 볼 수 있다.

You can see survival rate of children is slightly higher than that of adults.
Similarly, if you draw a piechart for each gender, you can see the difference in the survivor ratio.

![picture](https://drive.google.com/uc?id=1-XwC8SVyMsdJXGQVZUFRk67UhwMYiRSY)

## T3. 막대그래프

위 파이차트로 생존/사망자의 남녀별 비율을 확인해보았다.
이번엔 각 성별 별 전체 탑승인원에 생존자 수를 보여주는 누적 막대 그래프를 아래와 같이 그려보자.

Now let's use stacked bar charts to show the number of passengers and the survivor ratio for each gender.  

![picture](https://drive.google.com/uc?id=1-UEmDC3lpBkkMhkXiNeK0S60Vn8FIWOW)
"""

male = titanic[titanic['sex']=='male']['survived'].value_counts()
female = titanic[titanic['sex']=='female']['survived'].value_counts()

## To Do

df2 = pd.DataFrame([male,female],index=['male','female'])
df2.columns = ['died','survived']
df2.plot.bar(stacked=True, rot=0)
plt.show()

"""위 누적 막대그래프로


*   승객 중 남자가 많았음.
*   여성 승객이 더 많이 생존했음.
*   남성 승객은 생존자보다 사망자가 많았음.

등을 확인할 수 있다.

From the stacked bar graphs above, we can tell the followings.
* There were more men passengers than women passengers.  
* Survived women outnumbers survived men.
* With regards to the male passengers, there were more dead than survivors.

## T4. Box plots

위에 head로 살펴본 데이터에서 이상한 점이 발견되었다. 같은 등급객실임에도 지불한 가격이 다르다.
객실별 가격을 아래처럼 Box plot으로 그려보자.

You noticed that the fares were different even within the same class.
Use box plots to show the fares for each class.


![picture](https://drive.google.com/uc?id=1-Zj4MjHnoKeQ6wXzXn2KEWL_eXbPvDny)
"""

## To Do

boxplot = sns.boxplot(data=titanic, x='class', y='fare')

"""## T5. Scatter plot

혹시 나이와 요금간에 상관관계가 있나 객실별로 아래와 같이 scatter plot을 그려보자.

You may guess age and the fare might be related.
Draw a scatter plot similar to the one shown below.


![picture](https://drive.google.com/uc?id=1-_pfgqoVwshU6GpdTdGz8Nm_34uUus6K)


"""

## To Do

sns.scatterplot(x='age', y='fare', hue='class', style='class', data=titanic)
plt.show()

"""It seems age and fares are not related.

"""