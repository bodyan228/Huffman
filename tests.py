import unittest
from huffman import Huffman
import os


class TestCorrect(unittest.TestCase):
    
    huffman = Huffman()
    
    def test_correct_decompress(self):
        
        self.huffman.compress("for_tests/test1.txt", "for_tests/test1.huf")
        self.assertEqual(self.huffman.decompress(
            "for_tests/test1.huf", "for_tests/t1.txt"),
            (11, "b'ABRAKADABRA'"))

        self.huffman.compress("for_tests/test2.txt", "for_tests/test2.huf")
        self.assertEqual(self.huffman.decompress(
            "for_tests/test2.huf", "for_tests/t2.txt"),
            (6, "b'qwerty'"))

        self.huffman.compress("for_tests/test3.txt", "for_tests/test3.huf")
        self.assertEqual(self.huffman.decompress(
            "for_tests/test3.huf", "for_tests/t3.txt"),
            (13, "b'8917777777777'"))

        self.huffman.compress("for_tests/test4.cs", "for_tests/test4.huf")
        self.assertEqual(self.huffman.decompress(
            "for_tests/test4.huf", "for_tests/t4.cs"),
            (7, "b'rabbits'"))
    
    def test_compress_50_percent(self):
        self.huffman.compress("for_tests/test5.cs", "for_tests/test5.huf")
        size_arch = os.path.getsize("for_tests/test5.huf")
        size_file = os.path.getsize("for_tests/test5.cs")
        self.assertLess(size_arch/size_file, 0.59)

        self.huffman.compress("for_tests/test6.txt", "for_tests/test6.huf")
        size_arch = os.path.getsize("for_tests/test5.huf")
        size_file = os.path.getsize("for_tests/test5.cs")
        self.assertLess(size_arch / size_file, 0.59)
        
        
        