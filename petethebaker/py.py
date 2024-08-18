def cakes(recipe, available):
    times = []
    for keys,values in recipe.items():
        if keys not in available:
            return False
        times.append(available[keys] // values )
    return min(times)