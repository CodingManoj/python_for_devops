import re

text = "apple,banana,orange,grape"
pattern = ","

split_result = re.split(pattern , text)
print("Result after split:" , split_result)