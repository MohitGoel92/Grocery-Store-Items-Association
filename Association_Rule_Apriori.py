# Association rule learning - Apriori

# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset

ds = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# The algorithm requires a list of lists where all values are strings. The below code appends the list "transactions" with each
# list being an independent customers shopping basket/transaction.

transactions = []

for i in range(0,7501):
    transactions.append( [ str(ds.values[i,j]) for j in range(0,20) ] )
    
# min_support: (3 products per day * 7 days)/(7,500 transactions in total) = 0.0023 or 0.003 (3 DP), therefore at least 0.3% 
# of all transactions will contain this product.

# min_confidence: The % of times the rule is correct, i.e. min_confidence = 0.8 => 80% of the times the rule is prevelant 
# (e.g. if 4 out of 5 customers bought apples and bananas together, the propability of a customer buying bananas if they have
# picked apples is 80%, therefore min_confidence = 0.8). Note we use 0.2 as that seems optimal in our case.
    
# min_lift: The relevance/strength of the rule, min_lift >= 3 implies high/strong association between the two.

# min_length: The minimum number of items per list (>= 2, so we do not take into consideration any single item transactions).


# Training Apriori on the dataset
    
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results

results = list(rules)

# For instance from the first item, we can see that light cream and chicken are commonly bought together. 
# An interpretation of this could be that people who purchase light cream are careful about what they eat, hence they are more 
# likely to buy chicken i.e. white meat instead of red meat (e.g beef). Or this could mean that light cream is
# commonly used in recipes for chicken, therefore having a cultural link.

# The support value for the first rule is 0.0045. This number is calculated by dividing the number of transactions 
# containing light cream divided by total number of transactions. The confidence level for the rule is 0.2905 which
# shows that out of all the transactions that contain light cream, 29.05% of the transactions also contain chicken. 
# Finally, the lift of 4.84 tells us that chicken is 4.84 times more likely to be bought by the customers who buy light 
# cream compared to the default likelihood of the sale of chicken.