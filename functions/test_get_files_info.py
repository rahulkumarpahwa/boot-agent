import unittest
from get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def test_get_files_info1(self) -> None:
        result = get_files_info("calculator", ".")
        print(result)
        self.assertEqual(result, 'Success: "." is within the working directory')

    def test_get_files_info2(self) -> None:
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')


    def test_get_files_info3(self) -> None:
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

    
    def test_get_files_info4(self) -> None:
        result = get_files_info("calculator", "main.py")
        print(result)
        self.assertEqual(result, 'Error: "main.py" is not a directory')


if __name__ == "__main__":
    unittest.main()