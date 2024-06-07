current_users = ['nine','tor','kung','feaung','yuu'] #define current user list.
new_users = ['Nine','pai','pun','poom','park'] #define enw user list.

current_users_lower = [] #use loop to convert current user list to lowercase.
for user in current_users:
    current_users_lower.append(user.lower()) # add new loop item with lowercase to new list.

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print( "Sorry " +'"'+ new_user+'"' + " this username is already exists")
    else:
        print("Nice " + '"'+new_user+ '"' + " this username is still avialable.")

#-----------------------------------------------------------------------------------------------------------------------------------------

current_users = ['nine','tor','kung','feaung','yuu']
new_users = ['Nine','pai','pun','park','poom']

#convert items in current_users list to lowercase in condition that user use upper or titlecase.
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " +'"'+new_user+'"'+ " this name already exits.")
    else:
        print("Great!!! "+'"'+new_user+'"'+" this name are still avialable.")
