import time 
start_time = time.time() #start counting process
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#first algorithm :first algorithm run time: 18.1 s | a bit faster than second algorithm.
'''
hundred_thousand = []
for value in range(1,100_001):
    print(value)
    hundred_thousand.append(value)
print("End Process :]")
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Second algorithm: second algorithm run time:18.6 s | is a bit slower than first algorithm.
'''
hundred_thousand = list(range(1,100_001))
for i in range(1,100_001):
    j = i-1
    print(hundred_thousand[j])
print("end process :CC")
'''

end_time = time.time() # end counting process
elapsed_time = end_time - start_time #find total time of each algorithm used for finish the task.
print(f"Elapsed time: {elapsed_time} seconds")
    
