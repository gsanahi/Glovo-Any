import Test

# 
# CODE
# 
sweet_flavour = {"Plain": 0 , "Vanilla" : 5, "ChocolateChip" : 5, "Strawberry" : 10, "Chocolate" : 10}    # Dict (string,int)


def sweet_iceCream(iceCream): # (IceCream) --> int
    return sweet_flavour[iceCream.flavor] + iceCream.num_sprinkles


def sweetest_icecream(iceCreams): # (List [IceCream] ) --> int
    list = []
    for iceCream in iceCreams:
        value = sweet_iceCream(iceCream)
        list.append(value)

    return mayor(list)
    

def mayor(lst): # (List[int]) --> int
    mayor = 0
    for num in lst:
        if num > mayor:
            mayor = num
    return mayor

# 
# FINISH CODE
# 

# 
# TESTS
# 

class IceCream:
	def __init__(self, flavor, num_sprinkles):
		self.flavor = flavor
		self.num_sprinkles = num_sprinkles

ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)
ice6 = IceCream("Chocolate", 23)
ice7 = IceCream("Strawberry", 0)
ice8 = IceCream("Plain", 34)
ice9 = IceCream("Plain", 81)
ice10 = IceCream("Vanilla", 12)

Test.assert_equals(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]), 23)
Test.assert_equals(sweetest_icecream([ice7, ice10, ice1, ice6, ice8, ice10, ice2, ice2]), 34)
Test.assert_equals(sweetest_icecream([ice10, ice10, ice6, ice8, ice4]), 34)
Test.assert_equals(sweetest_icecream([ice2, ice10, ice6, ice9, ice7]), 81)
Test.assert_equals(sweetest_icecream([ice10, ice6, ice4, ice1, ice7, ice8, ice6]), 34)
Test.assert_equals(sweetest_icecream([ice3, ice1]), 23)
Test.assert_equals(sweetest_icecream([ice6, ice7, ice5, ice4, ice3]), 33)
Test.assert_equals(sweetest_icecream([ice4, ice8, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice5, ice7]), 10)
Test.assert_equals(sweetest_icecream([ice5, ice3, ice6, ice2, ice7, ice2, ice7, ice2]), 33)
Test.assert_equals(sweetest_icecream([ice1, ice9, ice10, ice9, ice7, ice1, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice1, ice4]), 23)
Test.assert_equals(sweetest_icecream([ice7, ice4]), 18)
Test.assert_equals(sweetest_icecream([ice1, ice8, ice6, ice7, ice3, ice2, ice3, ice7]), 34)
Test.assert_equals(sweetest_icecream([ice7, ice8, ice4, ice4, ice5, ice1]), 34)
Test.assert_equals(sweetest_icecream([ice10, ice10, ice9, ice4, ice7, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice3, ice10, ice1]), 23)
Test.assert_equals(sweetest_icecream([ice3, ice4, ice7, ice3, ice7, ice10, ice2]), 18)
Test.assert_equals(sweetest_icecream([ice5, ice9, ice9, ice9, ice7, ice5, ice9, ice7]), 81)
Test.assert_equals(sweetest_icecream([ice4, ice9, ice2]), 81)
Test.assert_equals(sweetest_icecream([ice8, ice2, ice2, ice2, ice4, ice8]), 34)
Test.assert_equals(sweetest_icecream([ice4, ice9, ice4, ice3, ice3, ice2, ice5, ice2]), 81)
Test.assert_equals(sweetest_icecream([ice8, ice10, ice5]), 34)
Test.assert_equals(sweetest_icecream([ice10, ice3, ice2, ice1, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice8, ice3, ice4, ice5]), 34)
Test.assert_equals(sweetest_icecream([ice10, ice8, ice6, ice7, ice9, ice4]), 81)
Test.assert_equals(sweetest_icecream([ice5, ice4, ice6, ice6, ice1]), 33)
Test.assert_equals(sweetest_icecream([ice6, ice8, ice2, ice10, ice7, ice10]), 34)
Test.assert_equals(sweetest_icecream([ice1, ice9, ice7, ice3]), 81)
Test.assert_equals(sweetest_icecream([ice7, ice1, ice9, ice6, ice7, ice10, ice2, ice3]), 81)
Test.assert_equals(sweetest_icecream([ice5, ice1, ice7, ice6, ice8, ice1, ice8]), 34)
Test.assert_equals(sweetest_icecream([ice10, ice9, ice2, ice4, ice10]), 81)
Test.assert_equals(sweetest_icecream([ice3, ice7, ice10]), 17)
Test.assert_equals(sweetest_icecream([ice10, ice5, ice4]), 18)
Test.assert_equals(sweetest_icecream([ice9, ice2, ice4, ice8, ice3, ice3]), 81)
Test.assert_equals(sweetest_icecream([ice6, ice3, ice9, ice8, ice2, ice6]), 81)
Test.assert_equals(sweetest_icecream([ice10, ice3]), 17)
Test.assert_equals(sweetest_icecream([ice10, ice7, ice5, ice2, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice10, ice10, ice4, ice1, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice9, ice2, ice6, ice4, ice10, ice3]), 81)
Test.assert_equals(sweetest_icecream([ice8, ice10, ice1, ice7, ice8, ice9, ice1]), 81)
Test.assert_equals(sweetest_icecream([ice7, ice5, ice3, ice8, ice1, ice9]), 81)
Test.assert_equals(sweetest_icecream([ice2, ice6, ice3]), 33)
Test.assert_equals(sweetest_icecream([ice6, ice6]), 33)
Test.assert_equals(sweetest_icecream([ice9, ice6, ice8, ice3, ice2, ice2]), 81)
Test.assert_equals(sweetest_icecream([ice1, ice3, ice3, ice6]), 33)
Test.assert_equals(sweetest_icecream([ice8, ice6]), 34)
Test.assert_equals(sweetest_icecream([ice1, ice1]), 23)
Test.assert_equals(sweetest_icecream([ice4, ice2, ice3, ice9, ice5, ice10, ice6]), 81)
Test.assert_equals(sweetest_icecream([ice10, ice8, ice4, ice3, ice9, ice8, ice1, ice10]), 81)
Test.assert_equals(sweetest_icecream([ice5, ice8, ice5]), 34)

# 
# FINISH TESTS
# 