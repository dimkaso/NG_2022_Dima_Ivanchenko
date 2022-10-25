import pandas as pd # Standard Library
Str = str(input("Enter a word to get an answer : ")) # entered value
Str_list = Str
Str_list = list(Str)

print(pd.value_counts(Str_list))



# Str_list.sort() \\Doesn't sort alphabetically
#HELP ME 
