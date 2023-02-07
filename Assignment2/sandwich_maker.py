
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        #checks for ingredients and compares it to resources, false if ingredients is more than resources
        if(ingredients>= self.machine_resources):
            return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.sandwich_size = sandwich_size
        self.order_ingredients = order_ingredients