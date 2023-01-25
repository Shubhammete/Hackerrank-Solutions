def is_leap(year):
   if year <=100000 and year>=1900:
     if year%4 != 0:
       return False
     elif year%4 == 0:
        return True

year = int(input())
print(is_leap(year))
