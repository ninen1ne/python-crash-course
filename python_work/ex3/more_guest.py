#3-4 Guest_List: list of guest that i invite for my dinner.
dinner_guest = ['mother','father','sister','gam']
message_mother = f'to {dinner_guest[0].title()}, thanks for your hard work and for every things you have done to me. Would you will come to my dinner mom?'
message_father = f"to {dinner_guest[1].title()}, its been a while since we see each other. do you have any free time for  my dinner dad? "
message_sister = f"to {dinner_guest[2].title()}, even we might seem not love each other that much but i really want you to be happy sis, btw will you come to my dinner?"
message_gam = f"to {dinner_guest[3].title()}, I know i hurt your feeling I'm really sorry about that you are the reason I want to change myself for better person than past me, It's a little bit nervous but would you come to my dinner?"

print(f"hope you are all come, \n{message_mother}\n{message_father}\n{message_sister}\n{message_gam}")
print('number of person i invited: '+ str(len(dinner_guest)))

#3-5 Changing Guest List: changing guest because gam can't come to dinner.
print("guest who can't come to my dinner is " + dinner_guest[3] +".")
del dinner_guest[3]
dinner_guest.insert(3, "kung")

confirm_message = "thanks you"
mother_cf = "I'm glad you accept it."
father_cf = "Thanks dad for come to my dinner."
sister_cf = "Glad to hear that."
kung_cf = "Just as i expect."
print(f"In conclusion guest in our dinner are, \n1-My mother:{mother_cf}\n2-My father:{father_cf}\n3-My sister:{sister_cf}\n4-Kung:{kung_cf}" )
print('number of person i invited: '+ str(len(dinner_guest)))

#3-6 More Guests: invite more 3 people.
print("In the dinner we found a bigger dinner table so now i was looking for extra 3 people to invite. ")
dinner_guest.insert(0, "narutorn")
dinner_guest.insert(2, "tor")
dinner_guest.insert(6, "win")
print(f"come join us bro, \n{dinner_guest[0]}\n{dinner_guest[1]}\n{dinner_guest[2]}\n{dinner_guest[3]}\n{dinner_guest[4]}\n{dinner_guest[5]}\n{dinner_guest[6]}")
print('number of person i invited: '+ str(len(dinner_guest)))

#3-7 Shrinking Guest List:
print("I'm feeling so bad for saying it but the table wasn't arrive in time it's mean we have space for only 2 guests.")
unlucky_guest_1 = dinner_guest.pop()
print(f"I'm really sorry {unlucky_guest_1}.")
unlucky_guest_2 = dinner_guest.pop()
print(f"Maybe another time {unlucky_guest_2}.")
unlucky_guest_3 = dinner_guest.pop()
print(f"I'm really sorry {unlucky_guest_3}.")
unlucky_guest_4 = dinner_guest.pop()
print(f"Maybe another time {unlucky_guest_4}.")
unlucky_guest_5 = dinner_guest.pop()


print("you 2 still got invite: ",dinner_guest[0],",", dinner_guest[1])
print('number of person i invited: '+ str(len(dinner_guest)))

del dinner_guest[1]
del dinner_guest[0]

print(dinner_guest)
print('number of person i invited: '+ str(len(dinner_guest)))


