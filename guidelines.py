# all times in days unless specified otherwise

NR = "Not Recommended"
INFI = "inf"

TYPES = ['fruit', 'vegetable', 'animal product', 'meat', 'baked good', 'condiment',
         'leftover', 'liquid']
LOCATIONS = ['fridge', 'pantry']

TIME_LENGTHS = list()

temp = dict()
temp['name'] = 'milk'
temp['type'] = 'liquid'
temp['unit'] = None
temp['fridge'] = {'min': "5", 'max': "7"}
temp['pantry'] = {'min': "1 hours", 'max': "1 hours"}
TIME_LENGTHS.append(temp)

temp = dict()
temp['name'] = 'orange juice'
temp['type'] = 'liquid'
temp['unit'] = None
temp['fridge'] = {'min': "5", 'max': "7"}
temp['pantry'] = {'min': "1 hours", 'max': "1 hours"}
TIME_LENGTHS.append(temp)

temp = dict()
temp['name'] = 'apple cider'
temp['type'] = 'liquid'
temp['unit'] = None
temp['fridge'] = {'min': "5", 'max': "7"}
temp['pantry'] = {'min': "1 hours", 'max': "1 hours"}
TIME_LENGTHS.append(temp)

temp = dict()
temp['name'] = "apple"
temp['type'] = "fruit"
temp['unit'] = 150
temp['fridge'] = {'min': "30", 'max': "60"}
temp['pantry'] = {'min': "14", 'max': "30"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "banana"
temp['type'] = "fruit"
temp['unit'] = 120
temp['fridge'] = {'min': "5", 'max': "9"}
temp['pantry'] = {'min': "2", 'max': "7"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "cantaloupe"
temp['type'] = "fruit"
temp['unit'] = 1500
temp['fridge'] = {'min': "7", 'max': "7"}
temp['pantry'] = {'min': "21", 'max': "28"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "grapes"
temp['type'] = "fruit"
temp['unit'] = 5
temp['fridge'] = {'min': "7", 'max': "10"}
temp['pantry'] = {'min': "3", 'max': "5"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "lemon"
temp['type'] = "fruit"
temp['unit'] = 58
temp['fridge'] = {'min': "30", 'max': "60"}
temp['pantry'] = {'min': "14", 'max': "30"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "peach"
temp['type'] = "fruit"
temp['unit'] = 175
temp['fridge'] = {'min': "2", 'max': "5"}
temp['pantry'] = {'min': "7", 'max': "11"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "strawberry"
temp['type'] = "fruit"
temp['unit'] = 18
temp['fridge'] = {'min': "5", 'max': "7"}
temp['pantry'] = {'min': "1", 'max': "2"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "broccoli"
temp['type'] = "vegetable"
temp['unit'] = 225
temp['fridge'] = {'min': "7", 'max': "14"}
temp['pantry'] = {'min': "2", 'max': "2"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "carrot"
temp['type'] = "vegetable"
temp['unit'] = 61
temp['fridge'] = {'min': "28", 'max': "35"}
temp['pantry'] = {'min': "4", 'max': "4"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "cucumber"
temp['type'] = "vegetable"
temp['unit'] = 400
temp['fridge'] = {'min': "7", 'max': "7"}
temp['pantry'] = {'min': "1", 'max': "3"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "green bean"
temp['type'] = "vegetable"
temp['unit'] = 5
temp['fridge'] = {'min': "7", 'max': "7"}
temp['pantry'] = {'min': "1,"+NR, 'max': "1,"+NR}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "lettuce"
temp['type'] = "vegetable"
temp['unit'] = 262
temp['fridge'] = {'min': "7", 'max': "7"}
temp['pantry'] = {'min': "1,"+NR, 'max': "1,"+NR}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "potato"
temp['type'] = "vegetable"
temp['unit'] = 160
temp['fridge'] = {'min': "90", 'max': "120"}
temp['pantry'] = {'min': "30", 'max': "30"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "tomato"
temp['type'] = "vegetable"
temp['unit'] = 115
temp['fridge'] = {'min': "14", 'max': "14"}
temp['pantry'] = {'min': "5", 'max': "7"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "hard cheese"
temp['type'] = 'animal product'
temp['unit'] = None
temp['fridge'] = {'min': "60", 'max': "120"}
temp['pantry'] = {'min': "30", 'max': "90"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "butter"
temp['type'] = 'animal product'
temp['unit'] = 450
temp['fridge'] = {'min': "30", 'max': "90"}
temp['pantry'] = {'min': "10", 'max': "10"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "soft cheese"
temp['type'] = 'animal product'
temp['unit'] = None
temp['fridge'] = {'min': "60", 'max': "120"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "eggs"
temp['type'] = 'animal product'
temp['unit'] = 57
temp['fridge'] = {'min': "21", 'max': "28"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "yogurt"
temp['type'] = "animal product"
temp['unit'] = None
temp['fridge'] = {'min': "14", 'max': "21"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "bacon"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "14", 'max': "14"}
temp['pantry'] = {'min': "2 hours", 'max': "12 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "bologna"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "7", 'max': "14"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "chicken"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "fish"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "ham"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "7", 'max': "7"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "hamburger patty"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "steak"
temp['type'] = "meat"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "2 hours", 'max': "2 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "bread"
temp['type'] = "baked good"
temp['unit'] = None
temp['fridge'] = {'min': "7", 'max': "14"}
temp['pantry'] = {'min': "5", 'max': "7"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "honey"
temp['type'] = "condiment"
temp['unit'] = None
temp['fridge'] = {'min': INFI+","+NR, 'max': INFI+","+NR}
temp['pantry'] = {'min': INFI, 'max': INFI}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "ketchup"
temp['type'] = "condiment"
temp['unit'] = None
temp['fridge'] = {'min': "365", 'max': "365"}
temp['pantry'] = {'min': "365", 'max': "365"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "mayonnaise"
temp['type'] = "condiment"
temp['unit'] = None
temp['fridge'] = {'min': "60", 'max': "365"}
temp['pantry'] = {'min': "60", 'max': "90"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "mac and cheese"
temp['type'] = "leftover"
temp['unit'] = None
temp['fridge'] = {'min': "3", 'max': "5"}
temp['pantry'] = {'min': "10 hours", 'max': "10 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "pizza"
temp['type'] = "leftover"
temp['unit'] = None
temp['fridge'] = {'min': "3", 'max': "4"}
temp['pantry'] = {'min': "10 hours", 'max': "10 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "salad (with dressing)"
temp['type'] = "leftover"
temp['unit'] = None
temp['fridge'] = {'min': "3", 'max': "5"}
temp['pantry'] = {'min': "10 hours", 'max': "10 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "sandwich"
temp['type'] = "leftover"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "10 hours", 'max': "10 hours"}
TIME_LENGTHS.append(temp)


temp = dict()
temp['name'] = "spaghetti (with meatballs)"
temp['type'] = "leftover"
temp['unit'] = None
temp['fridge'] = {'min': "1", 'max': "2"}
temp['pantry'] = {'min': "10 hours", 'max': "10 hours"}
TIME_LENGTHS.append(temp)
