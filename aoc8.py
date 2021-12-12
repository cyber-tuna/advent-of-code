import random
import time

random.seed(time.time())

true_a_sets = []
true_b_sets = []
true_c_sets = []
true_d_sets = []
true_e_sets = []
true_f_sets = []
true_g_sets = []

true_mapping = {
    "abcefg" : "0",
    "cf" : "1" ,
    "acdeg" : "2",
    "acdfg" : "3",
    "bcdf" : "4",
    "abdfg" : "5",
    "abdefg" : "6",
    "acf" : "7",
    "abcdefg" : "8",
    "abcdfg" : "9" 
}

lines = []
with open("input8.txt", "r") as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    left = line.split('|')[0].strip().split(' ')

    run = True
    while run:
        true_a_sets.clear()
        true_b_sets.clear()
        true_c_sets.clear()
        true_d_sets.clear()
        true_e_sets.clear()
        true_f_sets.clear()
        true_g_sets.clear()

        five_len_list = [2,3,5]
        six_len_list = [0,6,9]

        for word in left:
            s = (set([letter for letter in word]))
            if len(word) == 2: # must be a 1
                true_c_sets.append(s)
                true_f_sets.append(s)
            elif len(word) == 3: # must be a 7
                true_a_sets.append(s)
                true_c_sets.append(s)
                true_f_sets.append(s)
            elif len(word) == 4: # must be a 4
                true_b_sets.append(s)
                true_c_sets.append(s)
                true_d_sets.append(s)
                true_f_sets.append(s)
            elif len(word) == 5: # must be 2, 3 or 5
                random.shuffle(five_len_list)
                i = five_len_list.pop()
                if i == 2: # assume 2
                    true_a_sets.append(s)
                    true_c_sets.append(s)
                    true_d_sets.append(s)
                    true_e_sets.append(s)
                    true_g_sets.append(s)
                elif i == 3: # assume 3
                    true_a_sets.append(s)
                    true_c_sets.append(s)
                    true_d_sets.append(s)
                    true_f_sets.append(s)
                    true_g_sets.append(s)
                elif i == 5: # assume 5
                    true_a_sets.append(s)
                    true_b_sets.append(s)
                    true_d_sets.append(s)
                    true_f_sets.append(s)
                    true_g_sets.append(s)
            elif len(word) == 6: # must be 0, 6, or 9
                random.shuffle(six_len_list)
                i = six_len_list.pop()
                if i == 0: # assume 0
                    true_a_sets.append(s)
                    true_b_sets.append(s)
                    true_c_sets.append(s)
                    true_e_sets.append(s)
                    true_f_sets.append(s)
                    true_g_sets.append(s)
                elif i == 6: # assume 6
                    true_a_sets.append(s)
                    true_b_sets.append(s)
                    true_d_sets.append(s)
                    true_e_sets.append(s)
                    true_f_sets.append(s)
                    true_g_sets.append(s)
                elif i == 9: # assume 9
                    true_a_sets.append(s)
                    true_b_sets.append(s)
                    true_c_sets.append(s)
                    true_d_sets.append(s)
                    true_f_sets.append(s)
                    true_g_sets.append(s)

        if true_a_sets:
            i_a = set.intersection(*true_a_sets)
        if true_b_sets:
            i_b = set.intersection(*true_b_sets)
        if true_c_sets:
            i_c = set.intersection(*true_c_sets)
        if true_d_sets:
            i_d = set.intersection(*true_d_sets)
        if true_e_sets:
            i_e = set.intersection(*true_e_sets)
        if true_f_sets:
            i_f = set.intersection(*true_f_sets)
        if true_g_sets:
            i_g = set.intersection(*true_g_sets)
        
        if len(i_a) > 0 and len(i_b) > 0 and len(i_c) > 0 and len(i_d) > 0 and len(i_e) > 0 and len(i_f) > 0 and len(i_g)  > 0:
            run = False

        if len(i_a) > 1:
            i_a = (i_a - (i_b | i_c | i_d | i_e | i_f | i_g))
        if len(i_b) > 1:
            i_b = (i_b - (i_a | i_c | i_d | i_e | i_f | i_g))
        if len(i_c) > 1:
            i_c = (i_c - (i_a | i_b | i_d | i_e | i_f | i_g))
        if len(i_d) > 1:
            i_d = (i_d - (i_a | i_b | i_c | i_e | i_f | i_g))
        if len(i_e) > 1:
            i_e = (i_e - (i_a | i_b | i_c | i_d | i_f | i_g))
        if len(i_f) > 1:
            i_f = (i_f - (i_a | i_b | i_c | i_d | i_e | i_g))
        if len(i_g) > 1:
            i_g = (i_g - (i_a | i_b | i_c | i_d | i_e | i_f))

    translation = {
        i_a.pop() : "a",
        i_b.pop() : "b",
        i_c.pop() : "c",
        i_d.pop() : "d",
        i_e.pop() : "e",
        i_f.pop() : "f",
        i_g.pop() : "g"
    }

    right = line.split('|')[1].strip().split(' ')
    num = ""
    for word in right:
        translated = ""

        for char in word:
            translated += translation[char]
        num += true_mapping["".join(sorted(translated))]

    total += int(num)

print("total:", total)




