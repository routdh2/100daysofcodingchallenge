'''Program for unittesting of Employee class'''
import unittest
import employee
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Executing setup class method.")
        '''This will be executed only once at the start of the execution'''
    @classmethod
    def tearDownClass(cls) -> None:
        print("Executing teardown class method.")
        '''This will be run once at the end of the execution'''
    def setUp(self):
        print("Executing setup method")
        '''This will be executed at the beginning of each test case.
        so any initailization you want to do for the whole test case, you do it here.'''
        self.emp1 = employee.Employee("Dhananjay", "Rout", 23)
        self.emp2 = employee.Employee("Sunil", "Nair", 34)
    def tearDown(self):
        '''This will be run at the end of each test case'''
        print("Executing teardown method")
    def test_email(self):
        self.assertEqual(self.emp1.get_email(),"Dhananjay.Rout@email.com")
        self.assertEqual(self.emp2.get_email(),"Sunil.Nair@email.com")
        self.emp1.first="tanmay"
        self.emp1.last="kar"
        self.assertEqual(self.emp1.get_email(),"tanmay.kar@email.com")
    def test_fullname(self):
        self.assertEqual(self.emp1.get_fullname(),"Dhananjay Rout")
        self.assertEqual(self.emp2.get_fullname(),"Sunil Nair")
        self.emp2.first="tanmay"
        self.emp2.last="kar"
        self.assertEqual(self.emp2.get_fullname(),"tanmay kar")

if __name__=="__main__":
    unittest.main()
