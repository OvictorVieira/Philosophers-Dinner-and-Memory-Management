import math


class Mmu:
    def __init__(self):
        pass

    def mmu_converter(self, addres_virtual):
        address_physic = "032x01" + addres_virtual

        return address_physic


class RamMemory:
    def __init__(self, size):
        self.size = size
        self.frames = list()

    def process_allocate(self, address_physic, size):
        if self.size - len(self.frames) >= size:
            self.frames.append(address_physic)
            print("Alocando o processo na Memoria RAM", self.frames)
        else:
            print(f"Removendo o processo antigo para alocar o novo processo")
            while self.size - len(self.frames) < size:
                if self.frames:
                    old_process = self.frames.pop(0)
                    print(f'Processo {old_process} removido do inicio da fila!')
                    print(f'Processo {address_physic} alocado no final da fila!')

            self.frames.append(address_physic)
            print("Memória RAM", self.frames)

        print("\n")

    def process_remove(self, addr):
        try:
            self.frames.pop(self.frames.index(addr))
            print("Removendo Frame")
        except:
            print("Frame já removido")

    def process_show(self):
        print(self.frames)


class SwapMemory:
    def __init__(self, size):
        self.size = size
        self.pages = list()

    def process_allocate(self, process):
        first, last = None, None

        for i in range(math.ceil((process.size / 4))):
            addr = f"{process.name}{i}"
            if i == 0:
                first = addr

            if i == math.ceil((process.size / 4) - 1):
                last = addr

            self.pages.append(addr)
            print("Memória SWAP", self.pages)

        print("\n")

        return self.pages.index(first), self.pages.index(last)

    def process_remove(self, address_virtual):
        self.pages.pop(self.pages.index(address_virtual))
        print("Removendo Página")

    def process_show(self):
        print(self.pages)
