import re

text = "The quick red fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "blue"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)