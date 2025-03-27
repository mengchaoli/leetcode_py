import re

def convert_title(title):
    title = title.strip()
    number, rest = title.split(". ", 1)
    converted = re.sub(r"[^\w\s\-]", "", rest).replace(" ", "_").lower()
    return f"{number}_{converted}.py"

# 示例
title = "3179. Find the N-th Value After K Seconds"
print(convert_title(title))
