class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


# generate test for the bellow class
class WorkerTests(TestCase):
    def test_object_is_initialised_correctly(self):
        # ACT
        worker = Worker("Test", 1000, 60)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        # arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(0, worker.money)
        self.assertEqual(60, worker.energy)

        # act
        worker.work()

        # assert
        current_expected_money = worker.salary
        self.assertEqual(current_expected_money, worker.salary)
        self.assertEqual(worker.energy, worker.energy)

        worker.work()
        # worker works again
        current_expected_money = 1000 + 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1 - 1
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_has_no_energy_to_work(self):
        # Arrange: Create a Worker object with 0 energy
        worker = Worker("test", 1000, 0)

        # Act and Assert: Check that calling the work() method raises an Exception
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert: Check that the exception's message is as expected
        self.assertEqual('Not enough energy.', ex.exception.args[0])

    def test_worker_has_negative_energy_to_work(self):
        # Arrange: Create a Worker object with 0 energy
        worker = Worker("test", 1000, -1)

        # Act and Assert: Check that calling the work() method raises an Exception
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert: Check that the exception's message is as expected
        self.assertEqual('Not enough energy.', ex.exception.args[0])

    def test_if_energy_increases_when_rest(self):
        # arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)

        # act
        worker.rest()

        # assert
        self.assertEqual(61, worker.energy)

        # act
        worker.rest()

        # assert
        self.assertEqual(62, worker.energy)

    def test_get_info(self):
        # arrange
        worker = Worker("Test", 1000, 60)

        result = worker.get_info()

        # assert
        expected_result = "Test has saved 0 money."
        self.assertEqual(expected_result, result)

        worker.work()
        result = worker.get_info()
        expected_result = "Test has saved 1000 money."
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
