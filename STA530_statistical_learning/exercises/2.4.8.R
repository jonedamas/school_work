rm(list=ls())

# a.)
# load data
college = read.csv('~/school_work/STA530_statistical_learning/exercises/College.csv')

# b.)
# set row names
rownames(college) <- college[, 1]
View(college)

# remove first column
college <- college[, -1]

# c.)

summary(college)

pairs(college[, 2:11])

boxplot(Outstate ~ Private, data=college)
