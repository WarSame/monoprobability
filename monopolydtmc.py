#Monopoly Steady State Probability Solver
#Created by Graeme Cliffe
#Use: determine which monopoly squares are the most useful to own at n houses
#This allows for more informed trades
#It also allows for planning for future board states(i.e. Boardwalk falling off)
#It is a demonstration of me going way too hardcore into a basic boardgame
#But it was fun

from __future__ import division #imports floating point division
import numpy #imports array stuff
#import math #imports math operations

#Allows properties to be named by simply referencing this array
propertynames=["Go","Mediterranean Avenue","Community Chest(2)","Baltic Avenue","Income Tax","Reading Railroad","Oriental Avenue","Chance(7)","Vermont Avenue","Connecticut Avenue","Jail","St. Charles Place","Electric Company","States Avenue","Virginia Avenue","Pennsylvania Railroad","St. James Place","Community Chest(17)","Tennessee Avenue","New York Avenue","Free Parking","Kentucky Avenue","Chance(22)","Indiana Avenue","Illinois Avenue","B. & O. Railroad","Atlantic Avenue","Ventnor Avenue","Water Works","Marvin Gardens","Go To Jail","Pacific Avenue","North Carolina Avenue","Community Chest(33)","Pennsylvania Avenue","Short Line","Chance(36)","Park Place","Luxury Tax","Boardwalk"]

def probrank(prob):
#ranks the final results in terms of probability of landing on the square
#and nicely formats/prints the probabilities and ranking
	print "===========Probability==========="
	for k in range(len(prob)):
		print "Probability of",propertynames[k],"is",prob[k]
	rank = numpy.argsort(prob)
	print "===========Ranked Probability==========="
	counter=0
	for i in range(len(rank)):
		if (prob[rank[i]]>0):
			print "Rank probability of",propertynames[rank[i]],"is",counter
			counter+=1

