# Assignment 8: Populations and deep learning

## Part 1: Accuracy and recall

### Part 1.1 & 1.2
Write two lines: what is the difference between accuracy and precision?
Write two lines: what is the difference between precision and recall?

Accuracy
<ul>
<li>True Positives (<b>TP</b>): number of positive examples.</li>
<li>False Positives (<b>FP</b>): number of negative examples, labeled as positive.</li>
<li>True Negatives (<b>TN</b>): number of negative examples.</li>
<li>False Negatives (<b>FN</b>): number of positive examples, labeled as negative.</li>
</ul>

accuracy = (TP + TN)/(TP + TN + FP + FN)

The accuracy paradox:
Depending on whether we set it to output the positives or the negatives,
the accuracy will always increase, when <b>TP</b> < <b>FP</b> or when <b>Tn</b> < <b>FN</b>.

So to not get bamboozled by a false accuracy, we use together with precision and recall:

precision = <b>TP/(TP + FP)</b>
recall = <b>TP/(TP + FN)</b>

Example:

We create a program that detects blue cars. We pass 15 pictures of cars of different color to it.
Out of the 15 cars, the program recognizes 10 to be blue. 7 of the 10 recognized cars are blue (true positives),
while the rest are yellow (false positives).

from this example we can see that the programs precision = 7/10 and its recall = 7/15


src: https://tryolabs.com/blog/2013/03/25/why-accuracy-alone-bad-measure-classification-tasks-and-what-we-can-do-about-it/


### Part 1.3
Using ``sklearn.metrics.classification_report`` print the result from your
breast cancer classification from last week. Explain what is going on in at
least two lines of text.

## Part 2: Population and t-test
Using the data from ``brain_size.csv``, we would like to learn something
about the height of the people in the dataset and how it compares to the
danish and american population.

The data is taken from the scipy example at
http://www.scipy-lectures.org/packages/statistics/index.html#student-s-t-test-the-simplest-statistical-test

### Part 2.1
Write at least two lines about what a t-test can tell you and what the P-value
can be used for.

### Part 2.2
It turns out that the [average danish height is around 1.8 meters (71 inches)](https://en.wikipedia.org/wiki/List_of_average_human_height_worldwide).
Run a t-test using ``scipy.stats.ttest_1samp`` on the height of the people
in the dataset, assuming the mean height in the population is 71 inches.
Report the output and, using at least two lines of text, describe what the
numbers tells us.

### Part 2.3
Americans is generally a little lower than danes. It turns out they are [roughly
around 174 cm (68.4 inches) tall](https://ourworldindata.org/human-height/).
Run the same t-test as before, but assuming that the average height of the
population now is 68.4 inches.
Report the output and, using at laest two lines of text, describe what the
numbers tells us, and why they are different from the numbers from before.

## Part 3 (OPTIONAL): Training a perceptron network
Using the breast cancer dataset to predict whether a tumor is benign or
malignant, try to train a perceptron network (using
``sklearn.linear.Perceptron``) instead of your logistic model.

Don't forget to either split the dataset using a 80/20 training/testing split
or to use K-fold cross-validation (K is usually 10).

### Part 3.1
Write two lines about what is going on in the perceptron network.

### Part 3.2
Measure the accuracy of the model. Write two lines: is it better or worse than
your logistic regression model, and why is it better or worse?
