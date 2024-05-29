class Badge:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Badges:
    def __init__(self):
        self.badges = []

    def add_badge(self, name, description):
        badge = Badge(name, description)
        self.badges.append(badge)

    def list_badges(self):
        return self.badges

    def get_badge_by_name(self, name):
        for badge in self.badges:
            if badge.name == name:
                return badge
        return None

    def remove_badge(self, name):
        for badge in self.badges:
            if badge.name == name:
                self.badges.remove(badge)
                return True
        return False