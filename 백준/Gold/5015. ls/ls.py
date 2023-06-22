import fnmatch
pattern = input()
for i in range(int(input())):
    if fnmatch.fnmatch(k:=input(), pattern):
        print(k)