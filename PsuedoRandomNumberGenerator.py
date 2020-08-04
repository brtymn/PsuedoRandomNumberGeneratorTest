import time ## This module is used to capture the current time in miliseconds at the beginning.
import matplotlib.pyplot as plt ## This module is used for plotting the histogram.

## Function to convert a list to an integer.
def Convert(list):
    intt = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return(intt)

## pow() function from the math module return a value that ends with ".0" and this is a problem for me to turn it into a list easily. So I defined a function to take care of the problem.
def Squared(numm):
	sqrd = numm * numm
	return sqrd ## Simply returns the squared integer

## This function is defined to check if our seed is even or not.
def EvenOdd(numbb):
	evenodd_list = [] ## If there is one element in this list, the number is odd. If there are two elements in this list, the number is even.
	if (numbb % 2) == 0:
		evenodd_list.append('0')
		evenodd_list.append('1')
	else:
		evenodd_list.append('0')

	return evenodd_list

## This function generates the seeds we use for our random numbers.
def PotentialSeedGenerator():
    sloppy_control_mechanism = 1 ## Unreliable control mechanism here. Basically works as a switch, so it doesnot have to be fancy.
    secondary_switch = 0
    while(secondary_switch == 0):
        while(sloppy_control_mechanism == 1): ## Huge while loop to keep everything working unless our little switch is flipped.
            current_millis = int(round(time.time() * 1000)) ## Capture the current time in miliseconds.
            ##print(current_millis) ## For debugging purposes.

            current_millis_list = [int(x) for x in str(current_millis)] ## Convert the time value to a list of strings.
            ##print(current_millis_list) ## For debugging purposes.
        	## There must be an easier way to do this, but I like it this way since I can see every step.
            current_millis_reversed_list = current_millis_list[::-1] ## Reverse the string for later use.
            ##print(current_millis_reversed_list) ## For debugging purposes.

            potential_seed_reversed = [] ## Create an empty list here to use it for our seed candidate.
			## Extract the first four terms of the reversed list and add it to a list, which is our reversed potential seed
            potential_seed_reversed.append(current_millis_reversed_list[0])
            potential_seed_reversed.append(current_millis_reversed_list[1])
            potential_seed_reversed.append(current_millis_reversed_list[2])
            potential_seed_reversed.append(current_millis_reversed_list[3])
            ##print(potential_seed_reversed) ## For debugging purposes.
			## Reverse the latest list to obtain the potential seed list.
            potential_seed = potential_seed_reversed[::-1]
            ##print(potential_seed) ## For debugging purposes.
            secondary_switch = 1
			## Here is the main control mechanism. Check if there is a zero in our potential seed list.
            for i in potential_seed:
                print(i) ## For debugging purposes.
                if(0 in potential_seed) :
                    print ("There is a zero!")
                    potential_seed= []
                    secondary_switch = 0
                    break
                else:
                    sloppy_control_mechanism = 0 ## Flip the little switch here to end the while loop.
                    secondary_switch = 1
                    break ## Break out of the if loop.

    return potential_seed ## This is the output of the function.


def GoOnForNTimes():
	N = int(input("Enter the number of random numbers you want to create:     "))
	dummy = 0
	randoms = []
	while(dummy <= N):
		seed_list = PotentialSeedGenerator() ## Use the function to optain the output.
		seed = Convert(seed_list) ## Finally obtain the seed using the user defined convert() function.
		##print(seed) ## For debugging purposes.

		seed_squared = Squared(seed)
		##print(seed_squared) ## For debugging purposes.
		seed_squared_str_list = [int(x) for x in str(seed_squared)] ## Convert the squared seed into a list of strings.
		##print(seed_squared_str_list) ## For debugging purposes.

		evenorodd_list = EvenOdd(seed)
		extra_randomizer = len(evenorodd_list)
		##print(extra_randomizer) ## For debugging purposes.

		middle_four_of_squared = [] ## Empty list to hold the middle four elements of our squared seed.

 ## HUUUUUGE note here: If the squared seed has 8 elements, there is no problem. We can just take the middle four elements. HOWEVER, if the squared seed has 7 elements it is a problem for us. So I decided to add an extra layer just for fun. I defined the "even or odd function" and created this variable called "extra_randomizer" which takes the value of "1" if the seed is odd and takes the value of "2" if the seed is odd. Since we can't take the middle four elements of a list that contains seven elements, I decided to take the elements [1], [2], [3], [4] if the seed is odd and take the elements [2], [3], [4], [5] if the seed is even.
		if(len(seed_squared_str_list) == 8):
				middle_four_of_squared.append(seed_squared_str_list[2])
				middle_four_of_squared.append(seed_squared_str_list[3])
				middle_four_of_squared.append(seed_squared_str_list[4])
				middle_four_of_squared.append(seed_squared_str_list[5])
		elif(len(seed_squared_str_list) == 7 and extra_randomizer == 1):
				middle_four_of_squared.append(seed_squared_str_list[1])
				middle_four_of_squared.append(seed_squared_str_list[2])
				middle_four_of_squared.append(seed_squared_str_list[3])
				middle_four_of_squared.append(seed_squared_str_list[4])
		elif(len(seed_squared_str_list) == 7 and extra_randomizer == 2):
				middle_four_of_squared.append(seed_squared_str_list[2])
				middle_four_of_squared.append(seed_squared_str_list[3])
				middle_four_of_squared.append(seed_squared_str_list[4])
				middle_four_of_squared.append(seed_squared_str_list[5])

		the_middle_four = Convert(middle_four_of_squared) ## Use the previously defined Convert() function to convert the list to an integer.
		randoms.append(the_middle_four) ## Add all of the random numbers to our empty list.
		##print(middle_four_of_squared) ## For debugging purposes.

		sleep_duration = the_middle_four / 100000 ## This is another extra layer of unnecessary complication I added for fun. I needed a float for my sleep funtion and I decided to use the random number we created instead of giving it a fixed value.
		time.sleep(sleep_duration) ## Function executes too fast and gets the same time in miliseconds multiple times. Therefore we need it to wait for some time.

		dummy += 1 ## I increase my dummy variable by one here. This is necessary to "count" to 500. No idea if there is another way to "count" to a certain value.

	##print(the_middle_four) ## For debugging purposes.
	return randoms ## Outputs our list of random numbers.

## This function is used to plot histograms. It uses the "matplotlib" module.
def PlotHistogram(x):
	number_of_bins = int(input("Enter the number of bins that will be used for the histogram:   ")) ## I wanted the user to decide the number of bins.
	plt.style.use('fivethirtyeight') ## I added this because I thought this looked cool. This changes the histogram style, mainlyits colors.
	plt.hist(x, bins = number_of_bins) ## This is the command that plots our histogram.
	plt.show() ## This command shows the plot as the name suggests.

## This is the driver function of the code. I saw the usage of this "main()" function in stackoverflow and reallyliked it. I thought it would be cool if I organized everything to be inside a user defined function.
def main():
	rand = GoOnFor500Times() ## Execute the function that returns 500 numbers.
	PlotHistogram(rand) ## Plot our histogram


main() ## Finally execute the "main()" function to run the code.
