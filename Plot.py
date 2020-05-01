# creating empty lists 
first = []
last = [] 

 
try:
 # number of elements as input
	n = int(input("Enter number of elements for X-Axis: "))
	print("\t\t\t\t\tEntering first elements")
		# iterating till the range
	for i in range(0, n): 
		list_1 = float(input()) 
		first.append(list_1) # adding the element 
	print("The first entered values are", first) 
	print("\t\t\t\t\tEnter values for Y-axis")
	for j in range(0, n):
		list_2 = float(input())
		last.append(list_2) 
	print("The last entered values are", last)
	print("Received all values, Entering the graph part")
		#Graph Part
	import matplotlib.pyplot as plt
	plt.plot(first, last, linewidth=0.5)
	
	
	#choosing title
	j=input("Do you want to set labels?")
	if j == 'y':		
		a=input("\n\n\nSet name for your graph: ")
		plt.title(a, fontsize = 20)
				#choosing label axes
		x = input("\n\nSet the graph label of first entered values")
		plt.xlabel(x, fontsize = 15)
		y = input("\nSet the graph label of second entered values")
		plt.ylabel(y, fontsize = 15)
	else:
		plt.title("Graph", fontsize = 20)
		plt.xlabel("First", fontsize = 15)
		plt.ylabel("Last", fontsize = 15)

	#setting size of value shown
	plt.tick_params(axis='both', labelsize = 10.5)
	plt.show()
except:
	print("\n\n\t\t\t\t\t\tInvalid Input")
print("Exitting Program.. Thank You")
