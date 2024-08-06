class CPU: # класс для описания процессов
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory: # Memory. - класс для описания памяти;
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard: # MotherBoard - класс для описания материнских плат.
    total_mem_slots = 4
    def __init__(self, name, cpu, *memory_modules):
        self.name = name
        self.cpu = cpu
        self.memory_modules = memory_modules
        self.mem_slots = list(memory_modules)
        if len(self.mem_slots) > self.total_mem_slots:
            raise ValueError("Слишком много модулей памяти указано"
                             " для материнской платы")
    def get_config(self):
        result = []
        result.append(f'Материнская плата: {self.name}')
        result.append(f'Центральный процессор: {self.cpu.fr}')
        print(result)

mb = MotherBoard('Intel', 26, 100, 100, 25)
mb.get_config()


