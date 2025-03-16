#### Permutations ####

permut<-function(n,k){
	return(factorial(n)/factorial(n-k))
}
permut(3,2)
permut(20,3) #selection of office holders

#### birthday problem ####

permut(365,2) #impossible to be calculated

permut2<-function(n,k){
	outcome=1
	count=0
	while(count<k){
		outcome=outcome*n
		n=n-1
		count=count+1
	}
	return(outcome)
}
permut2(365,2)

k_diff_birth<-function(k){
	return(1-permut2(365,k)/365^k)
}

k_diff_birth(40)

data<-matrix(50)
for (k in 1:50){
  data[k]<-k_diff_birth(k)
}
plot(data)

#selection of office holders
permut(20,3)	

#### Combinations ####

comb<-function(n,k){
	return(factorial(n)/factorial(k)/factorial(n-k))
}

comb(20,3)				

choose(5,2) #combination


#Bayes' rule

prior <- c(0.6, 0.3, 0.1)
like <- c(0.003, 0.007, 0.01)
post <- prior * like
post/sum(post)

newprior <- post
post <- newprior * like
post/sum(post)


## posterior -> likelihood
ind=0
count=0
num=10000

prior <- c(0.6, 0.3, 0.1)
#prior <- c(1/3, 1/3, 1/3)
like <- c(0.003, 0.007, 0.01)
post <- prior * like
post/sum(post)

for(i in 1:num){
  newprior <- post
  post <- newprior * like^ind * (1-like)^(1-ind)
  post/sum(post)
  count=count+ind
  ind=sample(c(0,1), 1, prob=c(0.993,0.007))
}
post/sum(post)
count/num

