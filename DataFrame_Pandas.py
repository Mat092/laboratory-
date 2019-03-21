# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:04:00 2019

@author: mattia.ceccarelli3
"""

"""
21/03/2019 Lesson 9 

DataFrame in pandas 

"""

#%%
import pandas as pd 

data = pd.DataFrame([('Andrea', 24, 178, 'Male'),
                     ('Maria', 33, 154, 'Female'),
                     ('Luca', 30, 175, 'Male')],
                    columns=['name', 'age', 'height', 'sex'])
data.set_index('name', inplace=True)

"""
Pandas is one of the main staple of data analysis in the 
scientific python world 

It's a way of dealing with Dataframe
there's an impolementation od dataframe in most programming languages 

The dataframe "data" conteins infos about people. it's basically a table


"""

data



"""
the most commonly used is the tidyed formula:
    there is a very detailed paper about it 
    It's a way to organize data in order for them to be easier to read.
    
TIDY DATA
    every table is representing a specific kind of measurments
    we want to store as much metadata as possbile.
    every measured value is a comlumn 
    every observed unit is a row

"""
#%%

# skipped cell about hierarchical indexes
# Righe e colonne possono avere indici **GERARCHICI**, 
# in cui ho più livelli di indicizzazione delle mie informazioni

import pandas as pd

data = pd.DataFrame([('Andrea', '2015', 'residenza', 'Rimini', 'via stretta 20'),
                     ('Andrea', '2015', 'domicilio', 'Bologna', 'via larga 30'),
                     ('Andrea', '2016', 'residenza', 'Rimini', 'via stretta 20'),
                     ('Andrea', '2016', 'domicilio', 'Bologna', 'via larga 30'),
                     ('Giulio', '2015', 'residenza', 'Rimini', 'via giusta 50'),
                     ('Giulio', '2015', 'domicilio', 'Bologna', 'via falsa 40'),
                     ('Giulio', '2016', 'residenza', 'Bologna', 'via torna 10'),
                     ('Giulio', '2016', 'domicilio', 'Bologna', 'via torna 10'),
                    ], columns=['nome', 'anno', 'tipologia', 'città', 'indirizzo']
                    )
data.set_index(['nome', 'anno', 'tipologia'], inplace=True)

#data.sortlevel(0, axis=1, inplace=True)

data = data.unstack()
data.columns = data.columns.swaplevel(0, 1)




#%%

"""
ussually we will have different table, the work is merging splitting
and rework hthose information.

look at literaturee about this.
"""

import pandas as pd

data = pd.DataFrame([('Andrea', '2015', 'residenza', 'Rimini', 'via stretta 20'),
                     ('Andrea', '2015', 'domicilio', 'Bologna', 'via larga 30'),
                     ('Andrea', '2016', 'residenza', 'Rimini', 'via stretta 20'),
                     ('Andrea', '2016', 'domicilio', 'Bologna', 'via larga 30'),
                     ('Giulio', '2015', 'residenza', 'Rimini', 'via giusta 50'),
                     ('Giulio', '2015', 'domicilio', 'Bologna', 'via falsa 40'),
                     ('Giulio', '2016', 'residenza', 'Bologna', 'via torna 10'),
                     ('Giulio', '2016', 'domicilio', 'Bologna', 'via torna 10'),
                    ], columns=['nome', 'anno', 'tipologia', 'città', 'indirizzo']
                    )

data 

"""
that's what a (non perfect) tidy dataframe may look. Ther's no correct solution 
abou thow to store data.

tidy is a way of storing, it might be not the ideal one.
usaully is considered th ebest way 
"""

#%%

"""
Panda allow to manioulate dataframe iin python:
    numpy provide dataStructure (ndarry)
    
    Pandas give you adtaaFrame and Series 
    
    Pandas read and write almost all type of tabular format
    
    
"""
import numpy as np 
import pandas as pd


page = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
wikitables = pd.read_html(page)

"""
filters table
"""
#%%
wikitables[0].head()

dataframe = wikitables[0].copy()

dataframe.columns

dataframe['Year'].head()

"""
there are tons of operation similar as numpy arrays for Series
and DataFrame. DataFrame are basically collections of Series
"""

#%%

"""
Series as elements of DataFrame
"""

import pandas as pd
import numpy as np


page = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
wikitables = pd.read_html(page,)

#%%

"""
Manipulation 
"""
import numpy as np 
import pandas as pd 

wiki = "https://it.wikipedia.org/wiki/"
url_popolazione = wiki + "Comuni_d%27Italia_per_popolazione"
url_superficie = wiki + "Primi_100_comuni_italiani_per_superficie"

comuni_popolazione = pd.read_html(url_popolazione, header=0)
comuni_popolazione = comuni_popolazione[0]
comuni_popolazione.head()


comuni_superficie = pd.read_html(url_superficie, header=0)
comuni_superficie = comuni_superficie[0]
comuni_superficie.head()

#%%

comuni_superficie.groupby('Regione').mean()

g = comuni_superficie.groupby('Regione')
g.aggregate([np.mean, np.std, pd.Series.count])

#%%
"""
Seaborn
"""


