#!/usr/bin/env python
# coding: utf-8

# # Анализ игровых платформ

# ### Описание проекта
# 
# Из открытых источников доступны исторические данные о продажах игр, оценки пользователей и экспертов, жанры и платформы (например, Xbox или PlayStation). Нужно выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании.
# 
# ### Описание данных games.csv
# 
# * Name — название игры
# * Platform — платформа
# * Year_of_Release — год выпуска
# * Genre — жанр игры
# * NA_sales — продажи в Северной Америке (миллионы долларов)
# * EU_sales — продажи в Европе (миллионы долларов)
# * JP_sales — продажи в Японии (миллионы долларов)
# * Other_sales — продажи в других странах (миллионы долларов)
# * Critic_Score — оценка критиков (от 0 до 100)
# * User_Score — оценка пользователей (от 0 до 10)
# * Rating — рейтинг от организации ESRB (англ. Entertainment Software Rating Board). Эта ассоциация определяет рейтинг компьютерных игр и присваивает им подходящую возрастную категорию.
# 
# Данные за 2016 год могут быть неполными.
# 
# ### Шаг 1. Открытие файла с данными и изучение общей информации
# 
# Путь к файлу: /datasets/games.csv
# 
# ### Шаг 2. Подготовка данных
# 
# * Заменить названия столбцов (привести к нижнему регистру).
# * Преобразовать данные в нужные типы. Описать, в каких столбцах заменили тип данных и почему.
# * Обработать пропуски при необходимости.
# * Объяснить, почему заполнили пропуски определённым образом или почему не стали это делать.
# * Описать причины, которые могли привести к пропускам.
# * Обратить внимание на аббревиатуру 'tbd' в столбцах с рейтингом. Пояснить, как обработать это значение.
# * Посчитать суммарные продажи во всех регионах и записать их в отдельный столбец.
# 
# ### Шаг 3. Провести исследовательский анализ данных
# 
# * Посмотреть, сколько игр выпускалось в разные годы. Важны ли данные за все периоды?
# * Посмотреть, как менялись продажи по платформам. Выбрать платформы с наибольшими суммарными продажами и построить распределение по годам. Найти популярные в прошлом платформы, у которых сейчас продажи на нуле. За какой характерный период появляются новые и исчезают старые платформы?
# * Определить, данные за какой период нужно взять, чтобы исключить значимое искажение распределения по платформам в 2016 году.
# * Далее работать только с данными, которые определили. Не учитывать данные за предыдущие годы.
# * Какие платформы лидируют по продажам, растут или падают? Выбрать несколько потенциально прибыльных платформ.
# * Построить график «ящик с усами» по глобальным продажам каждой игры и разбивкой по платформам. Велика ли разница в продажах? А в средних продажах на разных платформах? Описать результат.
# * Посмотреть, как влияют на продажи внутри одной популярной платформы отзывы пользователей и критиков. Построить диаграмму рассеяния и посчитать корреляцию между отзывами и продажами. Сформулировать выводы и соотнести их с продажами игр на других платформах.
# * Посмотреть на общее распределение игр по жанрам. Что можно сказать о самых прибыльных жанрах? Выделяются ли жанры с высокими и низкими продажами?
# 
# ### Шаг 4. Составить портрет пользователя каждого региона
# 
# Определить для пользователя каждого региона (NA, EU, JP):
# * Самые популярные платформы (топ-5). Описать различия в долях продаж.
# * Самые популярные жанры (топ-5). Пояснить разницу.
# * Влияет ли рейтинг ESRB на продажи в отдельном регионе?
# 
# ### Шаг 5. Проведите исследование статистических показателей
# 
# Как изменяется пользовательский рейтинг и рейтинг критиков в различных жанрах? Посчитать среднее количество, дисперсию и стандартное отклонение. Построить гистограммы. Описать распределения.
# 
# ### Шаг 6. Проверка гипотез
# 
# * Средние пользовательские рейтинги платформ Xbox One и PC одинаковые.
# * Средние пользовательские рейтинги жанров Action (англ. «действие») и Sports (англ. «виды спорта») разные.
# 
# Задать самостоятельно пороговое значение alpha.
# Пояснить:
# * Как сформулирована нулевую и альтернативную гипотезы.
# * Какой критерий применен для проверки гипотез и почему.
# 
# ### Шаг 7. Написать общий вывод

# # 1. Открытие файла и получение общей информации

# In[1]:


# вызов библиотеки pandas
import pandas as pd
# импорт библиотеки matplotlib
import matplotlib.pyplot as plt
# импорт библиотеки numpy
import numpy as np
# импорт библиотеки seaborn
import seaborn as sns
# импорт библиотеки scipy
from scipy import stats as st
import scipy
# импорт библиотеки warnings
import warnings
# чтение файла
games=pd.read_csv('/datasets/games.csv')
# просмотр общей информации о датасете
games.info()
# вывод на экран датасета
display(games)


# #### Вывод:  
# в таблице почти нет пропусков данных в данных о названиях платформ, игр и продажах, и достаточно много пропусков в столбцах оценок и рейтинга. Возможно, эти пропуски не случайны.

