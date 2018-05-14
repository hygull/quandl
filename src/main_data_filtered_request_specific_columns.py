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

# Requesting specific columns
# Quandl codes: "NSE/OIL.1", "WIKI/AAPL.4"
data = quandl.get(["NSE/OIL.1", "WIKI/AAPL.4"])
print data; 