class Items(object):
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def use(self):
        print("you use %s" % self.name)


class Weapon(Items):
    def __init__(self, name, amount, damage, durability, material):
        super(Weapon, self).__init__(amount, name)
        self.name = name
        self.amount = amount
        self.damage = damage
        self.durability = durability
        self.material = material

    def pick_up(self):
        print("you pick up a %s" % self.name)
        print("there is %s of them" % self.amount)


class SteelSword(Weapon):
    def __init__(self, damage, durability, material):
        super(SteelSword, self).__init__("Steel sword", 1, damage, durability, material)
        self.damage = damage
        self.durability = durability
        self.material = material

    def inspect(self):
        print("you inspect your sword it does %s damage" % self.damage)
        print("it has %s hits left until it breaks" % self.durability)
        print("it is made of %s" % self.material)

    def slice(self):
        print("you slash your opponent hitting them for %s they are staggered allowing you to hit again" % self.damage)
        self.durability -= 20
        print("you have %s hits left on this weapon" % self.durability)


s_sword = SteelSword(16, 400, "steel")


class WoodenAxe(Weapon):
    def __init__(self, durability, material):
        super(WoodenAxe, self).__init__("wooden axe", 100, 7, durability, material)

    def axe_rush(self):
        print("you rush your opponent and you use your axe to slash them you smack them for %s, the axe gets stuck in "
              "them...but you at least killed it" % self.damage)
        self.durability -= 30
        print("your weapon is %s hits away from breaking" % self.durability)


w_axe = WoodenAxe(100, "wood")


class SteelAxe(WoodenAxe):
    def __init__(self, durability, material, damage):
        super(SteelAxe, self).__init__(durability, material)
        self.damage = damage

    def cleave(self):
        self.durability -= 40
        self.damage -= 5
        print("you rush your opponent and swing your axe decapitating them killing them instantly...your weapon has "
              "%s hits left" % self.durability)

    def inspect(self):
        print("you look at your axe, it has %s hits left" % self.durability)
        print("it is made of %s" % self.material)
        print("it does %s" % self.damage)


s_axe = SteelAxe(400, "steel", 16)


class PlatinumAxe(SteelAxe):
    def __init__(self, durability, damage, material):
        super(PlatinumAxe, self).__init__(durability, damage, material)
        self.damage = damage
        self.material = material
        self.durability = durability

    def inspect(self):
        print("you look at the shiny axe it seems to have %s hits left" % self.durability)
        print("%s, it is the finest material very rare" % self.material)
        print("this amazing weapon deals %s damage" % self.damage)

    def axe_throw(self):
        print("you toss the axe and it hits, the axe takes some massive damage to its durability "
              "but its still usable")
        self.durability -= 300
        self.damage -= 14


p_axe = PlatinumAxe(700, 34, "platinum")


class WoodenSword(SteelSword):
    def __init__(self, damage, material, durability):
        super(WoodenSword, self).__init__(damage, material, durability)
        self.durability = durability
        self.material = material
        self.damage = damage

    def inspect(self):
        print("you inspect your sword it seems sturdy enough to be used %s time(s)" % self.durability)
        print("%s, defiantly not good but it gets the job done" % self.material)
        print("surprisingly it does %s damage" % self.damage)

    def sword_rush(self):
        self.durability -= 25
        self.damage -= 4
        print("you rush your opponent swinging your flimsy sword")
        print("your sword takes some durability damage, it has %s hits left" % self.durability)


w_sword = WoodenSword(7, "wood", 100)


class Platinum_Sword(WoodenSword):
    def __init__(self):
        super(Platinum_Sword, self).__init__(34, "Platinum", 700)

    def ultra_cut(self):
        self.durability -= 600
        self.damage -= 16
        print("you cleave your opponent cutting causing massive damage, the sword becomes flimsy...it has %s hits left"
              % self.durability)

    def inspect(self):
        print("you inspect your sword it seems to be good enough to be used %s time(s)" % self.durability)
        print("%s, best material to get the job done" % self.material)
        print("of course it does %s damage" % self.damage)


p_sword = Platinum_Sword()


class Consumables(Items):
    def __init__(self, amount, name):
        super(Consumables, self).__init__(amount, name)
        self.name = name
        self.amount = amount


class Food(Consumables):
    def __init__(self, amount, name, heal):
        super(Food, self).__init__(amount, name)
        self.heal = heal

    def eat(self):
        print("you eat %s...it seems safe enough" % self.name)
        print("it heals you for %s!" % self.heal)


class Apple(Food):
    def __init__(self):
        super(Apple, self).__init__(2, "apple", 30)


class Steak(Food):
    def __init__(self):
        super(Steak, self).__init__(1, "Steak", 60)


class poisoned_apple(Food):
    def __init__(self):
        super(poisoned_apple, self).__init__(1, "Red Apple", 44)

    def eat(self):
        print("you eat the %s..you feel sick" % self.name)
        print("the apple was poisoned! you take %s damage from poison..then it goes away" % self.heal)


class rotten_steak(Food):
    def __init__(self):
        super(rotten_steak, self).__init__(1, "Odd looking steak", 50)

    def eat(self):
        print("you eat %s..why? it makes you feel odd" % self.name)
        print("you made a mistake it had gone bad! you vomit and take %s damage" % self.heal)


class potato(Food):
    def __init__(self):
        super(potato, self).__init__(1, "potato", 20)
