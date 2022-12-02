s = input()
print(["No", "Yes"][2*s.lower().count("z") == s.lower().count("o")])
