from a.project import Customer
from a.project import Equipment
from a.project import ExercisePlan
from a.project import Subscription
from a.project import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscript = [item for item in self.subscriptions if item.id == subscription_id][0]
        customer = [item for item in self.customers if item.id == subscript.customer_id][0]
        trainer = [item for item in self.trainers if item.id == subscript.trainer_id][0]
        plan = [item for item in self.plans if item.id == subscript.exercise_id][0]
        equipment = [item for item in self.equipment if item.id == plan.equipment_id][0]
        result = f"{subscript}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result