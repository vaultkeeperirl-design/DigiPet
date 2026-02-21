import time
import json
import os

class Pet:
    def __init__(self):
        self.name = "DigiPet"
        self.species = "Egg"
        self.stage = 0 # 0: Egg, 1: Baby, 2: Child, 3: Adult

        self.hunger = 50
        self.happiness = 50
        self.energy = 100
        self.discipline = 0
        self.weight = 5
        self.age = 0 # In hours or days

        self.is_sleeping = False
        self.is_sick = False
        self.has_poop = False

        self.care_mistakes = 0
        self.birth_time = time.time()
        self.last_update = time.time()

        # Evolution timers (seconds for testing, should be longer for real game)
        # Egg -> Baby: 60s
        # Baby -> Child: 300s (5m)
        # Child -> Adult: 600s (10m)
        self.evo_thresholds = [60, 360, 960]

    def update(self):
        current_time = time.time()
        dt = current_time - self.last_update
        self.last_update = current_time

        if self.stage == 0: # Egg stage
            if current_time - self.birth_time > self.evo_thresholds[0]:
                self.evolve()
            return

        # Natural decay (stats decrease over time)
        if not self.is_sleeping:
            self.hunger = max(0, self.hunger - dt * 0.2)
            self.happiness = max(0, self.happiness - dt * 0.1)
            self.energy = max(0, self.energy - dt * 0.15)

            # Pooping logic: chance to poop if hunger is high and weight is high
            if not self.has_poop and self.weight > 2:
                import random
                if random.random() < dt / 1800: # Average once every 30 mins
                    self.has_poop = True
        else:
            self.energy = min(100, self.energy + dt * 1.0)

        # Sickness logic
        if self.hunger == 0 or self.has_poop:
            if time.time() % 60 < dt: # Small chance to get sick every minute if neglected
                self.is_sick = True
                self.care_mistakes += 1

        # Age increases
        self.age += dt / 3600 # Age in hours

        # Evolution check
        if self.stage < 3:
            if current_time - self.birth_time > self.evo_thresholds[self.stage]:
                self.evolve()

    def evolve(self):
        self.stage += 1
        if self.stage == 1:
            self.species = "Bloop"
        elif self.stage == 2:
            # Evolution based on discipline
            if self.discipline > 50:
                self.species = "Sprout"
            else:
                self.species = "Thorn"
        elif self.stage == 3:
            # Evolution based on happiness and mistakes
            if self.care_mistakes < 2:
                self.species = "Arbor"
            else:
                self.species = "Wither"
        print(f"Evolved into {self.species}!")

    def feed_meal(self):
        if self.hunger < 100:
            self.hunger = min(100, self.hunger + 20)
            self.weight += 1
            return True
        return False

    def feed_snack(self):
        self.happiness = min(100, self.happiness + 10)
        self.weight += 2
        return True

    def clean(self):
        if self.has_poop:
            self.has_poop = False
            return True
        return False

    def heal(self):
        if self.is_sick:
            self.is_sick = False
            return True
        return False

    def train(self):
        if self.energy > 10:
            self.energy -= 10
            self.discipline = min(100, self.discipline + 5)
            self.weight = max(1, self.weight - 1)
            return True
        return False

    def toggle_sleep(self):
        self.is_sleeping = not self.is_sleeping
        return self.is_sleeping

    def get_status_summary(self):
        return {
            "Species": self.species,
            "Hunger": int(self.hunger),
            "Happiness": int(self.happiness),
            "Energy": int(self.energy),
            "Weight": self.weight,
            "Age": round(self.age, 2),
            "Sick": self.is_sick,
            "Poop": self.has_poop
        }

    def save(self, filepath="data/savegame.json"):
        data = {
            "name": self.name,
            "species": self.species,
            "stage": self.stage,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
            "discipline": self.discipline,
            "weight": self.weight,
            "age": self.age,
            "is_sleeping": self.is_sleeping,
            "is_sick": self.is_sick,
            "has_poop": self.has_poop,
            "care_mistakes": self.care_mistakes,
            "birth_time": self.birth_time,
            "last_save": time.time()
        }
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f)
        print("Game saved.")

    def load(self, filepath="data/savegame.json"):
        if not os.path.exists(filepath):
            return False
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.name = data.get("name", self.name)
        self.species = data.get("species", self.species)
        self.stage = data.get("stage", self.stage)
        self.hunger = data.get("hunger", self.hunger)
        self.happiness = data.get("happiness", self.happiness)
        self.energy = data.get("energy", self.energy)
        self.discipline = data.get("discipline", self.discipline)
        self.weight = data.get("weight", self.weight)
        self.age = data.get("age", self.age)
        self.is_sleeping = data.get("is_sleeping", self.is_sleeping)
        self.is_sick = data.get("is_sick", self.is_sick)
        self.has_poop = data.get("has_poop", self.has_poop)
        self.care_mistakes = data.get("care_mistakes", self.care_mistakes)
        self.birth_time = data.get("birth_time", self.birth_time)
        # We adjust birth_time so the pet doesn't "skip" time
        # unless we want real-time growth while away.
        # Apply real-time growth for the time spent away
        elapsed = time.time() - data.get("last_save", time.time())
        self.last_update = time.time() - elapsed
        self.update() # This will apply one tick of growth based on the full elapsed time
        self.last_update = time.time()
        print(f"Game loaded. {round(elapsed/60, 1)} minutes passed while away.")
        return True
