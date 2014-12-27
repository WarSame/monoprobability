from __future__ import division #imports floating point division
import numpy #imports array stuff

def probrank(prob):
#ranks the final results in terms of probability of landing on the square
	total= sum(prob)
	prob=prob/total
	for k in range(len(prob)):
		print "Probability of",k,"is",100*prob[k]
	rank = numpy.argsort(prob)
	print "Probability rank is",rank

def valuerank(prob):
#ranks the final results in terms of probability of landing on the square over cost of the square and 3 houses times rent at 3 houses
	#prob is solved already
	total= sum(prob)
	prob=prob/total
	railrent=100
	railcost=200
	utilityrent=10*7
	rent=[2^32,90,2^32,180,2^32,railrent,
270,2^32,270,300,2^32,450,utilityrent,450,500,railrent,
550,2^32,550,600,2^32,700,2^32,700,750,railrent,
800,800,utilityrent,850,2^32,900,900,2^32,1000,railrent,
2^32,1100,2^32,1400]
	cost=[-1,210,-1,210,-1,railcost,
250,-1,250,370,-1,440,150,440,460,railcost,
480,-1,480,500,-1,670,-1,670,690,railcost,
710,710,150,730,-1,900,900,-1,920,railcost,
-1,950,-1,1000]

	value=100*prob*rent/cost
	#filter out negative values if wanted, messes up indices of positive values
	#value=value[value>0] 
	for k in range(len(value)):
		print "Value of",k,"is",value[k]
	rank = numpy.argsort(value)
	print "Value rank is", rank

def probtravel(arg):
#returns the probability that you will travel a certain distance
#probabilities are symmetric about 7
	if (arg==2 or arg==12):
		return 1/36
	if (arg==3 or arg==11):
		return 2/36
	if (arg==4 or arg==10):
		return 3/36
	if (arg==5 or arg==9):
		return 4/36
	if (arg==6 or arg==8):
		return 5/36
	if (arg==7):
		return 6/36

def proba(arg):
#deals with the rollover, such as the probability of being 3 squares back from Go
	if (arg<0):
		arg+=40
	return prob[arg]

def incprob(arg):
#arg runs from 0 to 39
#incprob is the probability you end up at square arg
#makes calls to probtravel to determine the prob of moving a certain number of spaces
#and proba to deal with the rollover
	chance = proba(7)+proba(22)+proba(36)
	commchest=proba(2)+proba(17)+proba(33)
	probcurr=probtravel(2)*(proba(arg-2)+proba(arg-12)) + probtravel(3)*(proba(arg-3)+proba(arg-11)) + probtravel(4)*(proba(arg-4)+proba(arg-10))+probtravel(5)*(proba(arg-5)+proba(arg-9))+probtravel(6)*(proba(arg-6)+proba(arg-8))+probtravel(7)*proba(arg-7)

	#account for special chances
	if (arg==0):#move to Go
		probcurr+=(1/16)*chance + (1/16)*commchest
	if (arg==5):#go to nearest railroad(2 cards)&go to reading railroad
		probcurr+=(1/16)*chance+(2/16)*proba(36)
	if (arg==10):#go to jail
		probcurr+=(1/16)*chance + proba(30)
	if (arg==11):#go to St. Charles
		probcurr+=(1/16)*chance
	if (arg==12):#go to nearest utility
		probcurr+=(1/16)*proba(7)+(1/16)*proba(36)
	if (arg==28):#go to nearest utility
		probcurr+=(1/16)*proba(22)
	if (arg==39):#go to boardwalk
		probcurr+=(1/16)*chance
	if (arg==24):#go to illinois
		probcurr+=(1/16)*chance
	if (arg==25):#go to nearest railroad
		probcurr+=(2/16)*proba(22)
	if (arg==15):#go to nearest railroad
		probcurr+=(2/16)*proba(7)
	if (arg==4):#go back 3 spaces
		probcurr+=(1/16)*proba(7)
	if (arg==19):#go back 3 spaces
		probcurr+=(1/16)*proba(22)
	if (arg==33):#go back 3 spaces
		probcurr+=(1/16)*proba(36)
	
	if(arg==7 or 22 or 36):#if you land on chance, 10/16 chance you move somewhere else
		probcurr *= 6/16
	if (arg==2 or 17 or 33):#if you land on cc, 1/16 chance you move to go
		probcurr*=15/16
	return probcurr

def main():
	for i in range(0, 100):
		for j in range(0,40):
			probcurr[j]=incprob(j)
		for h in range(0,40):
			prob[h]=probcurr[h]
	probrank(prob)
	valuerank(prob)

columns=40
startprob=1/columns
prob=numpy.empty(columns)
probcurr=numpy.empty(columns)
prob.fill(startprob)
probcurr.fill(startprob)
main()
