from typing import List


class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on = False

    def power(self) -> None:
        if not self.is_on:
            self.is_on = True

    def install(self, app: str, app_memory: int) -> str:
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if self.memory < app_memory:
            return f"Not enough memory to install {app}"

        self.memory -= app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
