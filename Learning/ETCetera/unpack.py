# def total(galleons, sickels, knuts):
#     return(galleons * 17 + sickels) * 29 + knuts


# coins = [100,50,25]
# print(total(100,50,25), "knuts")
# print(total(coins[0], coins[1],coins[2]), "knuts")
# print(total(*coins), "knuts")

# coins= {
#     "galleons": 100,
#     "sickels" : 50,
#     "knuts"   : 25,
# }

# print(total(galleons=100, sickels=50, knuts=25), "Knuts")
# print(total(coins["galleons"], coins["sickels"], coins["knuts"]), "Knuts")
# print(total(**coins), "knuts")


def f(*args, **kwargs):
    print("Postional: ", args)
    print("Positional: ", kwargs)


f(galleons=100,sickels=50,knuts=25)