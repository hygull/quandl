# https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing

import quandl
import conf

# Setting Quandl's API KEY (Use your own API KEY)
quandl.ApiConfig.api_key = conf.API_KEY;

data = quandl.get("LBMA/GOLD", authtoken="2Evs3E8J_LduFKbNF6Gw", returns='numpy', start_date='01-01-2014', end_date="01-01-2017");
print data;
print type(data); # <class 'numpy.recarray'>