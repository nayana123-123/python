color_list1=input("Enter colors for list1:").split(',')
color_list2=input("Enter colors for list2:").split(',')

color_list1=[color.strip() for color in color_list1]
color_list2=[color.strip() for color in color_list2]
diff_colors=[color for color in color_list1 if color not in color_list2]

if diff_colors:
    print("colors in list1 not in list2:",','.join(diff_colors))
else:
    print("All colors in list1 are present in list2")
