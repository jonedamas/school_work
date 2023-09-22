SAheart = read.table("STA530_statistical_learning/lectures/Chap4/SAheart.data", sep=",", header = TRUE)
head(SAheart)
SAheart = SAheart[,-1] # Remove the row names column
head(SAheart)
heartds = SAheart
heartds$chd = as.factor(heartds$chd)
heartds = heartds[,c(10,1:9)]
head(heartds)


library(ISLR)
library(ggplot2)
library(ggpubr)
library(kableExtra)



data(Default)
head(Default,5)

Default$default = ifelse(Default$default == "Yes", 1, 0)

lm1_default = lm(default~balance, data=Default)
lm1_alpha = coef(lm1_default)[1]
lm1_beta = coef(lm1_default)[2]

lm2_default = lm(default~income, data=Default)
lm2_alpha = coef(lm2_default)[1]
lm2_beta = coef(lm2_default)[2]

gglm1 = ggplot(Default, aes(x=balance, y=default))+geom_point() +
  geom_line(aes(x=balance, y=lm1_alpha + lm1_beta*balance), col="red")
gglm2 = ggplot(Default, aes(x=income, y=default))+geom_point() + 
  geom_line(aes(x=income, y=lm2_alpha + lm2_beta*income), col="orange")
ggarrange(gglm1,gglm2)


library(ggplot2)
ggplot(data.frame(x=c(-6,5)), aes(x))+
  xlab(expression(x))+ 
  ylab(expression(p))+
    stat_function(fun=function(x) exp(x)/(1+exp(x)), geom="line", colour="red")+
    stat_function(fun=function(x) exp(2*x)/(1+exp(2*x)), geom="line", colour="orange")+
          stat_function(fun=function(x) exp(0.5*x)/(1+exp(0.5*x)), geom="line", colour="blue")+
    stat_function(fun=function(x) exp(1+x)/(1+exp(1+x)), geom="line", colour="red",linetype="dashed")+
    stat_function(fun=function(x) exp(1+2*x)/(1+exp(1+2*x)), geom="line", colour="orange",linetype="dashed")+
          stat_function(fun=function(x) exp(1+0.5*x)/(1+exp(1+0.5*x)), geom="line", colour="blue",linetype="dashed")+
  scale_colour_manual("0+k x",values = c("red", "orange","blue"),labels=c("1","2","0.5"))



glm_default = glm(default~balance, data=Default, family="binomial")
glm_alpha = coef(glm_default)[1]
glm_beta = coef(glm_default)[2]

ggglm = ggplot(Default, aes(x=balance, y=default))+geom_point() + 
  geom_line(aes(x=balance, y=exp(glm_alpha+glm_beta*balance)/
                  (1+exp(glm_alpha+glm_beta*balance))), col="blue")


ggglm



p=seq(0.1,0.9,0.1)
odds=p/(1-p)
kable(t(data.frame(p,odds)),digits=c(2,2))%>%
  kable_styling()


colnames(Default)
fit=glm(default~student+balance+income,family="binomial",data=Default)
round(coef(fit),6)
round(exp(coef(fit)),3)


options("scipen"=100, "digits"=4)
fit=glm(default~student+balance+income,family="binomial",data=Default)
summary(fit)
options("scipen"=0, "digits"=7)


fit=glm(default~student,family="binomial",data=Default)
round(summary(fit)$coef,4)


fit=glm(default~student+balance,family="binomial",data=Default)
round(summary(fit)$coef,4)




head(heartds)

library(ggplot2)
library(GGally)
ggpairs(heartds, aes(color=chd), #upper="blank",  
        lower = list(continuous = wrap("points", alpha = 0.3, size=0.2)),
        upper = list(continuous = wrap("cor", size = 2)))+
        theme(axis.text = element_text(size = 4))


glm_heart = glm(chd~., data=heartds, family="binomial")
summary(glm_heart)



library(MASS)
tab <- round(cbind(coef(glm_heart),exp(coef(glm_heart)), 
             exp(confint(glm_heart)[,1]),
             exp(confint(glm_heart)[,2])), digits = 3) 
colnames(tab) = c("coeffs", "exp(coeffs)","2.5%","97.5%" ) 
tab


library(ggplot2)
library(ggpubr)
x = seq(-6, 6, by = 0.01)
n = length(x)
y1 = dnorm(x, mean = -2, sd=1.5)
y2 = dnorm(x, mean= 2, sd=1.5)

