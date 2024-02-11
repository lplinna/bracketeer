import random
import subprocess

b = []
with open("list.txt",'r',encoding='utf-8') as gets:
    b = gets.read().splitlines()

win_bracket = []
lost_bracket = []

start = len(b)-100
end = len(b)

working_range = list(range(start,end))




def linear_victortree(winnernumber,final):
    final.append(f"--{b[winnernumber]}--\n")
    for index,loser in enumerate(tree_of_victors[winnernumber]):
        final.append(((index+1) * ' ') + b[loser]  + "\n")
    

def victortree2(winnernumber,vicd):
    plimbus = list(vicd[winnernumber])
    print(plimbus)
    for i in range(16):
        plimbus = list(map(lambda x: list(vicd[x]) if x in vicd else "?",plimbus))
        plimbus = [item for sublist in plimbus for item in sublist]
        print("quarkus\nquarkus")
        print(len(plimbus))
        print(plimbus)

def victortree3(winnernumber,vicd,stack={}):
    z = winnernumber
    stack[z] = {}
    q = stack[z]
    while z in vicd:
        zlist = list(vicd[z])
        z = zlist[0]
        q[z] = {}
        q = q[z]
        print(b[z])
    print(stack)




while True:
    chosen = input("1 or 2: ")
    if len(working_range) > 1:
        choice_one = random.choice(working_range)
        choice_two = random.choice(working_range)
        while choice_one == choice_two:
            choice_two = random.choice(working_range)
        print(f"Choose between {b[choice_one]}\n and \n {b[choice_two]}")
        if chosen in ["1","2"]:
            loser = choice_two if chosen == "1" else choice_one
            winner = choice_one if chosen == "1" else choice_two
            if loser in working_range:
                lost_bracket.append(loser)
                win_bracket.append(winner)
                working_range.remove(loser)
    else:
        print("end reached")



    if chosen == "load":
        working_range = list(range(start,end))
        oget = open("input.txt")
        get = oget.read().splitlines()
        lost_bracket = get[0].replace("[","").replace("]","").replace(",","").split(" ")
        win_bracket = get[1].replace("[","").replace("]","").replace(",","").split(" ")
        lost_bracket = list(map(lambda x: int(x),lost_bracket))
        win_bracket = list(map(lambda x: int(x), win_bracket))
        #print(lost_bracket)
        #print(working_range)
        for number in lost_bracket:
            if number in working_range:
                working_range.remove(number)
        #print(working_range)
        oget.close()
    if chosen == "cycle":
        load = open("output.txt")
        data = load.read()
        save = open("input.txt",'w')
        save.write(data)
        load.close()
        save.close()
    if chosen == "save":
        put = open("output.txt",'w')
        put.write(f"{str(lost_bracket)}\n{str(win_bracket)}")
        put.close()
    if chosen == "out":
        print(lost_bracket)
        print(win_bracket)
        pause = input("continue?")
    if chosen == "breakdown":
        results = {i:win_bracket.count(i) for i in win_bracket}
        cutoff = input("Cutoff: ")
        for key,value in results.items():
            if value > int(cutoff):
               print(f"{value} -> {b[key]}")
    if chosen == "breakdown2":
        results = {i:win_bracket.count(i) for i in win_bracket}
        cutoff = input("Cutoff: ")
        sorted_items = sorted(results.items(), key=lambda x: x[1])
        statement = ""
        willsave = input("save? Y:N").lower() == "y"
        for item in sorted_items:
            if item[1] > int(cutoff):
                line = f"{item[1]} -> {b[item[0]]}\n"
                statement += line
        if willsave:
            with open("breakdown.txt",'w',encoding='utf-8') as put:
                put.write(statement)
                put.close()


    if chosen == "breakdown3":
        num_wins = {i:win_bracket.count(i) for i in win_bracket}
        sorted_items = sorted(num_wins.items(), key=lambda x: x[1])

        tree_of_victors = {}
        for small_winner in win_bracket:
            index_in_winbracket = [index for index, value in enumerate(win_bracket) if value == small_winner]
            losers = [value for index,value in enumerate(lost_bracket) if index in index_in_winbracket]
            tree_of_victors[small_winner] = reversed(losers)
            
        offset = int(input("Enter starting offset:"))
        offset2 = int(input("Enter ending offset:"))

        
        with open("breakdown.txt",'w',encoding='utf-8') as put:
            final = []
            if offset == offset2:
                linear_victortree(sorted_items[-offset][0],final)
            else:
                for i in range(offset,offset2):
                    linear_victortree(sorted_items[-i][0],final)
            print(''.join(final))
            put.write(''.join(final))
            put.close()

    if chosen == "breakdown4":
        num_wins = {i:win_bracket.count(i) for i in win_bracket}
        sorted_items = sorted(num_wins.items(), key=lambda x: x[1])
        tree_of_victors = {}
        for small_winner in win_bracket:
            index_in_winbracket = [index for index, value in enumerate(win_bracket) if value == small_winner]
            losers = [value for index,value in enumerate(lost_bracket) if index in index_in_winbracket]
            tree_of_victors[small_winner] = reversed(losers)
        victortree3(sorted_items[-1][0],tree_of_victors)


    if chosen == "breakdown5":
        num_wins = {i:win_bracket.count(i) for i in win_bracket}
        top_hundy = []
        for i in range(len(win_bracket)-1,0,-1):
            if len(top_hundy) < 500 and not b[win_bracket[i]] in top_hundy:
                print(f"{num_wins[win_bracket[i]]} -- {b[win_bracket[i]]}")
                top_hundy.append(b[win_bracket[i]])
    
    if chosen == "breakdown6":
        num_wins = {i:win_bracket.count(i) for i in win_bracket}
        num_wins_to_songs = {}
        output = ""
        for key,value in num_wins.items():
            if not value in num_wins_to_songs:
                num_wins_to_songs[value] = []
            else:
                num_wins_to_songs[value].append(key)
        for i in range(max(num_wins_to_songs.keys()),0,-1):
            if i in num_wins_to_songs:
                the_songs = ""
                for song in num_wins_to_songs[i]:
                    the_songs += " | " + b[song] + " | "
                output += f"{i} -- {the_songs}\n"
        with open("breakdown.txt",'w',encoding='utf-8') as put:
                put.write(output)
                put.close()
    
    if chosen == "breakdown7":
        storbo_stack = []
        output = ""
        sevenstart = input("enter start: ")
        if sevenstart == "":
            sevenstart = -1
        else:
            sevenstart = int(sevenstart)
        output += f"\n{b[win_bracket[sevenstart]]}\n"
        for tindex,value in enumerate(win_bracket):
            if value == win_bracket[sevenstart]:
                storbo_stack.append(lost_bracket[tindex])
        output += ("\n//////\n")
        output += ("\n||".join(list(map(lambda x: b[x], storbo_stack))))
        still_winners = True
        while(still_winners):
            tempo = storbo_stack.copy()
            storbo_stack.clear()
            still_winners = False
            stage_winners = []
            stage_dropped = []
            for steve in tempo:
                dropped = True
                for tindex,value in enumerate(win_bracket):
                    if value == steve:
                        still_winners = True
                        dropped = False
                        storbo_stack.append(lost_bracket[tindex])
                if dropped:
                    stage_dropped.append(steve)
                else:
                    stage_winners.append(steve)
                
            output += ("\n///////\n")
            output += ("\n||".join(list(map(lambda x: b[x], stage_winners))))
            output += ("\n--".join(list(map(lambda x: b[x], stage_dropped))))
        with open("breakdown.txt",'w',encoding='utf-8') as put:
            put.write(output)
            put.close()








    if chosen == "check":
        results = {i:lost_bracket.count(i) for i in lost_bracket}
        sorted_items = sorted(results.items(), key=lambda x: x[1])
        for item in sorted_items:
            print(f"{item[1]} -> {b[item[0]]}")

    if chosen == "print":
        number = input("")
        print(b[int(number)])
    #print(f"Projected to crash in {len(b)-1-len(win_bracket)}")
    print(f"Projected to crash in {len(working_range)}")

