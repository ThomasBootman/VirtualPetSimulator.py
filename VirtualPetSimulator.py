import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 10

    def feed(self):
        print(f"{self.name} is being fed...")
        time.sleep(1)
        self.hunger -= 1
        print(f"{self.name} is no longer hungry.")

    def play(self):
        print(f"Playing with {self.name}...")
        time.sleep(2)
        self.happiness += 1
        print(f"{self.name} is happy.")

    def display_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")

def main():
    pet = VirtualPet("Fluffy")

    # Feed the pet
    pet.feed()

    # Play with the pet
    pet.play()

    # Display the pet's status
    pet.display_status()

if __name__ == "__main__":
    main()
