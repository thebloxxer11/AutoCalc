#Calculations Library
# Imports
import json

class Node(object):
    def __init__(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass

# Process Block
# To Define:
# recipe = Recipe(recipe)
# machine = Machine(recipe, recipe.jsonData["type"], tier)
class ProcessBlock(Node):
    def __init__(self, recipe, type, tier):
        self.type = type
        self.speed = self.setTier(tier)
        self.recipe = {}
        with open(f"references/recipes/{recipe}.json") as file:
            self.recipe = json.load(file)
        pass

    def setTier(self,tier):
        match self.type, tier:
            case 0, 0: return 0.75
            case 0, 2: return 1.5
            case 1, 1: return 2
            case 2, 1: return 2
            case _, _: return 1
# Resource Block
# Miners, Pumps, and Oil Extractors
class ResourceBlock(Node):
    def __init__(self, typeExtractor, typeResource, tier=1, modVeinUtilLevel=0):
        self.typeExtractor = typeExtractor
        self.speed = self.setTier(tier) + (0.1*modVeinUtilLevel)
        self.typeResource = typeResource
        pass

    def setTier(self, tier):
        if self.type == 0 and tier == 0: return 0
        else: return 1

