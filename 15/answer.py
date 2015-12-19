from itertools import combinations_with_replacement
import re

file = open("input.txt")

def read_ingredients(file):
    ingredients = {}

    # test input
    # lines = [
    #     "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    #     "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
    # ]

    for line in file.readlines():
        matches = re.match(r'(\w+): capacity (\-?\d+), durability (\-?\d+), flavor (\-?\d+), texture (\-?\d+), calories (\-?\d+)', line).groups()
        ingredients[matches[0]] = {
            "capacity": int(matches[1]),
            "durability": int(matches[2]),
            "flavor": int(matches[3]),
            "texture": int(matches[4]),
            "calories": int(matches[5])
        }

    return ingredients

def score(ingredients, capacities, count_calories):
    score = {}
    calculated_score = 1
    for ingredient in ingredients:
        for property in ingredients[ingredient]:
            single_score = capacities[ingredient] * ingredients[ingredient][property]

            if property not in score:
                score[property] = 0

            score[property] += single_score

    if count_calories and score["calories"] != 500:
        return 0

    for p in score:
        if p == "calories":
            continue

        if score[p] < 0:
            calculated_score *= 0
        else:
            calculated_score *= score[p]

    return calculated_score

def get_recipe(ingredients, r):
    recipe = {}

    for i in ingredients.keys():
        recipe[i] = r.count(i)

    return recipe

def score_all_recipes(count_calories):
    high_score = 0
    ingredients = read_ingredients(file)
    for r in combinations_with_replacement(ingredients, 100):
        recipe = get_recipe(ingredients, r)
        recipe_score = score(ingredients, recipe, count_calories)
        high_score = max(high_score, recipe_score)

    print high_score

def first_star():
    score_all_recipes(False)

def second_star():
    score_all_recipes(True)

#first_star()
second_star()