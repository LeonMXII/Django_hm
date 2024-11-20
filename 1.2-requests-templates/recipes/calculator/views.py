from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'shava': {
        'лаваш, шт': 1,
        'курица, г': 0.3,
        'огурец, г': 0.070,
        'помидор, г': 0.075,
        'лук, г': 0.05,
        'соус, г': 0.1,
    },

}

def recipe_all(request, dish):
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
        if servings <= 0:
            raise ValueError("Ушли в минус:)")
    except ValueError:
        return render(request, 'calculator/index.html', {'recipe': None})


    recipe = DATA.get(dish)

    if not recipe:
        return render(request, 'calculator/index.html', {'recipe': None})

    scaled_recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}

    context = {
        'recipe': scaled_recipe
    }

    return render(request, 'calculator/index.html', context)
