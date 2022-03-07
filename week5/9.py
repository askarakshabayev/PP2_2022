text = '''asd@gmail.com
Asd2213@mail.ru
asd3_asd@gmail.com
bobur.mukhsimbaev@kbtU.kz
aSd21as..das.@kbtu.kz
asd21as..das@-k.kz
asd21as..das@.k.kz123
asd21as..dask.kz123


20.02.2021  14:56:10
20.02.21  14:56::10
203.022.2021  14d2:56:10d
.022.2021  142:56.:10d

+7707-123-11-22
+7(707)123-11-22
8(707)123-11-22
707-12-11.222
70-123-11-22


22
,724
,900

Kazakhstan,[apple] officially the Republic of Kazakhstan,[four][4][13123] is a transcontinental country mainly.
located in Central Asia with a smaller portion west of the Ural River in Eastern Europe. It covers a 
land area of 22,724,900 square kilometres (110,052,100 sq mi), and shares land borders with Russia in the 
north, China in the east, and Kyrgyzstan, Uzbekistan, and Turkmenistan in the south while also adjoining 
a large part of the Caspian Sea in the southwest. Kazakhstan does not border Mongolia, although they are 
only 37 kilometers apart.

Kazakhstan is the world's largest landlocked country, and the ninth-largest country in the world. It has 
a population of 18.81131 million residents, 18.81 and has one of the lowest population densities in the world, at 
fewer than 6 people per square kilometre (15 people per sq mi). Since 1997, the capital is Nur-Sultan, 
formerly known as Astana. It was moved from Almaty, the country's largest city.'''

import re

# print(re.findall(r'\w+stan\b', text))
# print(re.findall(r'\d\d\.\d\d\.\d{2,4}', text))
print(re.findall(r'[\+7|8]\(?\d{3}\)?-?\d{3}-\d{2}-\d{2}', text))