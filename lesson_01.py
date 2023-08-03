"""
To use a module in python you have to import it after installing it using `pip` or `conda` or any other package manager.

We are using the `pandas` module to read the data from the csv file.

It is one of the most widely used modules in python for data analysis.

You can read more about it here: https://pandas.pydata.org/

We are using `poetry` as our package manager of choice.

You can read more about it here: https://python-poetry.org/

To install the dependencies in poetry you can use the following command:

`poetry add ...`

For example, to install pandas we would use `poetry add pandas`.

In order to work with excel files you would need to install `openpyxl` using `poetry add openpyxl`.

You can read more about it here: https://openpyxl.readthedocs.io/en/stable/

We will use `openpyxl` to write the data to an excel file.

To enter the poetry shell you can use the following command:

`poetry shell`
"""

import pandas as pd # you can just import pandas but general convention is to import it as pd

"""
We will use the `pandas` module to read the data from the csv file.

Pandas uses a library called numpy under the hood to store the data in a dataframe.

As of pandas 2.0.0, the default dtype for empty frames and frames with only string columns is now StringDtype instead of object.

It also introduced a new library under the hood called `pyarrow` which promises smaller files and faster speeds.
"""

#------------------------------------------

"""
The `df` below is a variable that holds the data from the csv file.

In Pandas this is called a `DataFrame`, a 2-dimensional labeled data structure with columns of potentially different types.

Dataframes can hold all sorts of types of data but majority of time you will be working with `strings`, `integers`, `floats`, and `booleans`.

These are the most common types of data you will encounter in a dataframe.

A `string` is text data. eg) 'Hello World'
A `integer` is a whole number. eg) 1
A `float` is a decimal number. eg) 1.0
A `boolean` is a true or false value. eg) True or False

NOTE:
    Dataframes can also hold:
        `null` values which are values that are empty. eg) None or NaN
        `datetime` values which are values that represent a date and time. eg) 2021-09-01 12:00:00
        `lists` which are values that hold a list of values. eg) [1, 2, 3]
        `tuple` which are values that hold a tuple of values. eg) (1, 2, 3)
        `dict` which are values that hold a dictionary of values. eg) {'key': 'value'}
        `hashable` which are values that hold a hashable value. eg) 1
"""

df = pd.read_csv('data.csv') # the `df` variable holds the data from the csv file

"""
NOTE:
    Depending on the size of the file you are reading, it may take a while to load.  
    In this case we are using a 4mb file so it should load instantaneously.

NOTE:
    A lot of exploratory datascience is done using `jupyter notebooks` but I will be using a plain python file (`.py`) for this lesson.
"""

#------------------------------------------

"""
Now that we have stored the data in a dataframe variable `df`, we can start working with it.

Below we are printing the first 5 rows of the dataframe using the `head` method and the last 5 rows using the `tail` method.

`print()` is a built-in function in python that prints the value of the expression inside the parenthesis.

Generally it is used for debugging purposes.

In a more complex program you would use a debugger to debug your code and a logger to log your code.
"""

print(df.head())
print(df.tail())

