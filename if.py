is_male= False
is_tall=True
#if is_male or is_tall:
if is_male and is_tall:
    print("take this long jacket")
elif is_male and not(is_tall):
    print("just take the heels")
elif not(is_male) and is_tall:
    print("hey tall woman")
else:
    print("take these heels")