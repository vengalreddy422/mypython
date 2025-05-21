#ForLoopEx2.py
s="PYTHON"
print("By using For Loop--Forward Direction wihout Indices")
for ch in s:
    print("\t{}".format(ch))
print("------------------------------------------")
print("By using For Loop--Backward Direction wihout Indices")
for ch in s[::-1]:
    print("\t{}".format(ch))
print("------------------------------------------")
print("By using For Loop--Forward Direction with +Ve Indices")
for i in range(0,len(s)):
    print("\t{}".format(s[i]))
print("------------------------------------------")
print("By using For Loop--Forward Direction with -VE Indices")
for i in range(-len(s),0):
    print("\t{}".format(s[i]))
print("------------------------------------------")
print("By using For Loop--Backward Direction with -VE Indices")
for i in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[i]))
print("------------------------------------------")
