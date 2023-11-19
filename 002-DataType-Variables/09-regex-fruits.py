import re

text = "apple,banana,orange,grape"
pattern = ","

split_result = re.text(pattern , text)
print("Result after split:" , split_result)