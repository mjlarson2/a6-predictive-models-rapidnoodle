# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The R squared coefficient is 0.86 and it says how well my model fits the price by age and milage trend. In this case, there is a noticeable trend with decently accurate predictions.

2. Is your model accurate? Why or why not?
I would say my model is decently accurate becuase the r^2 value is close to 1 and the actual vs predicted values are not too far off. There are some outliers in the predictions, but that's normal.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
The model predicted a 10-year-old car with 89000 miles to be worth $8703.25 and a 20-year-old car with 150000 miles to be worth $714.10.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
Since it is a decreasing linear model, the predicted values will eventually go negative if the input variables go high enough. It is not a perfect model, but still gives a generalized idea for more common inputs.
