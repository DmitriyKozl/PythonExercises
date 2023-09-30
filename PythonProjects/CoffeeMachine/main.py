import Menu

menu = Menu.MENU
resources = Menu.resources
resources["money"] = 0


def report():
    for r in Menu.resources:
        print(Menu.resources[r])


def espresso():

    return menu["espresso"]["cost"]


def latte():
    return menu["latte"]["cost"]


def cappuccino():



choices = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
    "report": report
}
print("what would you like?")
for coffee in menu:
    print(coffee)





def report():

    for r in Menu.resources:
        print(Menu.resources[r])



