class Subscribtion:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int) -> None:
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exersice_id = exercise_id
        self.id = Subscribtion.id
        Subscribtion.id += 1

    @staticmethod
    def get_next_id() -> int:
        return Subscribtion.id

    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"
