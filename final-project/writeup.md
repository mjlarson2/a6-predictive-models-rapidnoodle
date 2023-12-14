1. Why did you choose the algorithm you did?
We chose the logistic regression algorithm because of the nature of the data: all the variables are linked to whether or not a given email is spam, which presents two possible classifications, a scenario for which a logistic regression algorithm makes sense.

2. What results did your model produce? What do they mean?
Our model classified a given email as either spam or not spam.

3. A prediction based on your model


4. How accurate is your model?
Our model has an accuracy score of ~0.94, which is very good accuracy. This is likely because this model relies on many (~57) differnet input variables to determine whether or not an email is spam.

5. What are the real world implications of your model?
(Much much more complex) versions of models like ours are the basis for various spam filters used by email clients or similar services. The problems with this model, however, come up when an email is falsely labelled as spam. The creators of the dataset discuss this themselves: they say that there is low tolerance for false positives in this use case. This leads to the conclusion that this model as-is is probably not a good spam filter, but it is a solid demonstration of the principle.
