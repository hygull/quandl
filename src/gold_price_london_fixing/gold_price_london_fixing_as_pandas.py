# https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing

import quandl
import conf

# Setting Quandl's API KEY (Use your own API KEY)
quandl.ApiConfig.api_key = conf.API_KEY;

data = quandl.get("LBMA/GOLD", authtoken="2Evs3E8J_LduFKbNF6Gw", returns='pandas', start_date='01-01-2014', end_date="01-01-2017");
print data;
print type(data); # <class 'pandas.core.frame.DataFrame'>

# Save te obtained data to csv
data.to_csv("GOLD-Gold-Price-London-Fixing.csv", sep='\t', encoding='utf-8');