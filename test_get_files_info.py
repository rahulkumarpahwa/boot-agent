import unittest
from functions.get_files_info import get_files_info


class TestGetFileInfo(unittest.TestCase):
    def test_get_files_info1(self) -> None:
        result = get_files_info("calculator", ".")
        print(result)

        lines = ["Result for current directory:", f"  - main.py: file_size=748 bytes, is_dir=False", f"  - pkg: file_size=4096 bytes, is_dir=True", f"  - tests.py: file_size=1433 bytes, is_dir=False\n"]
        s = "\n".join(lines)
        self.assertEqual(result, s)


    def test_get_files_info2(self) -> None:
        result = get_files_info("calculator", "pkg")
        print(result)  
        lines = ["Result for pkg directory:", f"  - __pycache__: file_size=4096 bytes, is_dir=True", f"  - calculator.py: file_size=1956 bytes, is_dir=False", f"  - render.py: file_size=403 bytes, is_dir=False\n"]
        s = "\n".join(lines)
        self.assertEqual(result, s)


    def test_get_files_info3(self) -> None:
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')


    def test_get_files_info4(self) -> None:
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

    
    def test_get_files_info5(self) -> None:
        result = get_files_info("calculator", "main.py")
        print(result)
        self.assertEqual(result, 'Error: "main.py" is not a directory')


if __name__ == "__main__":
    unittest.main()