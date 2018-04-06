class Person (object):
    def __init__(self, name, health, stats, inventory, status_effects, DR):
        self.name = name
        self.health = health
        self.stats = stats
        self.inventory = inventory
        self.move = False
        self.talk = False
        self.status_effects = status_effects
        self.people = 0
        self.DR = DR

    def move_away(self):
        if self.talk:
            print("you convince them to move")
        else:
            print("they ignore you")

    def talk_to(self):
        if self.talk:
            print("you already spoke to this person")
        else:
            self.talk = True
            print("you talk to this person")

    def interaction(self, people):
        print("%d person blocks the way" % people)
        self.people = people
        self.talk_to()
        self.move_away()
        print("%d people walk away" % people)
        self.people = 0

    def combat(self):
        print("a troll blocks your path he has heavy armor")
        if self.DR >= input("you hit him with >_"):
            print("he shrugs off your hit, and kills you")
            quit()
        else:
            print("you deal 15 damage, he prepares his swing")
        if input("do you dodge? >_") == "yes":
                print("you dodge the hit and the troll falls off the bridge")
        else:
                print("you die")


thing = Person("guard troll", 400, "place holder", 'sword', "poison", "axe")

thing.interaction(1)
thing.combat()
