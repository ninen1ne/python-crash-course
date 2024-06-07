#log in system program same as hello admin program but user request is empty.
user_requested = [] #list of requested user for log in 

if user_requested:
    for user in user_requested: #loop through user_log_in list.
        if user == 'admin': #conditional test if user is a admin.
            print("Welcome back "+ user.title() + " would you like to see rating report?") 
        else:
            print("Hello, " + user.title() +'.')

else:
    print(" We need to find some users!")