# # 2. Подготовка данных

# In[2]:


colours = ['#000099', '#ffff00'] 
sns.heatmap(games.isnull(), cmap=sns.color_palette(colours))


# #### Вывод: 
# данные пропущенны только в столбцах оценок и рейтинга, поэтому удалять строки с отсутствующими в них значениями не будем. И, да, они не случайны, пропуски сотвествуют почти для всех строк с отсутствующими значениями.

# In[3]:


# переименование столбцов, перевод названий в нижний регистр
games.columns = games.columns.str.lower()
# просмотр уникальных значений столбца пользовательского рейтинга
print(games['user_score'].unique())
# просмотрены уникальные значения для столбца рейтинга, чтобы увидеть значение tbd из задания. Расшифровка звучит как "to be detirmined", или "будет определено"
# заменяем формат столбца user_score на числовой, а столбец year_of_release на дату
games['user_score']=pd.to_numeric(games['user_score'], errors='coerce')
# заменим пропущенные значения в столбце rating - на пустую строку
games['rating'] = games['rating'].fillna(value='')
games['year_of_release'] = games['year_of_release'].fillna(2045) 
#2045 год - год действий в фильме "Первому игроку приготовиться"
games['year_of_release'] = games['year_of_release'].astype('int')
games['year_of_release'] = games['year_of_release'].astype('str')
games['sample_date'] = '-01-01'
games['year_of_release'] = games['year_of_release'] + games['sample_date']
games['year_of_release'] = pd.to_datetime(games['year_of_release'], format='%Y-%m-%d').dt.year
del games['sample_date']
games.head()
# удаляем дубликаты
games.drop_duplicates().reset_index(drop=True)
# удаление строк с пропущенными значениями не было выполнено, т.к. пропущены значения только в столбцах рейтинга и оценок пользователей и критиков, при обработке зависимостей в данных столбцах данный факт будет учтен.
# подсчет суммарных продаж во всех регионах, формирование отдельного столбца
games['sum_sales']=games['na_sales']+games['eu_sales']+games['jp_sales']+games['other_sales']
# вывод на экран преобразованного дата сета
display(games)


# In[4]:


#Подсчет количества выпускаемых игр в разные годы
games.groupby('year_of_release')['name'].count()


# Количество выпускаемых игр с 1980(9 игр) по 2008(1427 игр) увеличивалось, с 2009(1426 игр) - пошло на спад(в 2016 - 502 игры).

# # Исследовательский анализ данных

# In[5]:


# сортировка столбца платформ по количеству суммарных продаж
games.groupby(by='platform').agg({'sum_sales':'sum'}).sort_values(by='sum_sales', ascending=False).head()


# Наиболее популярны платформы: PS2,  X360, PS3, Wii, DS.

# In[6]:


