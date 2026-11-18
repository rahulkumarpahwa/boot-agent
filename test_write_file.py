import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file1(self) -> None:
        content = "wait, this isn't lorem ipsum"
        result = write_file("calculator", "lorem.txt", content)
        print(result)
        s = f'Successfully wrote to "lorem.txt" ({len(content)} characters written)'
        self.assertEqual(result, s)


    def test_write_file2(self) -> None:
        content = "lorem ipsum dolor sit amet"
        result = write_file("calculator", "pkg/morelorem.txt", content)
        print(result)
        s = f'Successfully wrote to "pkg/morelorem.txt" ({len(content)} characters written)'
        self.assertEqual(result, s)


    def test_write_file3(self) -> None:
        content = "this should not be allowed"
        result = write_file("calculator", "/tmp/temp.txt", content)
        print(result)
        self.assertEqual(result, f'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()