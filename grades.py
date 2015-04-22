# print the grades

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in range(len(grades)):
        print grades[i]

print "Grades: "
print "-------------------------"  
print_grades(grades)


def grades_sum(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]        
    return total
print "-------------------------"    
print "Sum of grades: %s" % (grades_sum(grades))


def grades_average(grades):
    return grades_sum(grades)/float(len(grades))
print "-------------------------"        
print "Grades average: %s" % (grades_average(grades))


"""
Variance
We're going to use the average for computing the variance. The variance allows us to see how
widespread the grades were from the average.

The Variance
Let's see how the grades varied against the average. This is called computing the variance.

A very large variance means that the students' grades were all over the place, while a small variance 
(relatively close to the average) means that the majority of students did fairly well.

Instructions
01. On line 18, define a new function called grades_variance() that accepts one argument, scores, a list.
02. First, create a variable average and store the result of calling grades_average(scores).
03. Next, create another variable variance and set it to zero. We will use this as a rolling sum.
04. for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to 
variance.

05. Divide the total variance by the number of scores.

06. Then, return that result.

07. Finally, after your function code, print grades_variance(grades).
"""
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        #compute its square difference
        variance += (average - score) ** 2        
    return variance/len(scores)
print "-------------------------"      
print "grades_variance: %s" % (grades_variance(grades))

"""
Standard Deviation
Great job computing the variance! The last statistic will be much simpler: standard deviation.

The standard deviation is the square root of the variance. You can calculate the square root by 
raising the number to the one-half power.

Instructions
01. Define a function grades_std_deviation(variance).
02. return the result of variance ** 0.5
03. After the function, create a new variable called variance and store the result of calling
 grades_variance(grades).
04. Finally print the result of calling grades_std_deviation(variance).
"""

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)
print "-------------------------"  
print "grades_std_deviation(variance): %s" %(grades_std_deviation(variance))


print "-------------------------"  

"""
Review
You've done a great job completing this program.

We've created quite a few meaningful functions. Namely, we've created helper functions to print a list of grades, compute the sum, average, variance, and standard deviation about a set of grades.

Let's wrap up by printing out all of the statistics.

Who needs to pay for grade calculation software when you can write your own? :)

Instructions
Print out the following:

-- all of the grades
-- sum of grades
-- average grade
-- variance
-- standard deviation
"""
# DONE ABOVE