
import timeit
from pandas import DataFrame
import matplotlib.pyplot as plt


def userInputValue():
	
	while True:

		try:
			user_input=input("Enter an integer:\n")
			value1=int(user_input)
			break
		except ValueError:
			print("That's not an integer!")
			
	print("Input number value is: {}".format(value1))
	return value1	

	

def power(v1,v2):
	v=pow(v1,v2)
	return v

def squareAndMultiply(v1,v2):
	#this function will first of all convert v2 (exponent) into binary, initialize p (result) 
	#to 1 then apply the square and multiply algorithm, 
	#  p is multiplied by itself (square) when v2[i] is at 0, and when it is at 1 p is multiplied by itself then by v1.
	v2=bin(v2)
	p=1
	for i in range(0, len(v2)):
		p=p*p
		if(v2[i]=="1"):
			p=p*v1
		
	return p

if __name__=="__main__":
	x1 = []
	y1 = []
	y2=[]
	print("/***********************/ Simple algorithm vs Square and multiply /****************************/\n")
	v1=userInputValue()
	v2=userInputValue()
	powerVal=0

	#naive algorithm
	t0=timeit.default_timer() 
	powerVal=power(v1,v2)
	print("{} to the power of {} is : {}".format(v1,v2,powerVal))
	t1=timeit.default_timer()
	total_n = t1-t0
	print("Execution time of Power is: {}".format(total_n*1000))
	
	#square and multiply
	t0=timeit.default_timer() 
	sm=squareAndMultiply(v1,v2)
	print("{} to the power of {} is : {}".format(v1,v2,sm))
	t1=timeit.default_timer()
	total_n = t1-t0
	print("Execution time of SM is: {}".format(total_n*1000))
	
	#compare the two methods, with a base equal to v1, and exponent in the range [521,530]
	#n=[521,530]
	for i in range(521,530):
		x1.append(i)

		t0=timeit.default_timer() 
		powerVal=power(v1,i)
		t1=timeit.default_timer()
		total_n = t1-t0
		total_n=total_n*1000
		y1.append(total_n)#add the exec time of power with n=i to y1
		
		t0=timeit.default_timer() 
		sm=squareAndMultiply(v1,i)
		t1=timeit.default_timer()
		
		total_n = t1-t0
		total_n=total_n*1000
		y2.append(total_n)#add the exec time of square and multiply with n=i to y2

	#The graphs
	Data = {'ValuesPow':x1,'TimeNaive': y1,'TimeSM': y2}
	df = DataFrame(Data,columns=['ValuesPow','TimeNaive','TimeSM'])
	plt.plot( 'ValuesPow', 'TimeNaive', data=df, marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
	plt.plot( 'ValuesPow', 'TimeSM', data=df, marker='o',markerfacecolor='red', markersize=8, color='red', linewidth=2)
	plt.legend()
	print("\\**************************************************************\\")
	
	while True:
		try:
			reply=input("Do you want to view the graph?  [Y\\N]\n")
			if(reply=='Y') or (reply=='N'):
				break
		except:
			reply=input("Do you want to view the graph?  [Y\\N]\n")
	if(reply=='Y'):
		plt.show()
