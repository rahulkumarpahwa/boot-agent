import unittest

from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def test_get_file_content(self) -> None:
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")

    def test_get_file_content1(self) -> None:
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_get_file_content2(self) -> None:
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertTrue(result.startswith("from collections.abc import Callable"))

    def test_get_file_conten3(self) -> None:
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertEqual(result, 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory')
    
    def test_get_file_conten3(self) -> None:
        result = get_file_content("calculator", "pkg/does_not_exist.py") 
        print(result)
        self.assertEqual(result, 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"')


if __name__ == "__main__":
    unittest.main()