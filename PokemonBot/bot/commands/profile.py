class Profile:
    def __init__(self, name, level, exp, pokemon_team):
        self.name = name
        self.level = level
        self.exp = exp
        self.pokemon_team = pokemon_team

    def view_profile(self):
        profile_info = f"Trainer: {self.name}\nLevel: {self.level}\nExperience Points: {self.exp}\nPokemon Team: {', '.join(self.pokemon_team)}"
        return profile_info

    def update_level(self, exp_gained):
        self.exp += exp_gained
        if self.exp >= self.level * 100:
            self.level += 1
            return f"Congratulations! You have leveled up to level {self.level}!"

    def add_pokemon_to_team(self, pokemon_name):
        if len(self.pokemon_team) < 6:
            self.pokemon_team.append(pokemon_name)
            return f"{pokemon_name} has been added to your team!"
        else:
            return "Your Pokemon team is full. Please release a Pokemon before adding a new one."

    def remove_pokemon_from_team(self, pokemon_name):
        if pokemon_name in self.pokemon_team:
            self.pokemon_team.remove(pokemon_name)
            return f"{pokemon_name} has been released from your team."
        else:
            return f"{pokemon_name} is not in your team."

    def change_trainer_name(self, new_name):
        self.name = new_name
        return f"Your trainer name has been changed to {new_name}."

    def reset_profile(self):
        self.level = 1
        self.exp = 0
        self.pokemon_team = []
        return "Your profile has been reset to default values. Start anew!"