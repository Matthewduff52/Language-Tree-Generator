test_phrase = "hoj kʰos qulgʷeltos snesowt qūsten"
# should become hɔj kəɾos qʊlgʷɛltos ɛsnesowt qūsteŋ
new_phrase = " " + test_phrase + " "

with open('changes.txt', 'r', encoding="utf8") as file:
    file_content = file.read()
    commands = file_content.split()

    x = 0
    while x < len(commands):
        match commands[x+2]:
            case "_l":
                new_phrase = new_phrase.replace(commands[x+0]+"l",commands[x+1]+"l")
            case "_r":
                new_phrase = new_phrase.replace(commands[x+0]+"r",commands[x+1]+"r")
            case "_j":
                new_phrase = new_phrase.replace(commands[x+0]+"j",commands[x+1]+"j")
            case "_w":
                new_phrase = new_phrase.replace(commands[x+0]+"w",commands[x+1]+"w")
            case "#_":
                new_phrase = new_phrase.replace(" "+commands[x+0]," "+commands[x+1])
            case "_#":
                new_phrase = new_phrase.replace(commands[x+0]+" ",commands[x+1]+" ")
            case "V_V": # WIP
                new_phrase = new_phrase.replace("əo","ə"+commands[x+1]+"o")
            case _:
                pass
        x += 3
        
    new_phrase = new_phrase.replace(".","")
    print(test_phrase)
    print(new_phrase.strip())
