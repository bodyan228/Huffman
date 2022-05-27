from nodes.node_for_symbol import NodeForSymbol
from nodes.node_for_bits import NodeForBit
import queue


class Huffman:
    
    codes = [None for i in range(0, 256)]
    
    def compress(self, data_filename, arch_filename: str):
        """Открытие файла и записывание байтов символов."""
        with open(data_filename, "r", encoding='utf-8') as file:
            f = file.read()
        byte_array = bytes(f, encoding='utf-8')
        arch = self.compress_byte(byte_array)
        with open(arch_filename, "wb") as file:
            arch_filename = file.write(bytes(arch))
            
    def compress_byte(self, byte_array):
        """Сжатие файла и объеденение массива битов и заголовка"""
        freq = self.calculate_freq(byte_array)
        sorted_freq = sorted(freq.items())
        head = self.create_head(len(byte_array), freq)
        root = self.create_huffman_tree(sorted_freq)
        self.create_huffman_code(root)
        bits = self.compress_b(byte_array)
        res = head + bits
        return res

    def calculate_freq(self, data):
        """Составление словаря частотности символов"""
        dict_freq = dict()
        for el in data:
            if el in dict_freq.keys():
                dict_freq[el] += 1
            else:
                dict_freq[el] = 1
        d = self.normalize_freq(dict_freq)
        return d

    @staticmethod
    def normalize_freq(dict_freq):
        """Нормализация словаря, чтобы не было переполнения словаря"""
        max_code = 0
        for i in dict_freq.values():
            if i > max_code:
                max_code = i
        if max_code <= 255:
            return dict_freq
        for i in range(0, 256):
            if i in dict_freq.keys():
                if dict_freq[i] > 0:
                    dict_freq[i] = \
                        int(1 + (dict_freq[i] * 255 / (max_code + 1)))
        return dict_freq
        
    @staticmethod
    def create_huffman_tree(frequencies):
        """Составление дерева Хаффмана для символов файла"""
        pq = queue.PriorityQueue()
        for tup in frequencies:
            pq.put(NodeForSymbol(tup[0], tup[1]))
        
        while pq.qsize() > 1:
            bit0 = pq.get()
            bit1 = pq.get()
            freq = bit0.freq + bit1.freq
            next_item = NodeForBit(bit0, bit1, freq)
            pq.put(next_item)
            
        return pq.get()
    
    def create_huffman_code(self, root):
        """Стройка кодов для символов"""
        self.next_code(root, '')

    def next_code(self, node, code: str):
        """Рекурсивно строим код для символов"""
        if node.bit0 is None:
            self.codes[node.symbol] = code
        else:
            self.next_code(node.bit0, code + '0')
            self.next_code(node.bit1, code + '1')
    
    def compress_b(self, data):
        """Запись кодов символов в массив битов и деление по байтам"""
        bits = []
        sum_s = 0
        bit = 1
        for s in data:
            for char in self.codes[s]:
                if char == '1':
                    sum_s |= bit
                if bit < 128:
                    bit <<= 1
                else:
                    bits.append(sum_s)
                    sum_s = 0
                    bit = 1
        if bit > 1:
            bits.append(sum_s)
            
        return bits
    
    @staticmethod
    def create_head(len_data, freq):
        """Составление заголовка сжимаемого файла"""
        header_list = [len_data & 255, (len_data >> 8) & 255,
                       (len_data >> 16) & 255, (len_data >> 24) & 255]
        for i in range(0, 256):
            if i in freq.keys():
                header_list.append(freq[i])
            else:
                header_list.append(0)
        return header_list
    
    start_index: int
    max_size = 0
    
    def decompress(self, arch_file, data_file):
        """Чтение из сжатого файла байтов.
        Далее парсим заголовок на длину исходных данных, стартового индекса,
        и приоритет символов в исходном файле.
        Потом проверяем, если архив не больше 500 Мб,
        то за одну итерацию разархивируем.
        Если же нет, то делим его на куски по 500 Мб и записываем в файл."""
        with open(arch_file, "rb") as file:
            arch = file.read()
            
        data_len, self.start_index, freq = self.parse_header(arch)
        list_for_create_tree = []
        
        for i, el in enumerate(freq):
            if el != 0:
                list_for_create_tree.append((i, el))
        root = self.create_huffman_tree(list_for_create_tree)
        
        if self.start_index < 1024*1024*500:
            data = self.decompress_root(arch, data_len, root)
            with open(data_file, "wb") as file:
                data_file = file.write(bytes(data))
                
        else:
            arch_len = len(arch)
            
            while arch_len > 1024*1024*500:
                data = self.decompress_root(arch, data_len, root)
                
                with open(data_file, "ab") as file:
                    data_file = file.write(bytes(data))
                self.start_index += 1024*1024*500
                arch_len -= 1024*1024*500
                
            data = self.decompress_root(arch, data_len, root)
            with open(data_file, "ab") as file:
                data_file = file.write(bytes(data))
             
    def decompress_root(self, arch, data_len, root):
        """Развертывание дерева с корня"""
        size = 0
        curr = root
        data = []
        for i, current_bit in enumerate(arch):
            if i == 1024*1024*500:
                self.max_size = 0
                break
            if i < self.start_index:
                continue
            else:
                bit = 1
                while bit <= 128:
                    zero = (arch[i] & bit) == 0
                    if zero:
                        curr = curr.bit0
                    else:
                        curr = curr.bit1
                    if curr.bit0 is not None:
                        bit *= 2
                        continue
                    size += 1
                    if size <= data_len:
                        data.append(curr.symbol)
                    curr = root
                    bit *= 2
            self.max_size += 1
        return data

    @staticmethod
    def parse_header(arch):
        """Парсинг заголовка на длину исходной строки, смещения,
        откуда начинаются данные и последовательность симвлов для построения
        дерева Хаффмана"""
        data_len = arch[0] | (arch[1] << 8) | (arch[1] << 16) | (arch[1] << 24)
        freq = [0] * 256
        for i in range(0, 256):
            freq[i] = arch[i + 4]
        start = 4 + 256
        return data_len, start, freq

        