#Part 12, using if/else to compare prices
StoreA = 400 + (1.25 * 65)
StoreB = 530
if StoreA < StoreB:
    print("Store A is cheaper at $%.2f." % StoreA ," versus Store B at $%.2f." % StoreB)
else:
    print("Store B is cheaper at $%.2f." % StoreB ," versus Store A at $%.2f." % StoreA)