import unittest

from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self) -> None:
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertTrue(result.startswith("STDOUT: Calculator App"))

    def test_run_python_file1(self) -> None:
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_run_python_file2(self) -> None:
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_python_file3(self) -> None:
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertEqual(result, f'Error: Cannot execute "../main.py" as it is outside the permitted working directory')
    
    def test_run_python_file4(self) -> None:
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertEqual(result, f'Error: "nonexistent.py" does not exist or is not a regular file')
        
    def test_run_python_file5(self) -> None:
        result = run_python_file("calculator", "lorem.txt")
        print(result)
        self.assertEqual(result, f'Error: "lorem.txt" is not a Python file')
        
        


if __name__ == "__main__":
    unittest.main()