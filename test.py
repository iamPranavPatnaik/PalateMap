import requests

# Make a GET request to the API
query = input()
r = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q=' + query + '&app_id=f1431fdd&app_key=26d9a654405a30b4a18ddb36216b1046')

# Parse the JSON response
parsed = r.json()

def extract_top_ingredients(data):
    # Extract the ingredients from the top recipe
    if data['hits']:
        top_recipe = data['hits'][0]['recipe']
        if 'ingredientLines' in top_recipe:
            return top_recipe['ingredientLines']
    return []

top_ingredients = extract_top_ingredients(parsed)
print(top_ingredients)
