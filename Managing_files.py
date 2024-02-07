#Reading and Writing Files

#Let's say we have a text file containing current visitors at a hotel. We'll call it, guests.txt.
#Now suppose we want to update our file as guests check in and out.
#The current names in the guests.txt file should be: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.
#Now let's remove the guests that have checked out already. There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:
#1.Open the file in "read" mode.
#2.Iterate over each line in the file and put each guest's name into a Python list.
#3.Open the file once again in "write" mode.
#4.Add each guest's name in the Python list to the file one by one.
#The current names in the guests.txt file should be: Bob, Polly, Sam, Danielle and Jacob.
#Now let's check whether Bob and Andrea are still checked in

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)
