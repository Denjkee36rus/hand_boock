class Translator:

    def add(self, eng, rus):
        self.new_dict = {}
        if eng not in self.new_dict:
            self.new_dict[eng] = [rus]
        elif self.new_dict[eng, rus] in self.new_dict:
            pass
        else:
            self.new_dict.setdefault(eng, []).append(rus)


    def remove(self, eng):
        self.new_dict.pop(eng)

    def traslate(self, eng):
        print(*self.new_dict.get(eng,[]))
        #???????











        # for row in new_dict:
        #     if eng not in  new_dict:
        #         new_dict.append(dict(zip(eng.split(), rus.split())))
        #
        #     elif eng[rus]
        #
        #     else:
        #         new_dict
        #
        #
        #
        # return new_dict

a = Translator()
a.add('Hellow', 'привет')
a.add('Hellow', 'салам')
a.add('tree', 'дерево')
a.traslate('tree')

