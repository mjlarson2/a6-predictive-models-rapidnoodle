# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
My model scored about 0.68 without StandardScaler, which is lower than before. This is because scaling your data evenly distributes our data for our model, and without it, disproportionately skews your resuts.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model scored about 0.83 with the StandardScaler, which is pretty accurate enough for the given use case because the number is close to 1.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did pretty well, getting it correct about 83% of the time according to the StandardScaler score, which is pretty accurate and definitely has a noticable trend.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
According to our model, a 34 year old Female who makes 56000 a year would NOT buy an SUV.
