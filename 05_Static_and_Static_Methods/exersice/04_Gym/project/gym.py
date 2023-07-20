from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer
from typing import List


class Gym:
    customers: List[Customer] = []
    trainers: List[Trainer] = []
    equipment: List[Equipment] = []
    plans: List[ExercisePlan] = []
    subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in Gym.customers:
            Gym.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in Gym.trainers:
            Gym.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in Gym.equipment:
            Gym.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in Gym.plans:
            Gym.plans.append(plan)

    def subscription_info(self, subscription_id: int) -> str:
        Subscription.id = subscription_id
        return f"{subscription_id}\n" \
               f""
