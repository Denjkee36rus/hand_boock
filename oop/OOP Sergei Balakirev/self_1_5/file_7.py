class CPU:
    """Класс для описания процессов."""

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    """Класс для описания оперативной памяти."""

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    """Класс для описания материнских плат."""

    def __init__(self, name: str, cpu: CPU, *mems):
        self.name = name
        self.cpu = cpu
        self.__total_mem_slots: int = 4
        self.mem_slots: tuple[Memory] = mems[:self.__total_mem_slots]

    def get_config(self):
        result = []
        result.append(f'Материнская плата: {self.name}')
        result.append(f'Центральный процессор: {self.cpu.name} {self.cpu.fr}')
        result.append(f'Слотов памяти: {self.__total_mem_slots}')
        result.append(
            f'Память: ' + '; '.join(
                f'{mem.name} - {mem.volume}'
                for mem in self.mem_slots
            )
        )
        return result


if __name__ == '__main__':
    RAM: int = 8
    GHZ: float = 3.4
    n: int = 2

    # -----------------------

    mem_obj: list[Memory] = [Memory(f'Память {i}', RAM) for i in range(1, n)]
    cpu_obj: CPU = CPU('Apple Silicon M3 Pro', GHZ)
    mb: MotherBoard = MotherBoard('Apple', cpu_obj, *mem_obj)
    print(mb.get_config())
