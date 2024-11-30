import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_walk = runner.Runner('Name')
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    def test_run(self):
        runner_run = runner.Runner('Name')
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    def test_challenge(self):
        runner_1 = runner.Runner('Name1')
        runner_2 = runner.Runner('Name2')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()