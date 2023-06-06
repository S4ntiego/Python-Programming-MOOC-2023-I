def find_words(search_term: str):
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            if search_term.endswith("*"):
                if word.startswith(search_term[:-1]):
                    words.append(word)
            elif search_term.startswith("*"):
                if word.endswith(search_term[1:]):
                    words.append(word)
            else:
                if len(search_term) == len(word):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            match = False
                            break
                    if match:
                        words.append(word)
    return words
