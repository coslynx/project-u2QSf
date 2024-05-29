class MiniGame:
    def __init__(self):
        self.rewards = {
            "Potion": 3,
            "Revive": 1,
            "Rare Candy": 1
        }

    def play_mini_game(self, player):
        # Logic for playing the mini-game
        reward = self.select_random_reward()
        player.add_item(reward, self.rewards[reward])

    def select_random_reward(self):
        # Logic for selecting a random reward from the rewards dictionary
        return random.choice(list(self.rewards.keys()))