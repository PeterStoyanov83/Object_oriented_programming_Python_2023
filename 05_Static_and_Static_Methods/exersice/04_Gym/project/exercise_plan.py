from __future__ import annotations


class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id
        ExercisePlan.id += 1

    @staticmethod
    def get_next_id():
        return ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> ExercisePlan:
        minutes = hours * 60

        return cls(trainer_id, equipment_id, hours)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
