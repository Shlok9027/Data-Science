str = 'ABC12DC121GJAA3412J829'



alpha = []

num = []

temp_alpha = ""
temp_num = ""



for char in str:
    if char.isalpha():
        if temp_num != "":

            num.append(temp_num)
            temp_num = ""
        temp_alpha += char


    elif char.isdigit():
        if temp_alpha != "":    
            alpha.append(temp_alpha)
            temp_alpha = ""

        temp_num += char



if temp_alpha != "":
    alpha.append(temp_alpha)
if temp_num != "":
    num.append(temp_num)

print('Alphabets:', alpha)
print('Numbers:', num)

