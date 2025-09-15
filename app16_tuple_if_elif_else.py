month = int(input("What month is it?: Select (1-12)"))
if month in (1, 2, 3):
    print("Winter")
if month in (4, 5, 6):
    print("Spring")
if month in (7, 8, 9):
    print('Summer')
if month in (10, 11, 12):
    print('Autumn')
else:
    print('Select 1-12')
