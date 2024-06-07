#log in system program that will greeting user and it will detect who is in the admins list to have special line.
admins = ['nine','yuu'] #define admins list
user_requested = ['tor','win','nine','pai','kung','yuu'] #list of requested user for log in 

for user in user_requested: #loop through user_log_in list.
    if user in admins: #conditional test if user is a admin.
        print("Welcome back "+ user.title() + " would you like to see rating report?") 
    else: # if not in a admin.
        print("hello, " + user.title() + " how have you been?" )