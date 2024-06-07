#first i create list about math branch i do like or i want to know.
math_branch = ['trigonometry','vector','calculus','algebra','geometry']
# assign a message for every math branch in the list.   
trig_message = f"{math_branch[0].title()}, To be honest i didn't understand it. Maybe i just don't play attention enough."
vector_message = f"{math_branch[1].title()}, It's a very interested subject I'm very excited to learn this field."
calculus_message = f"{math_branch[2].title()}, Thanks to Newton and leibniz to created tool for describe serveral things in nature."
algebra_message = f"{math_branch[3].title()}, It's really though and hard to remember all the formulas but i like to know the core concept and proof it."
geometry_message = f"{math_branch[4].title()}, Don't remember formula all you have to do is just proof and understand it."

#display it on user screen.
print(f"message about math I want to tell you and myself: \n{trig_message} \n{vector_message} \n{calculus_message} \n{algebra_message} \n{geometry_message}")