# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations . You’ll have to think of someone else to invite .
#• Start with your program from Exercise 3-4 . 
# Add a print statement at the end of your program 
# stating the name of the guest who can’t make it .
#• Modify your list, replacing the name of the guest 
# who can’t make it with the name of the new person you are inviting .
# •  Print a second set of invitation messages, 
# one for each person who is still in your list .

dinner_guests = ['Dike', 'Eke', 'Uche', 'Raj', 'Halimat']

message1 = f"Hi {dinner_guests[0]}. Please come to dinner.\n"
message2 = f"Hi {dinner_guests[1]}. Please come to dinner.\n"
message3 = f"Hi {dinner_guests[2]}. Please come to dinner.\n"
message4 = f"Hi {dinner_guests[3]}. Please come to dinner.\n"
message5 = f"Hi {dinner_guests[4]}. Please come to dinner.\n"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

cant_come = 'Eke'
new_person = "Zhang"
print(f"Sorry but {cant_come} cannot attend the dinner.")
dinner_guests[1] = new_person


message1 = f"Hi {dinner_guests[0]}. Please come to dinner.\n"
message2 = f"Hi {dinner_guests[1]}. Please come to dinner.\n"
message3 = f"Hi {dinner_guests[2]}. Please come to dinner.\n"
message4 = f"Hi {dinner_guests[3]}. Please come to dinner.\n"
message5 = f"Hi {dinner_guests[4]}. Please come to dinner.\n"



print(message1)
print(message2)
print(message3)
print(message4)
print(message5)