XY = data.frame(x, y1, y2)
ggplot(XY)+geom_line(aes(x=x, y=0.5*y1), col="darkgreen")+geom_line(aes(x=x, y=0.5*y2), col="orange")+ annotate("text", x = 1.7, y = 0.175, parse=TRUE, label = as.character(expression(paste(pi[1], "=", pi[2], "=", 0.5))))+labs(y=NULL, title=expression(pi[k]*f[k](x)))


taildnorm=function(x,upper,lower,mean,sd,faktor)
{ 
  res=faktor*dnorm(x,mean=mean,sd=sd)
  res[x<lower]=0
  res[x>upper]=0
  return(res)
}

gg=ggplot(XY)+geom_line(aes(x=x, y=0.5*y1), col="darkgreen")+geom_line(aes(x=x, y=0.5*y2), col="orange")+geom_vline(xintercept=0, linetype="dashed")+ annotate("text", x = 1.7, y = 0.175, parse=TRUE, label = as.character(expression(paste(pi[1], "=", pi[2], "=", 0.5))))+labs(y=NULL, title=expression(pi[k]*f[k](x)))
gg+stat_function(fun=taildnorm,geom='area',fill="lightgreen",alpha=0.5,args=list(upper=6,lower=0,mean=-2,sd=1.5,faktor=0.5))+stat_function(fun=taildnorm,geom='area',fill="orange",alpha=0.5,args=list(upper=0,lower=-6,mean=2,sd=1.5,faktor=0.5))


ggplot(XY)+geom_line(aes(x=x, y=0.3*y1), col="darkgreen")+geom_line(aes(x=x, y=0.7*y2),col="orange")+geom_vline(xintercept=-0.45, linetype="dashed") +annotate("text", x = -2, y = 0.2, parse=TRUE, label =as.character(expression(pi[1] == 0.3)))+annotate("text", x=1, y=0.2, parse=TRUE, label=as.character(expression(pi[2]==0.7)))+labs(y=NULL, title=expression(pi[k]*f[k](x)))



n=1000
pi1=pi2=0.5
mu1=-2; mu2=2; sigma=1.5
set.seed(12345)
n1train=rbinom(1,n,pi1);n2train=n-n1train
n1test=rbinom(1,n,pi1);n2test=n-n1test
train1=rnorm(n1train,mu1,sigma);train2=rnorm(n2train,mu2,sigma)
test1=rnorm(n1test,mu1,sigma);test2=rnorm(n2test,mu2,sigma)
sigma2.1=var(train1);sigma2.2=var(train2)
estsigma2=((n1train-1)*sigma2.1+(n2train-1)*sigma2.2)/(n-2)
rule=0.5*(mean(train1)+mean(train2))+
  estsigma2*(log(n2train/n)-log(n1train/n))/(mean(train1)-mean(train2))

cat("Training error: ", (sum(train1>rule)+sum(train2<rule))/n)
cat("Test error: ", (sum(test1>rule)+sum(test2<rule))/n)




row1 = c("", "True 1", "True 2","...", "True K")
row2 = c("Predicted 1", "correct", "wrong", "...", "wrong")
row3 = c("Predicted 2", "wrong", "correct","...", "wrong")
row4 = c("...", "...", "...", "...","...")
row5 = c("Predicted K", "wrong", "wrong","...", "correct")


rbind(row1, row2, row3,row4,row5)


attach(iris)
library(class)
library(MASS)
library(ggplot2)
library(dplyr)
head(iris)


iris0_plot = ggplot(iris, aes(x=Sepal.Width, y=Sepal.Length, 
                              color=Species))+geom_point(size=2.5)
iris0_plot


testgrid = expand.grid(Sepal.Length = seq(min(iris[,1]-0.2), max(iris[,1]+0.2), 
              by=0.05), Sepal.Width = seq(min(iris[,2]-0.2), max(iris[,2]+0.2), 
              by=0.05))
iris_lda = lda(Species~Sepal.Length+Sepal.Width, data=iris, prior=c(1,1,1)/3)
res = predict(object = iris_lda, newdata = testgrid)
Species_lda = res$class
postprobs=res$posterior

iris_lda_df = bind_rows(mutate(testgrid, Species_lda))
iris_lda_df$Species_lda = as.factor(iris_lda_df$Species_lda)

irislda_plot = iris0_plot + geom_point(aes(x = Sepal.Width, y=Sepal.Length, 
                            colour=Species_lda), data=iris_lda_df, size=0.8)
irislda_plot


iris_qda = qda(Species~Sepal.Length + Sepal.Width, data=iris, prior=c(1,1,1)/3)
Species_qda = predict(object = iris_qda, newdata = testgrid)$class

