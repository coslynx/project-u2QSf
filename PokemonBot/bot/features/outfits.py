class Outfits:
    def __init__(self):
        self.outfits = {}

    def add_outfit(self, trainer_id, outfit_name, outfit_color):
        if trainer_id not in self.outfits:
            self.outfits[trainer_id] = {}
        self.outfits[trainer_id][outfit_name] = outfit_color

    def remove_outfit(self, trainer_id, outfit_name):
        if trainer_id in self.outfits and outfit_name in self.outfits[trainer_id]:
            del self.outfits[trainer_id][outfit_name]

    def get_outfit_color(self, trainer_id, outfit_name):
        if trainer_id in self.outfits and outfit_name in self.outfits[trainer_id]:
            return self.outfits[trainer_id][outfit_name]
        return None

    def list_outfits(self, trainer_id):
        if trainer_id in self.outfits:
            return self.outfits[trainer_id]
        return {}

    def change_outfit_color(self, trainer_id, outfit_name, new_color):
        if trainer_id in self.outfits and outfit_name in self.outfits[trainer_id]:
            self.outfits[trainer_id][outfit_name] = new_color