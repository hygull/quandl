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

# WTI Crude Oil Price (https://www.quandl.com/EIA/PET_RWTC_D)
# Quandl code: EIA/PET_RWTC_D
# From: US Department of Energy (https://www.quandl.com/EIA)
data = quandl.get("EIA/PET_RWTC_D", returns="numpy"); 
print data; # data is Numpy array