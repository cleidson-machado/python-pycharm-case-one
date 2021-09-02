string = "ab1cd1ef"
string = string.replace("1", "")

print(string)
# result: "abcdef"
# Put it in a loop:

a = "a!b@c#d$"
b = "!@#$"
for char in b:
    a = a.replace(char, "")

print(a)
# result: "abcd"

