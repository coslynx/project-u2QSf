class Storage:
    def __init__(self):
        self.pokemon_storage = {}

    def add_pokemon(self, trainer_id, pokemon):
        if trainer_id not in self.pokemon_storage:
            self.pokemon_storage[trainer_id] = []
        self.pokemon_storage[trainer_id].append(pokemon)

    def remove_pokemon(self, trainer_id, pokemon):
        if trainer_id in self.pokemon_storage:
            if pokemon in self.pokemon_storage[trainer_id]:
                self.pokemon_storage[trainer_id].remove(pokemon)
            else:
                print("Pokemon not found in storage.")
        else:
            print("Trainer not found in storage.")

    def get_trainer_pokemon(self, trainer_id):
        if trainer_id in self.pokemon_storage:
            return self.pokemon_storage[trainer_id]
        else:
            print("Trainer not found in storage.")
            return []

    def get_all_pokemon(self):
        all_pokemon = []
        for trainer_pokemon in self.pokemon_storage.values():
            all_pokemon.extend(trainer_pokemon)
        return all_pokemon