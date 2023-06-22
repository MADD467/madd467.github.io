# CODER UN CHATBOT qui pourra t'entrainer au HINDI

for i in range(7):
    score = 0

    question1 = "Aap kaa naam kyaa hai ?/ Comment tu t'appelles ?"
    response1 = "Meraa name Madane hai, aap se milkar kushi hui"
    print(question1)
    response11 = input("Response: ")

    if response11 == response1:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)

    question2 = "Aapakee aayu kitanee hai ?/ Quel age as tu ?"
    response2 = "Main bees(20) saal ka hoon / J'ai vingt ans"
    print(question2)
    response22 = input("Response: ")

    if response22 == response2:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)

    question3 = "Aap kyaa karte hain ? / Qu'est ce que tu fais dans la vie ?"
    response3 = "Main videshee bhaashaon ka chhaatr hoon / Je suis étudiant en langues étrangères"
    print(question3)
    response33 = input("Response: ")

    if response33 == response3:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)

    question4 = "Main dekhata hoon... aur aap kaun see bhaashaen bolate(se prononce:'bolte') hain ? / Je vois... et quel langues parlez-vous ?"
    response4 = "Main angrejee, spanish, french aur tamil bol sakta hoon aur main hindi seekh raha hoon / Je peux parler anglais, espagnol, francais et tamoul et je suis en train d'apprendre le hindi. "
    print(question4)
    response44 = input("Response: ")

    if response44 == response4:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)

    question5 = "Main prabhaavit hoon, aap bahut achchhee Hindi bolte hain aur aap kaun see bhaashaen seekhana chaahate hain ? / i am impressed, you speak very well hindi and which languages you want to learn"
    response5 = "Main hindi ke baad russi seekhana chaahoonga / I would like to learn russian after hindi"
    print(question5)
    response55 = input("Response: ")

    if response55 == response5:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)

    question6 = "Phir milenge"
    response6 = "Alvida"
    print(question6)
    response66 = input("Response: ")

    if response66 == response6:
        score = score + 1
        print("CORRECT")
        print(score)
    else:
        score = score - 1
        print("INCORRECT")
        print(score)
        break
