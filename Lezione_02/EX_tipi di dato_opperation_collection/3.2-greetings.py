#EX-3.2
name:list = ["penny:\n","sheldon:\n","leonard:\n","emy farrah fowler:\n"]
mess:list = ["sofice kitty canta kitty bel micino tu...\n","penny,penny,penny\n","penny ti amo <3\n","il contatto tra fidanzati non lo prevede sheldon\n"]
for i in range(len(name)):

    if i == 0:
        print("The Big Bang Theory")
    print(name[i], mess[i])
