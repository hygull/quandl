"""
	{
		"date": "14 May 2018, Mon",
		"aim": "To access QUANDL's APIs using Python's quandl package",
		"links": [
			"https://docs.quandl.com/docs/python",
			"https://github.com/quandl/Matlab",
		],
		"pythonVersion": "Python 2.7.14 :: Anaconda custom (64-bit)",
		"codedBy": "Rishikesh Agrawani"
	}
"""


import quandl 
from conf import API_KEY

# Setting Quandl's API KEY
quandl.ApiConfig.api_key = conf.API_KEY