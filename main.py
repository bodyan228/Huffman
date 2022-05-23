from huffman import Huffman


def main():
    huffman = Huffman()
    huffman.compress("input data/abra.txt", "archived/archived_abra.txt")
    huffman.decompress("archived/archived_abra.txt", "unzipped/abra.txt")
    huffman.compress("input data/Rational.cs", "archived/archived_Rational.cs")
    huffman.decompress("archived/archived_Rational.cs", "unzipped/Rational.cs")


if __name__ == '__main__':
    main()
    