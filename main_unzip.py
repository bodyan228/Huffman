from huffman import Huffman
import argparse


def main_unzip():
    huffman = Huffman()
    parser = argparse.ArgumentParser()
    parser.add_argument("zipped_file", help="Введите название файла с "
                                            "расшириением, "
                                            "который нужно разархивировать")
    parser.add_argument("file", help="Введите название файла с "
                                     "расшириением, "
                                     "который вы хотите получить после"
                                     "разархивации")
    args = parser.parse_args()
    huffman.decompress(args.zipped_file, args.file)


if __name__ == '__main__':
    main_unzip()