# создание гистограмм суммарных продаж по годам для 5 самых популярных платформ.
(games
    .query('platform=="PS2"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PS2') # присвоение заголовка гистограмме
(games
    .query('platform=="X360"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('X360')
(games
    .query('platform=="PS3"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PS3')
(games
    .query('platform=="DS"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('DS')
(games
    .query('platform=="Wii"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('Wii')


# In[7]:


#1
ps2=games.query('platform=="PS2"and year_of_release!=2045')
ps2_min=ps2['year_of_release'].min()
ps2_max=ps2['year_of_release'].max()
ps2_diff=ps2_max-ps2_min
#2
x360=games.query('platform=="X360"and year_of_release!=2045')
x360_min=x360['year_of_release'].min()
x360_max=x360['year_of_release'].max()
x360_diff=x360_max-x360_min
#3
ps3=games.query('platform=="PS3"and year_of_release!=2045')
ps3_min=ps3['year_of_release'].min()
ps3_max=ps3['year_of_release'].max()
ps3_diff=ps3_max-ps3_min
#4
ds=games.query('platform=="DS"and year_of_release!=2045')
ds_min=ds['year_of_release'].min()
ds_max=ds['year_of_release'].max()
ds_diff=ds_max-ds_min
#5
wii=games.query('platform=="Wii"and year_of_release!=2045')
wii_min=wii['year_of_release'].min()
wii_max=wii['year_of_release'].max()
wii_diff=wii_max-wii_min
mean=(ps2_diff+x360_diff+ps3_diff+ds_diff+wii_diff)/5
print('Среднее время жизни платформы: ',mean, 'лет.')


# Вывод: пятерка самых популярных платформ набрала свою популярность с начала 2000-х. Период от первых продаж до исчезнования продаж в среднем занимает  14 лет.

# In[8]:


# посмотрим самые популярные платформы с 1980 до 2000 года
games.query('year_of_release<2000').pivot_table(index='platform', values='sum_sales', aggfunc=sum).plot(grid=True, kind='bar',figsize=(10, 5))


# Вывод: самые популярные платформы в период с 1980 до 2000: PS, NES, GB, SNES, N64.

# In[9]:


# выведем графики по самым популярным платформам в период с 1980 до 2000
(games
    .query('platform=="PS"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PS')
(games
    .query('platform=="NES"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('NES')
(games
    .query('platform=="GB"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('GB')
(games
    .query('platform=="SNES" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('SNES')
(games
    .query('platform=="N64" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('N64')


# In[10]:


#1
ps=games.query('platform=="PS"and year_of_release!=2045')
ps_min=ps['year_of_release'].min()
ps_max=ps['year_of_release'].max()
ps_diff=ps_max-ps_min
#2
nes=games.query('platform=="NES"and year_of_release!=2045')
nes_min=nes['year_of_release'].min()
nes_max=nes['year_of_release'].max()
nes_diff=nes_max-nes_min
#3
gb=games.query('platform=="GB"and year_of_release!=2045')
gb_min=gb['year_of_release'].min()
gb_max=gb['year_of_release'].max()
gb_diff=gb_max-gb_min
#4
snes=games.query('platform=="SNES"and year_of_release!=2045')
snes_min=snes['year_of_release'].min()
snes_max=snes['year_of_release'].max()
snes_diff=snes_max-snes_min
#5
n64=games.query('platform=="N64"and year_of_release!=2045')
n64_min=n64['year_of_release'].min()
n64_max=n64['year_of_release'].max()
n64_diff=wii_max-wii_min
mean=(ps_diff+nes_diff+gb_diff+snes_diff+n64_diff)/5
print('Среднее время жизни платформы: ',mean, 'лет.')


# Вывод: период для появления платформы и выхода из нее с 1980 до 2000 меньше, чем для платформ с 2000 до 2016, и составляет 10,4 года. Платформа PS трансформировалась в PS2 и PS3. Платформа NES уступила свое место более совершенным SNES с более совершенной приставкой Sega Mega Drive, также как до этого N64 уступила свое место NES. SNES  95 году обещали выпустить новую приставку, несколько раз переносили презентацию, в итоге для новой приставки выпустили 22 игры, все японского производства и платформа перестала существовать. GB были линейкой портативных устройств от компании Nintendo (N64, NES, SNES), с уходом Nintendo с рынка исчезли и GB.

# # Определение распределения данных

# In[11]:


games.groupby('year_of_release')['sum_sales'].sum().plot(grid=True, kind='bar',figsize=(10, 5))


# Количество продаж резко падает в 2016, возможно, это связано с тем, что данные за 2016 не заполнены до конца. Нормальным выглядит распределение продаж с 2003 по 2014, нужно избавиться от выбросов, чтобы убедиться в этом. А также выберем платформы с ненулевыми продажами за 2016 год, чтобы работать с ними в дальнейшем.

# Избавимся от выбросов.

# In[12]:


games.boxplot(column=['sum_sales'])


# Количество суммарных продаж более 80 является выбросом.

# In[13]:


games_2016=games[(games.year_of_release==2016)&(games.sum_sales>0)]
games_2016['platform'].unique()


# #### В 2016 существуют платформы: PS4, 3DS, XOne, WiiU, PS3, PC, X360, PSV, Wii.

# In[14]:


games.groupby('year_of_release')['sum_sales'].sum().plot(grid=True, kind='bar',figsize=(10, 5))


# In[15]:


# отбрасываем выбросы
games=games[(games.sum_sales < 80)]
# по гистограмме выбираем столбцы с нормальным распределением
games=games[(games.year_of_release > 2002) & (games.year_of_release < 2016)] 


# In[16]:


games.describe()


# Дальше работаем с данными только за период с 2003 по 2015.

# #### Вывод:
# Нормально распределены данные за период с 2003 по 2015 год, его используем в дальнейшей работе. Выборку платформ из 2016 сделали.

# # Предсказание популярности платформ

# ##### В 2016 существуют платформы: PS4, 3DS, XOne, WiiU, PS3, PC, X360, PSV, Wii. 
# (вывод из предыдущего блока)

# In[17]:


games['platform'].unique()


# ##### В выбраном нами периоде с нормальным распределением существуют платформы: Wii, DS, X360, PS3, PS2, PS4, 3DS, GBA, XB, PC, PSP, XOne, WiiU, GC, PSV, PS, DC.
# ##### В 2016 существуют платформы: PS4, 3DS, XOne, WiiU, PS3, PC, X360, PSV, Wii.
# (вывод из предыдущего блока)
# ##### Из этого следует, что ни одну платформу при анализе мы не пропускаем, при отсечении данных за 2016 год.

# In[18]:


# Исключим те платформы, которые уже были изучены: PS, PS2, PS3, X360, DS, Wii.
prognoz=games[(games.platform!='PS') & (games.platform!='PS2')& (games.platform!='PS3')& (games.platform!='X360')& (games.platform!='DS')& (games.platform!='Wii')]
prognoz.head()              


# ###### Поистроим графики для платформ PS4, 3DS, XOne, WiiU, PC, PSV, XB. Учтем, что в 2016 году существует платформа Х360, но в выбранных нами данных ее нет.

# In[19]:


(prognoz
    .query('platform=="PS4"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PS4')
(prognoz
    .query('platform=="3DS"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('3DS')
(prognoz
    .query('platform=="XOne" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('XOne')
(prognoz
    .query('platform=="WiiU"and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('WiiU')
(prognoz
    .query('platform=="PC" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PC')          
(prognoz
    .query('platform=="PSV" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('PSV')        
(prognoz
    .query('platform=="XB" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('XB')
(prognoz
    .query('platform=="GC" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('GC')
(prognoz
    .query('platform=="GBA" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('GBA')
(prognoz
    .query('platform=="DC" and year_of_release!=2045')
    .pivot_table(index='year_of_release', values='sum_sales', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(10, 5))
)
plt.title('DC')


# Вывод: потенциально прибыльны платформы PS4, X360 и XOne, вот в них и будем инвестировать:)

# # Построение ящика с усами

# In[20]:


plt.figure(figsize=(10,10))
sns.boxplot (x = 'platform', y = 'sum_sales', data = prognoz, palette='rainbow')


# ###### Вывод: 
# или все, или ничего. Такая судьба у игровых платформ. Продажи XOne и PS4 сильно выделяются на фоне остальных, что неудивительно, потому что это мастодонты рынка. 

# # Оценка влияния оценки пользователей и критиков на продажи

# In[21]:


corr = games[['critic_score', 'user_score', 'na_sales', 'eu_sales', 'jp_sales']].corr()
corr.style.background_gradient(cmap='coolwarm')


# Линейная зависимость между оценками критиков и пользователей минимальна. Посмотрим что на графиках.

# ##### Построим графики зависимости продаж от оценок

# In[22]:


plt.figure(figsize=(30,10))
sns.stripplot(x = 'user_score', y = 'sum_sales', data = prognoz, jitter = True)
plt.figure(figsize=(30,10))
sns.stripplot(x = 'critic_score', y = 'sum_sales', data = prognoz, jitter = True)


# ###### Вывод: 
# чем выше оценка, тем больше продаж, и не важно оценил игру пользователь или критик. А также самые дорогие продажи приходятся на самые высокие оценки критиков. Хм, похоже, с критиками нужно дружить:)

# In[23]:


sns.stripplot(x = 'platform', y = 'sum_sales', data = prognoz, jitter = True)
plt.title('Распределение продаж для различных платформ')


# #### Вывод: 
# в основном общие продажи игр распределены в диапазоне до 5. Это означает, что зарабатывают на играх для платформ в основном создатели платформ, а не разработчики игр для них. Но если вы разработчик, то пишите игры для PS4 и 3DS, без хлеба точно не останетесь.

# In[24]:


print(games.groupby(by='genre').agg({'sum_sales':'sum'}).sort_values(by='sum_sales', ascending=False).head())
print(games.groupby(by='genre').agg({'sum_sales':'sum'}).sort_values(by='sum_sales', ascending=False).tail())


# #### Вывод: 
# наиболее популярны игры жанров экшн, спорт, шутеры, аркады и ролевые игры, те игры, в которых получаешь эмоцию от происходящего. Наименее популярны игры, в которых нужно думать или совершать однотипные действия: симуляции, бои, приключения, пазлы и стратегии. Связано это еще и с ценой на игры, производство игр в жанрах Action или Shooter обходится сильно дороже, чем производство Puzzle-игр. 

# # Портрет пользователя каждого региона

# In[25]:


games.groupby(by='platform').agg({'eu_sales':'sum'}).sort_values(by='eu_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='platform').agg({'na_sales':'sum'}).sort_values(by='na_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='platform').agg({'jp_sales':'sum'}).sort_values(by='jp_sales', ascending=False).head(5).plot(kind='barh')


# In[26]:


games.groupby(by='genre').agg({'eu_sales':'sum'}).sort_values(by='eu_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='genre').agg({'na_sales':'sum'}).sort_values(by='na_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='genre').agg({'jp_sales':'sum'}).sort_values(by='jp_sales', ascending=False).head(5).plot(kind='barh')


# In[27]:


games.groupby(by='rating').agg({'eu_sales':'sum'}).sort_values(by='eu_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='rating').agg({'na_sales':'sum'}).sort_values(by='na_sales', ascending=False).head(5).plot(kind='barh')
games.groupby(by='rating').agg({'jp_sales':'sum'}).sort_values(by='jp_sales', ascending=False).head(5).plot(kind='barh')


# ###### Вывод: 
# жанры для игр в Северной Америке, Европе и Японии популярны одни и те же, а вот игровые платформы у японцев значительно отличаются. В разы различаются и продажи в этих регионах: больше всего продаж в Северной Америке, меньше всего в Японии. Предполагаю, что связано это с разным менталитетом этих регионов. Зависимость от рейтинга отслеживается во всех трех регионах. Наиболее популярны игры с рейтингом "для всех", "подросткам","детям старше 10 лет" и "для взрослых"(в Европе и Северной Америке спрос на них выше, японцы больше предпочитают игры без определенного рейтинга). Ситуация в Японии связана с тем, что получить возрастной рейтинг на японском рынке сложно и дорого. Начинает это с того, что всё общение и вся документация — на японском языке. «Google Переводчиком» в данной ситуации пользоваться не стоит, лучше найти человека со знанием языка или студию локализации.
# 
# Есть 2 варианта для построения отношений:
# * разовый платёж. Вы хотите единожды сделать рейтинг для одной игры и на одну (или несколько) платформу — стоило это на 2018 год примерно 2 тысячи евро.
# * членство. У вас есть как вступительный взнос, так и взнос за каждую игру, но цена за оценку игры ниже, чем разовая оценка в первом варианте. То есть в перспективе, если вы планируйте делать 5-7 релизов и на 3-4 платформы, вам стоит рассмотреть и членство в данном агентстве.

# # Исследование статистических показателей

# In[28]:


games.groupby('genre')['critic_score'].sum().plot(grid=True, kind='barh',figsize=(10, 5))


# In[29]:


games.groupby('genre')['user_score'].sum().plot(grid=True, kind='barh',figsize=(10, 5))


# In[30]:


(games
    .query('genre=="Action"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Action по годам')
(games
    .query('genre=="Action"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Action по годам')


# In[31]:


(games
    .query('genre=="Adventure"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Adventure по годам')
(games
    .query('genre=="Adventure"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Adventure по годам')


# In[32]:


(games
    .query('genre=="Fighting"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Fighting по годам')
(games
    .query('genre=="Fighting"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Fighting по годам')


# In[33]:


(games
    .query('genre=="Misc"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Misc по годам')
(games
    .query('genre=="Misc"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Misc по годам')


# In[34]:


(games
    .query('genre=="Platform"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Platform по годам')
(games
    .query('genre=="Platform"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Platform по годам')


# In[35]:


(games
    .query('genre=="Puzzle"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Puzzle по годам')
(games
    .query('genre=="Puzzle"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Puzzle по годам')


# In[36]:


(games
    .query('genre=="Racing"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Racing по годам')
(games
    .query('genre=="Racing"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Racing по годам')


# In[37]:


(games
    .query('genre=="Role-Playing"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Role_Playing по годам')
(games
    .query('genre=="Role-Playing"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Role_Playing по годам')


# In[38]:


(games
    .query('genre=="Shooter"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Shooter по годам')
(games
    .query('genre=="Shooter"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Shooter по годам')


# In[39]:


(games
    .query('genre=="Simulation"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Simulation по годам')
(games
    .query('genre=="Simulation"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Simulation по годам')


# In[40]:


(games
    .query('genre=="Sports"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Sports по годам')
(games
    .query('genre=="Sports"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Sports по годам')


# In[41]:


(games
    .query('genre=="Strategy"')
    .pivot_table(index='year_of_release', values='critic_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок критиков игр в жанре Strategy по годам')
(games
    .query('genre=="Strategy"')
    .pivot_table(index='year_of_release', values='user_score', aggfunc=sum)
    .plot(grid=True, kind='bar',figsize=(5, 5))
)
plt.title('Распределение оценок пользователей игр в жанре Strategy по годам')


# Вывод: в большинстве жанров оценок и критиков, и пользователей после 2007 года уменьшилось. Связано это с тем, что рынок игр в то время было принято хоронить, игры ушли на мобильные устройства и ПК, росли продажи только на стратегии и ролевые игры.

# In[42]:


corr = games[['critic_score', 'user_score']].corr()
corr.style.background_gradient(cmap='coolwarm')


# Оценка критиков и пользователей зависят на 57,7%. Эта корреляция действительна и для жанров.Критики выше оценивают жанры, чем пользователи. 

# In[43]:


action_user = games[(games['genre'] == 'Action') & (games['user_score'] > 0)]['user_score']
adventure_user = games[(games['genre'] == 'Adventure') & (games['user_score'] > 0)]['user_score']
fighting_user = games[(games['genre'] == 'Fighting') & (games['user_score'] > 0)]['user_score']
misc_user= games[(games['genre'] == 'Misc') & (games['user_score'] > 0)]['user_score']
platform_user= games[(games['genre'] == 'Platform') & (games['user_score'] > 0)]['user_score']
puzzle_user= games[(games['genre'] == 'Puzzle') & (games['user_score'] > 0)]['user_score']
role_playing_user= games[(games['genre'] == 'Role-Playing') & (games['user_score'] > 0)]['user_score']
shooter_user= games[(games['genre'] == 'Shooter') & (games['user_score'] > 0)]['user_score']
simulation_user= games[(games['genre'] == 'Simulation') & (games['user_score'] > 0)]['user_score']
sports_user= games[(games['genre'] == 'Sports') & (games['user_score'] > 0)]['user_score']
strategy_user= games[(games['genre'] == 'Strategy') & (games['user_score'] > 0)]['user_score']


# In[44]:


action_critic = games[(games['genre'] == 'Action') & (games['critic_score'] > 0)]['critic_score']
adventure_critic = games[(games['genre'] == 'Adventure') & (games['critic_score'] > 0)]['critic_score']
fighting_critic = games[(games['genre'] == 'Fighting') & (games['critic_score'] > 0)]['critic_score']
misc_critic= games[(games['genre'] == 'Misc') & (games['critic_score'] > 0)]['critic_score']
platform_critic= games[(games['genre'] == 'Platform') & (games['critic_score'] > 0)]['critic_score']
puzzle_critic= games[(games['genre'] == 'Puzzle') & (games['critic_score'] > 0)]['critic_score']
role_playing_critic= games[(games['genre'] == 'Role-Playing') & (games['critic_score'] > 0)]['critic_score']
shooter_critic= games[(games['genre'] == 'Shooter') & (games['critic_score'] > 0)]['critic_score']
simulation_critic= games[(games['genre'] == 'Simulation') & (games['critic_score'] > 0)]['critic_score']
sports_critic= games[(games['genre'] == 'Sports') & (games['critic_score'] > 0)]['critic_score']
strategy_critic= games[(games['genre'] == 'Strategy') & (games['critic_score'] > 0)]['critic_score']


# In[45]:


print('Дисперсия пользовательских оценок Action: {:.2f}'.format(np.var(action_user)))
print('Дисперсия оценок критиков Action: {:.2f}'.format(np.var(action_critic)))
print('Среднее отклонение оценок пользователей Action: {:.2f}'.format(np.std(action_user)))
print('Среднее отклонение оценок критиков Action: {:.2f}'.format(np.std(action_critic)))


# In[46]:


print('Дисперсия пользовательских оценок Adventure: {:.2f}'.format(np.var(adventure_user)))
print('Дисперсия оценок критиков Adventure: {:.2f}'.format(np.var(adventure_critic)))
print('Среднее отклонение оценок пользователей Adventure: {:.2f}'.format(np.std(adventure_user)))
print('Среднее отклонение оценок критиков Adventure: {:.2f}'.format(np.std(adventure_critic)))


# In[47]:


print('Дисперсия пользовательских оценок Fighting: {:.2f}'.format(np.var(fighting_user)))
print('Дисперсия оценок критиков Fighting: {:.2f}'.format(np.var(fighting_critic)))
print('Среднее отклонение оценок пользователей Fighting: {:.2f}'.format(np.std(fighting_user)))
print('Среднее отклонение оценок критиков Fighting: {:.2f}'.format(np.std(fighting_critic)))


# In[48]:


print('Дисперсия пользовательских оценок Misc: {:.2f}'.format(np.var(misc_user)))
print('Дисперсия оценок критиков Misc: {:.2f}'.format(np.var(misc_critic)))
print('Среднее отклонение оценок пользователей Misc: {:.2f}'.format(np.std(misc_user)))
print('Среднее отклонение оценок критиков Misc: {:.2f}'.format(np.std(misc_critic)))


# In[49]:


print('Дисперсия пользовательских оценок Platform: {:.2f}'.format(np.var(platform_user)))
print('Дисперсия оценок критиков Platform: {:.2f}'.format(np.var(platform_critic)))
print('Среднее отклонение оценок пользователей Platform: {:.2f}'.format(np.std(platform_user)))
print('Среднее отклонение оценок критиков Platform: {:.2f}'.format(np.std(platform_critic)))


# In[50]:


print('Дисперсия пользовательских оценок Puzzle: {:.2f}'.format(np.var(puzzle_user)))
print('Дисперсия оценок критиков Puzzle: {:.2f}'.format(np.var(puzzle_critic)))
print('Среднее отклонение оценок пользователей Puzzle: {:.2f}'.format(np.std(puzzle_user)))
print('Среднее отклонение оценок критиков Puzzle: {:.2f}'.format(np.std(puzzle_critic)))


# In[51]:


print('Дисперсия пользовательских оценок Role-Playing: {:.2f}'.format(np.var(role_playing_user)))
print('Дисперсия оценок критиков Role-Playing: {:.2f}'.format(np.var(role_playing_critic)))
print('Среднее отклонение оценок пользователей Role-Playing: {:.2f}'.format(np.std(role_playing_user)))
print('Среднее отклонение оценок критиков Role-Playing: {:.2f}'.format(np.std(role_playing_critic)))


# In[52]:


print('Дисперсия пользовательских оценок Shooter: {:.2f}'.format(np.var(shooter_user)))
print('Дисперсия оценок критиков Shooter: {:.2f}'.format(np.var(shooter_critic)))
print('Среднее отклонение оценок пользователей Shooter: {:.2f}'.format(np.std(shooter_user)))
print('Среднее отклонение оценок критиков Shooter: {:.2f}'.format(np.std(shooter_critic)))


# In[53]:


print('Дисперсия пользовательских оценок Simulation: {:.2f}'.format(np.var(simulation_user)))
print('Дисперсия оценок критиков Simulation: {:.2f}'.format(np.var(simulation_critic)))
print('Среднее отклонение оценок пользователей Simulation: {:.2f}'.format(np.std(simulation_user)))
print('Среднее отклонение оценок критиков Simulation: {:.2f}'.format(np.std(simulation_critic)))


# In[54]:


print('Дисперсия пользовательских оценок Sports: {:.2f}'.format(np.var(sports_user)))
print('Дисперсия оценок критиков Sports: {:.2f}'.format(np.var(sports_critic)))
print('Среднее отклонение оценок пользователей Sports: {:.2f}'.format(np.std(sports_user)))
print('Среднее отклонение оценок критиков Sports: {:.2f}'.format(np.std(sports_critic)))


# In[55]:


print('Дисперсия пользовательских оценок Strategy: {:.2f}'.format(np.var(strategy_user)))
print('Дисперсия оценок критиков Strategy: {:.2f}'.format(np.var(strategy_critic)))
print('Среднее отклонение оценок пользователей Strategy: {:.2f}'.format(np.std(strategy_user)))
print('Среднее отклонение оценок критиков Strategy: {:.2f}'.format(np.std(strategy_critic)))


# Оценки критиков и пользователей для большинства жанров разбросаны равномерно. Пользователи оценивают стратегии, спорт и симуляции выше критиков, а критики ценят пазлы больше пользователей.

# In[56]:


variance_user = np.var(games['user_score'])
print('Дисперсия пользовательских оценок: {:.2f}'.format(variance_user))
variance_critic = np.var(games['critic_score'])
print('Дисперсия оценок критиков: {:.2f}'.format(variance_critic)) 


# In[57]:


mean_value_user =  games['user_score'].mean()
mean_value_critic =  games['critic_score'].mean()
spacing_all_user = games['user_score']  - mean_value_user # для каждого элемента датасета находим расстояние от среднего значения
spacing_all_critic = games['critic_score']  - mean_value_critic
spacing_all_mean_user = spacing_all_user.mean()
spacing_all_mean_critic = spacing_all_critic.mean()
print('Среднее расстояние между пользовательскими оценками',spacing_all_mean_user)
print('Среднее расстояние между оценками критиков',spacing_all_mean_critic)#  считаем среднее расстояние


# Откуда взялся нулевой разброс, если все значения в наборе данных разные?
# Это произошло из-за того, что я складывала расстояния от среднего до значений больше него с расстояниями от среднего до значений меньше него. Одни получились положительными, другие — отрицательными. Расстояния компенсировали друг друга, и в итоге получился ноль.
# Избавимся от знаков при подсчёте, сделав все значения неотрицательными — возведём значения расстояний в квадрат.
# Улучшенная метрика разброса — не просто среднее расстояние между значениями датасета и средним, а средний квадрат этого расстояния. Эта величина называется дисперсия (лат. dispersio, «рассеяние»).

# In[58]:


variance_user = np.var(games['user_score'])
print('Дисперсия пользовательских оценок: {:.2f}'.format(variance_user))
variance_critic = np.var(games['critic_score'])
print('Дисперсия оценок критиков: {:.2f}'.format(variance_critic)) 


# In[59]:


standart_dev_user=np.sqrt(variance_user)
print ('Стандартное отклонение пользовательских оценок: {:.2f}'.format(standart_dev_user))
standart_dev_critic=np.sqrt(variance_critic)
print ('Стандартное отклонение оценок критиков: {:.2f}'.format(standart_dev_critic))


# In[60]:


variance_user = np.var(games['user_score'])
print('Дисперсия пользовательских оценок: {:.2f}'.format(variance_user))
variance_critic = np.var(games['critic_score'])
print('Дисперсия оценок критиков: {:.2f}'.format(variance_critic)) 


# #### Выводы: 
# пользовательские оценки и оценки критиков разбросаны равномерно для большинства жанров. Критики чаще ставят низкие оценки и оценивают жанры, которые пользователи считают непопулярными. Пользователи оценивают стратегии, спорт и симуляции выше критиков, а критики ценят пазлы больше пользователей.

# # Проверка гипотез

# H0. Средние пользовательские рейтинги платформ Xbox One и PC одинаковы.
# 
# H1. Средние пользовательские рейтинги платформ Xbox One и PC различны.

# In[61]:


alpha = 0.05
xbox = games[(games['platform'] == 'XOne') & (games['user_score'] > 0)]['user_score']
pc = games[(games['platform'] == 'PC') & (games['user_score'] > 0)]['user_score']
if np.var(xbox)==np.var(pc):
    print('True')
else:
    print('False')


# In[62]:


sns.distplot(xbox)
plt.show()
sns.distplot(pc)
plt.show()


# ###### Распределение Гауссовское, используем Т-критерий Стьюдентса, дисперсия выборок не равна,.

# In[63]:


results = scipy.stats.ttest_ind(xbox, pc, equal_var = False)
print('p-значение:', results.pvalue)

if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# H0. Средние пользовательские рейтинги жанров Action (англ. «действие») и Sports (англ. «виды спорта») одинаковы.
# 
# H1. Средние пользовательские рейтинги жанров Action (англ. «действие») и Sports (англ. «виды спорта») разные.

# In[64]:


alpha = 0.05
action = games[(games['genre'] == 'Action') & (games['user_score'] > 0)]['user_score']
sports = games[(games['genre'] == 'Sports') & (games['user_score'] > 0)]['user_score']
if np.var(action)==np.var(sports):
    print('True')
else:
    print('False')


# In[65]:


sns.distplot(action)
plt.show()
sns.distplot(sports)
plt.show()


# ###### Распределение Гауссовское, используем Т-критерий Стьюдентса, дисперсия выборок не равна.

# In[66]:


results=scipy.stats.ttest_ind(action, sports, equal_var = False)
print('p-значение:', results.pvalue)

if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# Вывод: пользовательские рейтинги для платформ Xbox и PC различны. Средние пользовательские рейтинги жанров Action (англ. «действие») и Sports (англ. «виды спорта») тоже различны.

# # Общие выводы

# Геймдейв медленно и верно теряет обороты, игры ушли на мобильные устройства. Люди играть в приставки не перестали, поэтому не останавливаются и разработчики, хотя делают это уже более осмотрительно. 
# 
# Пятерка самых популярных платформ набрала свою популярность с начала 2000-х. Период от первых продаж до исчезновения продаж в среднем занимает 14 лет. Период для появления платформы и выхода из нее с 1980 до 2000 такой же, как и для платформ с 2000 до 2016, от 9 до 11 лет. Платформа PS трансформировалась в PS2 и PS3. Платформа NES уступила свое место более совершенным SNES с более совершенной приставкой Sega Mega Drive, также как до этого N64 уступила свое место NES. SNES 95 году обещали выпустить новую приставку, несколько раз переносили презентацию, в итоге для новой приставки выпустили 22 игры, все японского производства и платформа перестала существовать. GB были линейкой портативных устройств от компании Nintendo (N64, NES, SNES), с уходом Nintendo с рынка исчезли и GB. Период для появления платформы и выхода из нее с 1980 до 2000 меньше, чем для платформ с 2000 до 2016, и составляет 10,4 года. Платформа PS трансформировалась в PS2 и PS3. Платформа NES уступила свое место более совершенным SNES с более совершенной приставкой Sega Mega Drive, также как до этого N64 уступила свое место NES. SNES 95 году обещали выпустить новую приставку, несколько раз переносили презентацию, в итоге для новой приставки выпустили 22 игры, все японского производства и платформа перестала существовать. GB были линейкой портативных устройств от компании Nintendo (N64, NES, SNES), с уходом Nintendo с рынка исчезли и GB.  Нормально распределены данные за период с 2003 по 2015 год, их используем в дальнейшей работе. Потенциально прибыльны платформы PS4, X360 и XOne, что неудивительно, потому что это мастодонты рынка. 
# 
# От уровня оценки прямо пропорционально зависят продажи, и не важно оценил игру пользователь или критик. А также самые дорогие продажи приходятся на самые высокие оценки критиков. Жанры для игр в Северной Америке, Европе и Японии популярны одни и те же, а вот игровые платформы у японцев значительно отличаются. В разы различаются и продажи в этих регионах: больше всего продаж в Северной Америке, меньше всего в Японии. Предполагаю, что связано это с разным менталитетом этих регионов. Зависимость от рейтинга отслеживается во всех трех регионах. Наиболее популярны игры с рейтингом "для всех", "подросткам","детям старше 10 лет" и "для взрослых"(в Европе и Северной Америке спрос на них выше, японцы больше предпочитают игры без определенного рейтинга). Ситуация в Японии связана с тем, что получить возрастной рейтинг на японском рынке сложно и дорого. Начинает это с того, что всё общение и вся документация — на японском языке. «Google Переводчиком» в данной ситуации пользоваться не стоит, лучше найти человека со знанием языка или студию локализации. 
# 
# Есть 2 варианта для построения отношений: 
# 
# * разовый платёж. Вы хотите единожды сделать рейтинг для одной игры и на одну (или несколько) платформу — стоило это на 2018 год примерно 2 тысячи евро. 
# * членство. У вас есть как вступительный взнос, так и взнос за каждую игру, но цена за оценку игры ниже, чем разовая оценка в первом варианте. То есть в перспективе, если вы планируйте делать 5-7 релизов и на 3-4 платформы, вам стоит рассмотреть и членство в данном агентстве. 
# 
# В большинстве жанров оценок и критиков, и пользователей после 2007 года уменьшилось. Связано это с тем, что рынок игр в то время было принято хоронить, игры ушли на мобильные устройства и ПК, росли продажи только на стратегии и ролевые игры.Оценки критиков и пользователей для большинства жанров разбросаны равномерно. Пользователи оценивают стратегии, спорт и симуляции выше критиков, а критики ценят пазлы больше пользователей.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера 3</h2>
# 
# Помарки исправлены, теперь работа выполнена хорошо. У тебя получился классный проект, молодец. Поздравляю со сданным проектом. Надеюсь, он был интересен и познавателен. Спасибо за комментарии по исправлениям. Успехов в дальнейшем пути :)
# 
# </div>
