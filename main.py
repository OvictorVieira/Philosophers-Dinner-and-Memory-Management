import threading
import random
import time
import math
import support


class Philosopher(threading.Thread):
    ram_memory = support.RamMemory(10)
    swap_memory = support.SwapMemory(20)
    mmu = support.Mmu()
    main_page = dict()

    process = tuple()
    process_begin = None
    process_end = None

    running = True

    def __init__(self, f_name, left_fork, right_fork, food, size):
        threading.Thread.__init__(self)
        self.name = f_name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.food = food
        self.size = size

    def run(self):
        time.sleep(random.uniform(3, 13))
        self.process_begin, self.process_end = self.swap_memory.process_allocate(self)

        for page in self.swap_memory.pages[self.process_begin:self.process_end + 1]:
            address_physic = self.mmu.mmu_converter(page)

            self.ram_memory.process_allocate(address_physic, math.ceil(self.size / 4))
            self.main_page[page] = address_physic

        while True:
            if self.food == 0:
                print(f'A comida do {self.name} acabou!')

                for i in range(math.ceil(self.size / 4)):
                    address_virtual = self.name + str(i)
                    address_physic_1 = self.main_page[address_virtual]

                    self.ram_memory.process_remove(address_physic_1)
                    self.swap_memory.process_remove(address_virtual)

                print("\n\n")
                print(f"Memoria RAM: {self.ram_memory.frames}")
                print(f"Memoria SWAP: {self.swap_memory.pages}")
                print(f"Tabela de Paginação: {self.main_page}")
                print("\n\n")
                break

            print(f'{self.name} esta com fome!')
            print('\n')
            self.dine()

    def dine(self):
        (fork1, fork2) = (self.left_fork, self.right_fork)
        while self.running:
            fork1.acquire(True)

            locked = fork2.acquire(False)

            if locked:
                break

            fork1.release()
            (fork1, fork2) = (fork2, fork1)
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        for page in self.swap_memory.pages[self.process_begin:self.process_end + 1]:
            address_physic = self.mmu.mmu_converter(page)

            if address_physic not in self.ram_memory.frames:
                print("Inserindo frames na memoria RAM")
                self.ram_memory.process_allocate(address_physic, math.ceil(self.size / 4))

        print(f'{self.name} comecou a comer!')
        print('\n')
        time.sleep(random.uniform(1, 10))
        print(f'{self.name} terminou de comer e esta voltando a pensar')
        print('\n')

        self.food -= 1

        print(f'Ainda restam {self.food} de comida para {self.name}')
        print('\n')


def dining_philosophers():
    forks = [threading.Lock() for i in range(5)]
    food = 2
    philosophy = ['Socrates', 'Platão', 'Aristoteles', 'Friedrich', 'Karl Marx']

    # cada filosofo tera tamanho minimo de 4 e tamanho máximo 12
    # pois cada pagina tera um tamanho minimo de 4 e máximo de 12
    size = random.randint(4, 12)

    philosophers = [Philosopher(philosophy[i], forks[i % 5], forks[(i + 1) % 5], food, size) for i in range(5)]

    random.seed(507129)
    Philosopher.running = True

    for philosopher in philosophers:
        philosopher.start()

    if food == 0:
        Philosopher.running = False
        print('Finalizando o jantar!')


if __name__ == '__main__':
    dining_philosophers()
