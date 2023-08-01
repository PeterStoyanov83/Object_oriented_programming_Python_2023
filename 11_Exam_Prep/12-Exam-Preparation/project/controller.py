from player import Player
from project.supply.food import Food
from project.supply.drink import Drink

class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added_names = []
        for player in players:
            if player.name in added_names:
                raise Exception(f"Name {player.name} is already used!")
            self.players.append(player)
            added_names.append(player.name)
        return f"Successfully added: {', '.join(player.name for player in players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        valid_types = ["Food", "Drink"]

        if sustenance_type not in valid_types:
            return

        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply_type = sustenance_type.lower() + "s"
        supply = next((s for s in reversed(self.supplies) if s.__class__.__name__ == sustenance_type), None)
        if not supply:
            raise Exception(f"There are no {supply_type} left!")

        player.stamina = min(player.stamina + supply.energy, 100)
        self.supplies.remove(supply)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next((p for p in self.players if p.name == first_player_name), None)
        player2 = next((p for p in self.players if p.name == second_player_name), None)

        if not player1 or not player2:
            return

        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."

        if player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        while player1.stamina > 0 and player2.stamina > 0:
            attack_value = player1.stamina // 2
            player2.stamina -= attack_value
            player1.stamina = max(player1.stamina - attack_value, 0)

            if player2.stamina == 0:
                return f"Winner: {first_player_name}"
            elif player1.stamina == 0:
                return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0

        for player in self.players:
            if player.stamina < 100:
                food = next((s for s in reversed(self.supplies) if isinstance(s, Food)), None)
                if food:
                    player.stamina = min(player.stamina + food.energy, 100)
                    self.supplies.remove(food)

                drink = next((s for s in reversed(self.supplies) if isinstance(s, Drink)), None)
                if drink:
                    player.stamina = min(player.stamina + drink.energy, 100)
                    self.supplies.remove(drink)

    def __str__(self):
        players_data = "\n".join(str(player) for player in self.players)
        supplies_data = "\n".join(supply.details() for supply in self.supplies)
        return f"{players_data}\n{supplies_data}"
