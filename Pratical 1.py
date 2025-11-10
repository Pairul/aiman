import random
import time
NUMBER_OF_ELEMENT = 10000

#Create a list
list_1 = list(range(NUMBER_OF_ELEMENT))
random.shuffle(list_1)

#Create a set from the list
set_1 = set(list_1)

# Test if an element is in the set
start_time + time.time() # Get start time
for i in range(NUMBER_OF_ELEMENT):
    i in set_1

    end_time = time.time() #Get end time
    run_time = int (( end_time - start_time ) * 1000) # Get test time
    print("To test if", NUMBER_OF_ELEMENT, "elements are in the set")
    print("--> The runtime is", run_time, "milliseconds")

    #Test if an element is in the list
    start_time = time.time() #Get start time
    for i in range(NumbER_OF_ELEMENT):
        i in list_1

        end_time = time.time() # Get end time
        run_time = int((end_time - start_time ) * 1000) # Get test time
        print("\nTo test if" , NUMBER_OF_ELEMENT, "element are in the list")
        print("--> The runtime is", run_time, "milliseconds")

        #Remove elemet from a set one at a time
        start_time = time.time()
        for i in range(NUMBER_OF_ELEMENT):
            set_1.remove (i)

            end_time = time.time() # Get end time
            run_time = int((end_time - start_time ) * 1000) #Get test time
            print("\nTo remove", NUMBER_OF_ELEMENT, "element are in the set")
            print("--> The runtime is ", run_time , "milliseconds")

            # Remove elements from a list one at a time
            start_time = time.time() #Get start time
            for i in range(NUMBER_OF_ELEMENT):
                list_1.remove(i)

                end_time = time.time() #Get end time
                run_time = int((end_time - start_time ) * 1000) #Get test time
                print("\nTo remove", NUMBER_OF_ELEMENT, "element are in the list")
                print("--> The runtime is ", run_time , "milliseconds")