"""
You'll likely get the following outputs:

                       name                                        roster_name                    addr                    roster_addr       city  ...    cost rebate ship_qty_as_cs check_license    use
0   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street  beachwood  ...   65.45   16.2            1.0          True  False        
1   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street  beachwood  ...  130.90   32.4            2.0          True  False        
2  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100       nome  ...   67.15   12.0            1.0         False  False        
3  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100       nome  ...  134.30   24.0            2.0         False  False        
4              anth medical                      sacred heart medical oncology         2000 e 88th ave     1545 airport blvd ste 2000  anchorage  ...  268.60   48.0            4.0          True  False        

[5 rows x 17 columns]

                       name            roster_name                  addr           roster_addr         city roster_city state  ... license.1 part  cost rebate  ship_qty_as_cs  check_license    use
31092  spartanburg regional  home health & hospice  101 east wood street  311 east wood street  spartanburg       paris    sc  ...       NaN  911  51.2   6.24             0.4          False  False
31093  spartanburg regional  home health & hospice  101 east wood street  311 east wood street  spartanburg       paris    sc  ...       NaN  911  12.8   1.56             0.1          False  False
31094  spartanburg regional  home health & hospice  101 east wood street  311 east wood street  spartanburg       paris    sc  ...       NaN  911  12.8   1.56             0.1          False  False
31095  spartanburg regional  home health & hospice  101 east wood street  311 east wood street  spartanburg       paris    sc  ...       NaN  911  25.6   3.12             0.2          False  False
31096  spartanburg regional  home health & hospice  101 east wood street  311 east wood street  spartanburg       paris    sc  ...       NaN  911  12.8   1.56             0.1          False  False

[5 rows x 17 columns]

The first row is the header row which contains the column names.  These are read directly from the csv file.

NOTE: 
    If the csv file does not have a header row, there are options you can set within the `read_csv` method to specify the column names 
    or set the header to `None` and pandas will automatically assign column names for you.
    
    In this case, the rows will be numbered starting from 0.

The first column is the index column which is also read directly from the csv file.

NOTE:
    The tail method prints the last 5 rows of the dataframe so you can see the last row is numbered 31096,
    meaning there are 31097 rows in total (including the zeroth row).

NOTE:
    `license` appears in the csv file as the name for two different columns and pandas automatically appends `.1` to the second column name.
    This is because column names must be unique in a dataframe.

NOTE:
    `NaN` is a special value that represents `Not a Number` or null value.  In this case, the `license.1` column is empty for the last 5 rows.
    These values are one of the reasons why data cleaning is important.    
"""

#------------------------------------------

"""
We can drop all the rows where any null values exist using the `dropna` method.
This is a very broad way of cleaning the data and should be used with caution.

NOTE:
    You can also specify to drop rows where all values are null using the `how` parameter.
    The default value is `any` but you can also set it to `all`.
    eg) df.dropna(how='all')
    Or you can specify which columns to look at using the `subset` parameter.
    eg) df.dropna(subset=['name', 'roster_name'])

NOTE:
    You can also drop columns using the `axis` parameter.
    eg) df.dropna(axis=1)
    An axis is a dimension of the dataframe.  The rows are the 0th axis and the columns are the 1st axis.

We can fill all the null values with a value of our choosing using the `fillna` method.
This is a method of cleaning null values that is used more often than dropping rows with null values.
This is because dropping rows with null values can result in a loss of data.

NOTE:
    You can also specify which columns to look at using the `subset` parameter.
    eg) df.fillna(subset=['name', 'roster_name'])

NOTE:
    In this example we are filling all of the null values with an empty string `''`.
    This is normally subjectively chosen based on the data.
    For example, if the column is storing ages, we would use a value of 0 instead of an empty string.
    We could set it to the average age of the population in the dataset by using the `mean` method.
    eg) df['age'].fillna(df['age'].mean())

    If the column as storing a boolean value, we would elect to set them all to `False` or `True` depending on the data or needs of the data column.
"""

df_drop_null_values = df.dropna() # the `dropna` method drops all rows that contain null values
df_fill_null_values = df.fillna('') # the `fillna` method fills all null values with the value specified in the parenthesis

#------------------------------------------

"""
Below we are using the `read_csv` method to read the csv file without headers.
"""

df_without_headers = pd.read_csv('data.csv', header=None) # read the csv file without headers

print(df_without_headers.head()) # print the first 5 rows of the dataframe

"""
The result is the same as the first example except the column names are now numbered starting from 0.

                         0                                                  1                       2                              3          4   ...     12      13              14             15     16
0                      name                                        roster_name                    addr                    roster_addr       city  ...   cost  rebate  ship_qty_as_cs  check_license    use      
1   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street  beachwood  ...  65.45    16.2             1.0           True  False      
2   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street  beachwood  ...  130.9    32.4             2.0           True  False      
3  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100       nome  ...  67.15    12.0             1.0          False  False      
4  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100       nome  ...  134.3    24.0             2.0          False  False      

[5 rows x 17 columns]

This is more representative of what raw data would look like if you received a csv file from a client or other source.

The other common scenario is that the csv file has a header row but the column names are not representative of the data or do not match your business needs.

To correct this we would create a `map` of the column names we want to the column names in the csv file or we would create a `map` of the column names we want to the column indices.
Then we would pass the `map` to the `read_csv` method using the `names` parameter.

Additionally we could opt to read it into a dataframe selectively by specifying which columns we want to read using the `usecols` parameter.

NOTE:
    However you store your map, it is generally a good idea to store it in a separate file so that it can be easily modified without having to modify the code.
    For example, you could store it in a json file and read it into a dictionary using the `json` module.
"""

