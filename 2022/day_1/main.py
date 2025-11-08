list_ = open("input.txt").read().split('\n')

index = 0
elf_list = []
elf_total = []
for i in range(len(list_)):
    if(list_[i] == ""):
        calories = list(map(int,list_[index:i]))
        elf_list.append(calories)
        elf_total.append(sum(calories))
        index = i + 1

max_list = []
for i in range(3):
    max_value = max(elf_total)
    max_index = elf_total.index(max(elf_total))
    max_list.append(max_value)
    del elf_total[max_index]

print(max_list)
print(sum(max_list))