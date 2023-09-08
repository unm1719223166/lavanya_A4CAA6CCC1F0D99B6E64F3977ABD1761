# to find leapyear
def isLeapyear(year):
  if (year% 4) ==0 and (year % 100)!=0 or (year % 400) == 0:
    return True
  else:
    return False
year =(int(input()))
if isLeapyear(year):
  print("{} is leap year".format(year))
else:
  print("{} is not leap year".format(year))
      