# Grocery Store Items Association

According to an article by the BBC, Tesco stated that men who buy babies nappies are likely to put cans of beer in their shopping trolley too. Research by Tesco revealed a strong link between nappies and beer purchases by male customers. Tesco may use this information to increase sales figures, for instance, putting beer at the top shelf and nappies on the shelves below. 

In a general sense, if it were possible for stores to get an idea of their product association rules, they could be implemented to structure the store layout in order to increase the probability of higher customer spending. For instance, if a typical customer purchases bread and milk as part of their weekly shop, seperating these products in order to maximise the distance travelled between them in store will allow customers to be exposed to a wide range of products in between. This increases the probability of customers purchasing additional products they would not have initially bought.

**Task**

Produce a machine learning model for the store under study which finds the association rules for the products sold in store. This model will be used to optimise the placement of products in store to further increase sales.

We will be analysing the shopping baskets of customers in our dataset, learning product associations and customer behaviour. In order for us to learn these associations, we will be using the "Apriori" association rule algorithm.

## Association Rule Learning

"People who bought item X also bought item Y", "These items are frequently bought together", or "Those who watched program A also watched program B". In essence, this is what association rule learning is about.

## Apriori Algorithm

This algorithm has three parts:
- Support
- Confidence
- Lift

E.g. Let's say we own a grocery store and wish to study our customers shopping behaviour. Using the Apriori algorithm, let's analyse the association between bread and milk. The "Support", "Confidence" and "Lift" are calculated as follows:

<img src = 'Screen1.png' width='700'>



### References
BBC article:   http://news.bbc.co.uk/1/hi/uk/77622.stm
Online LaTeX equation editor: https://www.codecogs.com/latex/eqneditor.php