iris_qda_df = bind_rows(mutate(testgrid, Species_qda))
iris_qda_df$Species_qda = as.factor(iris_qda_df$Species_qda)

irisqda_plot = iris0_plot + geom_point(aes(x = Sepal.Width, y=Sepal.Length, 
                            colour=Species_qda), data=iris_qda_df, size=0.8)
irisqda_plot


set.seed(1)
train = sample(1:150, 75)

iris_train = iris[train, ]
iris_test = iris[-train, ]

iris_lda2 = lda(Species~Sepal.Length + Sepal.Width, 
                data=iris_train, 
                prior=c(1,1,1)/3)


# Training error
iris_lda2_predict_train = predict(iris_lda2, newdata=iris_train)
table(iris_lda2_predict_train$class, iris_train$Species)
# Test error
iris_lda2_predict_test = predict(iris_lda2, newdata=iris_test)
table(iris_lda2_predict_test$class, iris_test$Species)



iris_qda2 = qda(Species~Sepal.Length + Sepal.Width, data=iris_train, 
                prior=c(1,1,1)/3)


# Training error
iris_qda2_predict_train = predict(iris_qda2, newdata=iris_train)
table(iris_qda2_predict_train$class, iris_train$Species)
# Test error
iris_qda2_predict_test = predict(iris_qda2, newdata=iris_test)
table(iris_qda2_predict_test$class, iris_test$Species)



row1 = c("", "True -", "True +","Total")
row2 = c("Predicted -", "True Negative TN", "False Negative FN","N*")
row3 = c("Predicted +", "False Positive FP", "True Positive TP","P*")
row4 = c("Total", "N", "P"," ")
rbind(row1, row2, row3,row4)


row1 = c("Name", "Definition", "Synonyms")
row2 = c("False positive rate", "FP/N", "Type I error, 1-specificity")
row3 = c("True positive rate", "TP/P", "1-Type II error, power, sensitivity, recall")
row4=c("Positive predictive value (PPV)","TP/P*","Precision, 1-false discovery proportion")
row5=c("Negative predictive value (NPV)","TN/N*","")

rbind(row1, row2, row3,row4,row5)

set.seed(20)
train_ID = sample(1:nrow(heartds), nrow(heartds)/2)
train_SA = heartds[train_ID, ]
test_SA = heartds[-train_ID, ]


glm_SA = glm(chd~. , data=train_SA, family="binomial")
summary(glm_SA)


probs_SA = predict(glm_SA, newdata=test_SA, type="response")

pred_SA = ifelse(probs_SA > 0.5, 1, 0)

predictions_SA = data.frame(probs_SA, pred_SA, test_SA[,1])
colnames(predictions_SA) = c("Estim. prob. of Y=1","Predicted class","True class")
head(predictions_SA)


table(pred_SA, SAheart[-train_ID,10])

SA_train_prob = glm_SA$fitted.values
SA_train_pred = ifelse(SA_train_prob>0.5, 1, 0)
conf_train = table(SA_train_pred, SAheart[train_ID, 10])
misclas_train = (231-sum(diag(conf_train)))/231
misclas_train
sens_train=conf_train[2,2]/sum(conf_train[,2])
sens_train
spec_train=conf_train[1,1]/sum(conf_train[,1])
spec_train


library(pROC)
SA_roc = roc(SAheart[-train_ID, 10], probs_SA, legacy.axes=TRUE)
ggroc(SA_roc)+ggtitle("ROC curve")+ 
  annotate("text", x = 0.25, y = 0.30, label = "AUC = 0.764")
ggroc(SA_roc)+ggtitle("ROC curve")+ 
  annotate("text", x = 0.25, y = 0.30, label = paste("AUC =",round(SA_roc$auc,3)))


res=table(pred_SA, SAheart[-train_ID,10])
sens=res[2,2]/sum(res[,2])
spec=res[1,1]/sum(res[,1])
sens
spec


# Poisson example
asthma = read.csv("asthma.csv", header = TRUE, sep = ",")
head(asthma, 4)
hist(asthma$attack, main="",xlab="Number of attacks", col="burlywood")

library(ggplot2)
library(GGally)
ggpairs(asthma[,c(4,1:3)],lower = list(combo = wrap(ggally_facethist, binwidth = 0.5)))

mod1 <- glm(attack~gender, family = "poisson", data = asthma)
summary(mod1)
mod2 <- glm(attack~gender+res_inf+ghq12, family = "poisson", data = asthma)
summary(mod2)
mod3 <- glm(attack~res_inf+ghq12, family = "poisson", data = asthma)
summary(mod3)

