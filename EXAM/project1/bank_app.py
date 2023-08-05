from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in ["StudentLoan", "MortgageLoan"]:
            raise Exception("Invalid loan type!")

        loan = StudentLoan() if loan_type == "StudentLoan" else MortgageLoan()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        if any(client.client_id == client_id for client in self.clients):
            raise Exception("Client ID already exists!")

        if client_type not in ["Student", "Adult"]:
            raise Exception("Invalid client type!")

        client = Student(client_name, client_id, income) if client_type == "Student" else Adult(client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next((client for client in self.clients if client.client_id == client_id), None)
        loan = next((loan for loan in self.loans if type(loan).__name__ == loan_type), None)

        if not client or not loan:
            raise Exception("No such client or loan!")

        if (isinstance(client, Student) and isinstance(loan, StudentLoan)) or \
           (isinstance(client, Adult) and isinstance(loan, MortgageLoan)):
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = next((client for client in self.clients if client.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        if loan_type not in ["StudentLoan", "MortgageLoan"]:
            raise Exception("Invalid loan type!")

        changed_loans = [loan for loan in self.loans if type(loan).__name__ == loan_type]
        for loan in changed_loans:
            loan.increase_interest_rate()
        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = [client for client in self.clients if client.interest < min_rate]
        for client in affected_clients:
            client.increase_clients_interest()
        return f"Number of clients affected: {len(affected_clients)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)
        loans_granted = [loan for client in self.clients for loan in client.loans]
        loans_count_granted_to_clients = len(loans_granted)
        granted_sum = sum(loan.amount for loan in loans_granted)
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = sum(client.interest for client in self.clients) / total_clients_count if self.clients else 0

        return '\n'.join([
            f"Active Clients: {total_clients_count}",
            f"Total Income: {total_clients_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ])

#
# bank = BankApp(3)
#
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
#
#
# print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
# print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
# print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
# print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
#
# print(bank.grant_loan('StudentLoan', '1234567891'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
#
# print(bank.remove_client('1234567999'))
#
# print(bank.increase_loan_interest('StudentLoan'))
# print(bank.increase_loan_interest('MortgageLoan'))
#
# print(bank.increase_clients_interest(1.2))
# print(bank.increase_clients_interest(3.5))
#
# print(bank.get_statistics())
#
