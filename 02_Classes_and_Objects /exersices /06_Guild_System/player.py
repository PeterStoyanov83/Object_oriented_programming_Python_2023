from typing import Dict, List


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        info = f"Name: {self.name}\nGuild: {self.guild_name}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill_name, mana_cost in self.skills.items():
            info += f"==={skill_name} - {mana_cost}\n"
        return info

