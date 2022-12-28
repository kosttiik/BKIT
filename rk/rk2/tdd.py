import unittest
from tasks import task_1, task_2, task_3

task_1_result = [('MyBirthday.mp4ов', 14.9, 'C:\\'), ('Program.zipов', 100, 'C:\\Users\\User\\')]
task_2_result = [['C:\\Users\\', 1700], ['C:\\Users\\User\\', 33], ['C:\\', 15], ['D:\\', 0], ['D:\\Users\\', 0], ['A:\\Users\\Aboba\\', 0]]
task_3_result = {'A:\\Users\\Aboba\\': ['Course-Work.docx', 'Task.pdf', 'Program.zipов']}

class TasksTestCase(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task_1_result, task_1())
    def test_task_2(self):
        self.assertEqual(task_2_result, task_2())
    def test_task_3(self):
        self.assertEqual(task_3_result, task_3())
