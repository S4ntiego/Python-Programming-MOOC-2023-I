# Write your solution here
def find_movies(database: list, search_term: str):
    search = []
    for i in range(len(database)):
        if search_term.lower() in database[i]["name"].lower():
            search.append(database[i])
    return search
