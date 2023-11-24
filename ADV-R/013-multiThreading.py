import threading
import subprocess

def print_numbers():
    for i in range(1,6):
        print("Number is:", i) 

def print_chars():
    # for char in 'abcde':
    #     print("Character is:", char) 
    subprocess.run(["sleep", "20"], capture_output=True, text=True) # This makes thread 2 to take more time, even thought t1 is complted , it has to wait for t1

# Just Prints
# print_numbers()
# print_chars()

# We are creating threads and they will be on waiting state
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_chars)

# Starts the created threads which are in waiting state 
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
#If you run both of them would run parallel.
