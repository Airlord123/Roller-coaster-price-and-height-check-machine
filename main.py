height = input('\nPlease enter your height in inches and feet:')
age = input('\nplease enter your age: ')
gender = input('\nplease enter your gender :(Male/Female): ')

if float (height) > 4: 
  print('\nenjoy your ride!')
  if int(age) >= 18:
    print('\nplease pay $10')
  elif int(age) > 12 < 18:
    print('\nplease pay $7')
  elif int(age) < 12 :
    if gender == 'Male':
      print('\nMy guy the ride is  free for u,Damn ur tall :)')
    elif gender == 'Female':
      print('\nHey sweet heart the ride is free for u')
else : 
  print('\nSorry this ride might be too dangerous for you u just need some more height')
  





