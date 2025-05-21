#SubFunEx.py
import re
txt = "The rain in Spain"
x = re.sub(r"\s", "->", txt)
print(x)