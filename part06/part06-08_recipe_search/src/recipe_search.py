# write your solution here
def read_recipes(filename: str):
    recipes = []
    current_recipe = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line != "":
                if "name" not in current_recipe:
                    current_recipe["name"] = line
                elif "time" not in current_recipe:
                    current_recipe["time"] = int(line)
                else:
                    if "ingredients" not in current_recipe:
                        current_recipe["ingredients"] = []
                    current_recipe["ingredients"].append(line)
            else:
                recipes.append(current_recipe)
                current_recipe = {}

        recipes.append(current_recipe)

    print(recipes)
    return recipes


def search_by_name(filename: str, word: str):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
    return found


def search_by_time(filename: str, time: int):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        if time >= recipe["time"]:
            found.append(f"{recipe['name']}, preparation time {recipe['time']} min")
    return found


def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['time']} min")
    return found


if __name__ == "__main__":
    read_recipes("recipes1.txt")