def valuerank(prob,numhouses,railowned,utilityowned):
#ranks the final results in terms of probability of landing on the square over cost of the square and n houses times rent at n houses
#and nicely formats/prints the probabilities and ranking
	if (numhouses<0 or numhouses>5 or railowned<0 or railowned>4 or utilityowned<0 or utilityowned>2):
		print "You need to enter the proper number of owned properties or houses"
		return -1

	railrent=0
	if (railowned==1):
		railrent=25
	elif (railowned==2):
		railrent=50
	elif (railowned==3):
		railrent=100
	elif (railowned==4):
		railrent=200

	#the expected roll(7) is used
	utilityrent=0
	if (utilityowned==1):
		utilityrent=4*7
	elif (utilityowned==2):
		utilityrent=10*7

	#multiplier rows are number of houses, columns are multiplier for that property type(i.e. brown regular, brown super)
	multiplier=[(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(5,5,5,5,5,5,5,5,5,5,5,5,5,150/28,5,4),(15,15,15,100/8,15,15,200/14,220/16,250/18,15,15,15,15,420/28,500/35,12),(45,45,45,300/8,45,500/12,550/14,600/16,700/18,750/20,800/22,850/24,900/26,1000/28,1100/35,28),(80,80,200/3,450/8,62.5,700/12,750/14,800/16,875/18,925/20,975/22,1025/24,1100/26,1200/28,1300/35,34),(125,112.5,550/6,600/8,75,900/12,950/14,1000/16,1050/18,1100/20,1150/22,1200/24,1275/26,1400/28,1500/35,40)]

	rent=[2^31,2*multiplier[numhouses][0] #mediterranean avenue,1
,2^31,4*multiplier[numhouses][1] #baltic avenue,3
,2^31,railrent,6*multiplier[numhouses][2] #oriental avenue,6
,2^31,6*multiplier[numhouses][2] #vermont avenue, 8
,8*multiplier[numhouses][3] #connecticut avenue, 9
,2^31,10*multiplier[numhouses][4] #st charles place, 11
,utilityrent,10*multiplier[numhouses][4] #states avenue, 13
,12*multiplier[numhouses][5] #virginia avenue, 14
,railrent,14*multiplier[numhouses][6] #st james place, 16
,2^31,14*multiplier[numhouses][6] #tennessee avenue, 18
,16*multiplier[numhouses][7] #new york avenue, 19
,2^31,18*multiplier[numhouses][8] #kentucky avenue, 21
,2^31,18*multiplier[numhouses][8] #indiana avenue, 23
,20*multiplier[numhouses][9] #illinois avenue, 24
,railrent,22*multiplier[numhouses][10] #atlantic avenue, 26
,22*multiplier[numhouses][10] #ventnor avenue, 27
,utilityrent,24*multiplier[numhouses][11] #marvin gardens, 29
,2^31,26*multiplier[numhouses][12] #pacific avenue, 31
,26*multiplier[numhouses][12] #north carolina avenue, 32
,2^31,28*multiplier[numhouses][13] #pennsylvania avenue, 34
,railrent, 2^31,35*multiplier[numhouses][14] #park place, 37
,2^31,50*multiplier[numhouses][15] #boardwalk, 39
]

	housecostgroup1=50
	housecostgroup2=100
	housecostgroup3=150
	housecostgroup4=200
	cost=[-1,60+numhouses*housecostgroup1#mediterranean avenue, 1
,-1,60+numhouses*housecostgroup1 #baltic avenue, 3
,-1,200,100+numhouses*housecostgroup1#oriental avenue, 6
,-1,100+numhouses*housecostgroup1#vermont avenue, 8
,120+numhouses*housecostgroup1 #connecticut avenue, 9
,-1,140+numhouses*housecostgroup2#st charles place, 11
,150,140+numhouses*housecostgroup2#states avenue, 13
,160+numhouses*housecostgroup2#virginia avenue, 14
,200,180+numhouses*housecostgroup2#st james place, 16
,-1,180+numhouses*housecostgroup2#tennessee avenue, 18
,200+numhouses*housecostgroup2 #new york avenue, 19
,-1,220+numhouses*housecostgroup3 #kentucky avenue, 21
,-1,220+numhouses*housecostgroup3 #indiana avenue, 23
,240+numhouses*housecostgroup3 #illinois avenue, 24
,200,260+numhouses*housecostgroup3 #atlantic avenue, 26
,260+numhouses*housecostgroup3 #ventnor avenue, 27
,150,280+numhouses*housecostgroup3 #marvin gardens, 29
,-1,300+numhouses*housecostgroup4 #pacific avenue, 31
,300+numhouses*housecostgroup4 #north carolina avenue, 32
,-1,320+numhouses*housecostgroup4 #pennsylvania avenue, 34
,200,-1,350+numhouses*housecostgroup4 #park place, 37
,-1,400+numhouses*housecostgroup4 #boardwalk, 39
]

	value=100*prob*rent/cost
	print "===========Values==========="
	for k in range(len(value)):
		if (value[k]>0):
			print "Value of",propertynames[k],"is",value[k]
	rank = numpy.argsort(value)

	print "===========Ranked Values==========="
	counter=0
	for i in range(len(rank)):
		if (value[rank[i]]>0):
			print "Rank value of",propertynames[rank[i]],"is",counter
			counter+=1

def probtravel(arg):
#returns the probability that you will travel a certain distance
#probabilities are symmetric about 7
	if (arg==2 or arg==12):
		return 1/36
	elif (arg==3 or arg==11):
		return 2/36
	elif (arg==4 or arg==10):
		return 3/36
	elif (arg==5 or arg==9):
		return 4/36
	elif (arg==6 or arg==8):
		return 5/36
	elif (arg==7):
		return 6/36

def proba(prob,arg):
#deals with the rollover, such as the probability of being 3 squares back from Go
	if (arg<0):
		arg+=40

	if(arg==7 or arg==22 or arg==36):#if you land on chance, 10/16 chance you move somewhere else
		return prob[arg]* 6/16
	if (arg==2 or arg==17 or arg==33):#if you land on cc, 1/16 chance you move to go
		return prob[arg]*15/16
	if (arg==30):
		return 0

	return prob[arg]

def incprob(prob,arg):
#arg runs from 0 to 39
#incprob is the probability you end up at square arg
#makes calls to probtravel to determine the prob of moving a certain number of spaces
#and proba to deal with the rollover

#basic sanity checking
	if (arg<0 or arg>40):
		print "Your argument for incprob was outside of the allowed range"
		return -1	
	
	chance = prob[7]+prob[22]+prob[36]
	commchest=prob[2]+prob[17]+prob[33]
	probcurr=probtravel(2)*(proba(prob,arg-2)+proba(prob,arg-12)) + probtravel(3)*(proba(prob,arg-3)+proba(prob,arg-11)) + probtravel(4)*(proba(prob,arg-4)+proba(prob,arg-10))+probtravel(5)*(proba(prob,arg-5)+proba(prob,arg-9))+probtravel(6)*(proba(prob,arg-6)+proba(prob,arg-8))+probtravel(7)*proba(prob,arg-7)

	#account for special chances
	#python doesn't have case/switch like C :/
	if (arg==0):#move to Go
		probcurr+=(1/16)*chance + (1/16)*commchest
	elif (arg==5):#go to nearest railroad(2 cards)&go to reading railroad
		probcurr+=(1/16)*chance+(2/16)*prob[36]
	elif (arg==10):#go to jail
		probcurr+=(1/16)*chance + prob[30]
	elif (arg==11):#go to St. Charles
		probcurr+=(1/16)*chance
	elif (arg==12):#go to nearest utility
		probcurr+=(1/16)*prob[7]+(1/16)*prob[36]
	elif (arg==28):#go to nearest utility
		probcurr+=(1/16)*prob[22]
	elif (arg==39):#go to boardwalk
		probcurr+=(1/16)*chance
	elif (arg==24):#go to illinois
		probcurr+=(1/16)*chance
	elif (arg==25):#go to nearest railroad
		probcurr+=(2/16)*prob[22]
	elif (arg==15):#go to nearest railroad
		probcurr+=(2/16)*prob[7]
	elif (arg==4):#go back 3 spaces
		probcurr+=(1/16)*prob[7]
	elif (arg==19):#go back 3 spaces
		probcurr+=(1/16)*prob[22]
	elif (arg==33):#go back 3 spaces
		probcurr+=(1/16)*prob[36]

	#basic output checking
	if (probcurr<0):
		print "The returned probability was going to be negative"
		return -1
	return probcurr

def main():
	#initialize the arrays used
	columns=40
	startprob=1/columns
	prob=numpy.empty(columns)
	probcurr=numpy.empty(columns)
	prob.fill(startprob)
	probcurr.fill(startprob)
	#loop through the arrays m times, determining the probabilities from the previous
	#set of probabilities times the transition probabilities
	for i in range(0, 100):
		for j in range(0,40):
			#determine the next set of probabilities from the previous set
			probcurr[j]=incprob(prob,j)
		for h in range(0,40):
			#reset the next set to be the current set for the next iteration
			prob[h]=probcurr[h]
	#rank properties based upon probability of landing on them
	probrank(prob)
	#rank properties based upon value, determined by rent at n houses times the
	#probability of landing on it, divided by the cost of property and n houses
	#railowned and utilityowned are number of railroads and utilities owned, respectively
	#numhouses is the number of houses assumed for properties
	railowned=4
	utilityowned=2
	numhouses=1
	valuerank(prob,numhouses,railowned,utilityowned)


main()
