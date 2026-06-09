#Part 14: FOR Loop for Adding Weight
weight_loss = [10, 12, 8, 5]
total_l = 0
for i in weight_loss:
    total_l += i
print("Total weight loss in 4 months:", total_l, "lbs.")

#using the range
for j in range(len(weight_loss)):
    print("Month", j + 1, "weight loss:", weight_loss[j], "lbs.")
    print("Cumulative weight loss after month", j + 1, ":", sum(weight_loss[:j + 1]), "lbs.")