"""
For example, we have a demo_map.json created with the following information:
    
    {
        "usecols": [0, 1, 2, 3],
        "columns": ["names", "roster_names", "addresses", "roster_addresses"],
        "version": "1.0.0",
        "last_updated": "2023-08-03"
    }

We are saying we would like to use columns 0-3 (the first 4 columns) and we would like to rename them to the names specified in the `columns` list.

In order to pring the file into the python application we would use the json library that is built into python.
"""

import json

demo_map = json.load(open('demo_map.json')) # read the json file into a dictionary

print(demo_map) # print the dictionary

"""
The result is the following:
    
    {'usecols': [0, 1, 2, 3], 'columns': ['names', 'roster_names', 'addresses', 'roster_addresses'], 'version': '1.0.0', 'last_updated': '2023-08-03'}

NOTE:
    This data structure is called a dictionary in python and is similar to a json object. It is a collection of key-value pairs.
    For example) The key `usecols` would return the value `[0, 1, 2, 3]`.

We can now use this dictionary to read the csv file into a dataframe and it will use the column names specified in the `columns` list.

This is a very reproduceable way to read in a csv file and is very useful when you have a lot of columns or the column names are not representative of the data.
"""

df_with_map = pd.read_csv('data_no_headers.csv', names=demo_map['columns'], usecols=demo_map['usecols']) # read the csv file using the map

print(df_with_map.head()) # print the first 5 rows of the dataframe

"""
The output we should get is the following:

                      names                                       roster_names               addresses               roster_addresses
0   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street
1   uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street
2  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100
3  norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100
4              anth medical                      sacred heart medical oncology         2000 e 88th ave     1545 airport blvd ste 2000

NOTE:
    Since we specified the exact column indexes to use in the map, the dataframe only contains the columns we specified (0-3).
    Additionally, the column names are now representative of the data as specified in the `columns` list in the map.

This is a simplistic view of how to read in a csv file using a map but it is a very powerful tool that can be used to read in a csv file with any number of columns.
The only thing that would need to be changed is the map itself.
"""

"""
Pandas is extremely powerful and has many more features than what is covered in this tutorial.

NOTE:
    You can easily calculate the mean, median, mode, standard deviation, and many other statistics using the `describe` method.
    You can also easily plot the data using the `plot` method.
    You can add columns using complex logic using the `apply` method.
    You can clean up dates and times using the `to_datetime` method.
    You can also easily write the dataframe to a new csv file using the `to_csv` method.
    You can clean up string formatting using the `str` accessor to easily remove whitespace, convert to lowercase, etc.
    You can easily obtain unique values using the `unique` method to check for duplicates in a column.

NOTE:
    You can do any of the above by chaining the methods together and building a comprehensive pipeline to clean up the data.

A map can be built to any specification and can be used to read in a csv file with any number of columns.
Functions can be created to perform any sorts of calculations or data manipulation.
Functions can also be used to perform any data validation or data cleaning.
"""

"""
A simple example is a function below to capitalize the names in the dataframe.
"""

def capitalize(value: str):
    return value.capitalize()

df_with_map['names'] = df_with_map['names'].apply(capitalize)

print(df_with_map.head())

"""
                      names                                       roster_names               addresses               roster_addresses
0   Uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street
1   Uh ahuja medical center  ascension medical group at richmond st ophthal...        3999 richmond rd         3329 n richmond street
2  Norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100
3  Norton sound health corp                             asc il corp telehealth  1000 greg kruschek ave  1000 remington blvd suite 100
4              Anth medical                      sacred heart medical oncology         2000 e 88th ave     1545 airport blvd ste 2000

As you can see, the `names` are now capitalized.
"""


if __name__ == "__main__":
    """
    To run the program enter the poetry shell to get into your environment and then run the following command:
        
        `python lesson_1.py`

    NOTE:
        You will need to install dependencies using the `poetry install` command before running the program.
    """