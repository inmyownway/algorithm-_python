skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
skill = "CBD"

count=0

for skill_tree in skill_trees:
    str =""
    for s in skill_tree:
        if s in skill:
            str+=s
    print(str)
    if str==skill[:len(str)]:
        count+=1
print(count)


