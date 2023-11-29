# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?
The model can be tested with some of its data to measure its effectiveness. This is important because we did not have any test data in part 1, so we would never know if it was accurate.

2. What does the R squared coefficient tell you about the model?
The R squared coefficient tells us how linear our training data is (AKA: how well does the best-fit line "fit" the training data).

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.
Similar to question 1, our model is pretty accurate and we can prove this with the accuracy of our testing data. However, when you run the program, the data is split at random, so we can have models with unfair training or testing data.