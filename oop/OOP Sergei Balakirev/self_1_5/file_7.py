class CPU: # класс для описания процессов
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory: # Memory. - класс для описания памяти;
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard: # MotherBoard - класс для описания материнских плат.
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]

    def get_config(self):
        result = []
        result.append(f'Материнская плата: {self.name}')
        result.append(f'Центральный процессор: {self.cpu.name} {self.cpu.fr}')
        result.append(f'Слотов памяти: {self.total_mem_slots}')
        result.append(f"Память:" + '; '.join(lambda x)






