class Translator:

    def add(self, eng, rus):
        self.new_dict = {}
        if eng not in self.new_dict:
            self.new_dict.setdefault(eng, rus)
        elif self.new_dict[eng, rus] in self.new_dict:
            pass
        else:
            self.new_dict.setdefault(eng, []).append(rus)
        return self.new_dict

    def remove(self, eng):
        return self.new_dict.pop(eng)

    def traslate(self, eng):
        print(*self.new_dict.get(eng,[]))
        #??

a = Translator()
a.add('tree', 'дерево')
a.add('car', 'машина')
a.add('car', 'автомобиль')
a.add('leaf', 'лист')
a.add('river', 'река')
a.add('go', 'идти')
a.add('go', 'ехать')
a.add('go', 'ходить')
a.add('milk', 'молоко')
print(a.__dict__)


