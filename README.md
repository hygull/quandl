# Python's quandl package

A project containing the source code and many more usage examples related to Python's quandl package

> Get millions of financial and economic datasets from hundreds of publishers directly into Python.

# Python version

Python 2.7.14 :: Anaconda custom (64-bit)

## Compatibility

This package is compatible with Python v2.7.x and v3.x+.

## Installation 

`pip install quandl`

## Authentication

> The Quandl Python module is free but you must have a Quandl API key in order to download data. To get your own API key, you will need to create a free [Quandl account](https://www.quandl.com/users/login) and set your API key.
>
> Finally you can visit https://www.quandl.com/account/api and check/copy your API to access Quandl's API.

## Setting API Key

conf.py
```python
# API KEY for QUANDL (Use your own API KEY)
API_KEY = '2eVS3E8J_lDUFKbnF6gW';
```

main.py
```python
"""
	{
		"date": "14 May 2018, Mon",
		"aim": "To access QUANDL's APIs using Python's quandl package",
		"links": [
			"https://docs.quandl.com/docs/python",
			"https://github.com/quandl/Matlab",
			"https://docs.quandl.com/docs/python-time-series",
		],
		"pythonVersion": "Python 2.7.14 :: Anaconda custom (64-bit)",
		"codedBy": "Rishikesh Agrawani"
	}
"""


import quandl 
import conf

# Setting Quandl's API KEY
quandl.ApiConfig.api_key = conf.API_KEY
```

## Run code (main.py)

`python main.py`

# TIME-SERIES (Using time-series based APIs, Making a time-series call)

> [WTI Crude Oil Price](https://www.quandl.com/EIA/PET_RWTC_D)
>
> Quandl code &raquo; EIA/PET_RWTC_D
>
> From &raquo; [US Department of Energy](https://www.quandl.com/EIA)

```python
"""
	{
		"date": "14 May 2018, Mon",
		"aim": "To access QUANDL's APIs using Python's quandl package",
		"links": [
			"https://docs.quandl.com/docs/python",
			"https://github.com/quandl/Matlab",
			"https://docs.quandl.com/docs/python-time-series",
		],
		"pythonVersion": "Python 2.7.14 :: Anaconda custom (64-bit)",
		"codedBy": "Rishikesh Agrawani"
	}
"""


import quandl 
import conf

# Setting Quandl's API KEY (Use your own API KEY)
quandl.ApiConfig.api_key = conf.API_KEY

# [WTI Crude Oil Price](https://www.quandl.com/EIA/PET_RWTC_D)
# Quandl code: EIA/PET_RWTC_D
# From: [US Department of Energy](https://www.quandl.com/EIA)
data = quandl.get("EIA/PET_RWTC_D");
print data;
```

## Run code (main.py)

`python main.py`

Click [WTI Crude Oil Price - time series] to see the output of above command.







