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
The t test is used to compare means and tells you how significant the differences are. 
The p value is used with a t value to tell how likely it is that your t value happened by chance. A low p value is good.

### Part 2.2
Ttest_1sampResult(statistic=-3.8682665640568583, pvalue=0.00041658142370520256)
This result tells us that the sample mean deviates from the null hypothesis by -3.8682665640568583. The pvalue tells us that there is a 0.041658142370520256% chance that the result happened by chance.

### Part 2.3
Ttest_1sampResult(statistic=0.1964197529935458, pvalue=0.84532834985133909)
This result tells us that the sample mean deviates from the null hypothesis by 0.1964197529935458. The pvalue tells us that there is a 84.532834985133909% chance that the result happened by chance. This is very high.
