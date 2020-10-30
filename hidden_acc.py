account_number = 114789278
display_number = ""
acc_num = range(len(str(account_number)))

for i in acc_num:
  if i <= 4:
    display_number += "*"
  else:
    display_number += str(account_number)[i]


print(display_number)
