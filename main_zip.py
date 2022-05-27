from huffman import Huffman
import argparse


def main_zip():
    huffman = Huffman()
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="Введите название файла с "
                                            "расшириением, "
                                            "который нужно заархивировать.")
    parser.add_argument("zipped_file", help="Введите название файла с "
                                            "расшириением, "
                                            "который вы хотите получить после"
                                            "архивации")
    args = parser.parse_args()
    huffman.compress(args.source_file, args.zipped_file)


if __name__ == '__main__':
    main_zip()
