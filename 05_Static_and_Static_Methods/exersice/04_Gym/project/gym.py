from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
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
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in Gym.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in Gym.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in Gym.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in Gym.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exersice_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"


