a = input()
it = iter(a)
for i in a:
    if i != " ":
        print(next(it), end="")
    else:
        break