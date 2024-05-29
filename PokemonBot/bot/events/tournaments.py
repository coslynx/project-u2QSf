class Tournament:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)

    def get_participants(self):
        return self.participants

    def start_tournament(self):
        if len(self.participants) < 2:
            return "Not enough participants to start the tournament."
        
        # Logic to handle the tournament battles and determine the winner
        winner = self.simulate_tournament()

        return f"The winner of the tournament is {winner}! Congratulations!"

    def simulate_tournament(self):
        # Simulate battles between participants and determine the winner
        # Placeholder logic, to be implemented
        pass

    def display_tournament_info(self):
        return f"Tournament: {self.name}\nPrize: {self.prize}\nParticipants: {', '.join(self.participants)}"