class Translator:

    def add(self, eng, rus):
        new_dict = {}
        if eng not in new_dict:
                new_dict[eng] = [rus]
        elif new_dict[eng, rus] in new_dict:
                pass
        else:
                new_dict.setdefault(eng, []).append(rus)
        print(new_dict)




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

