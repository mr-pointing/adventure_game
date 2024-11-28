class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def __str__(self):
        return f"{self.name}\t\t\tHealth: {self.health}\t\t\tScore: {self.score}"

    def dec_health(self, amount):
        self.health -= amount

    def add_to_score(self, amount):
        self.score += amount


