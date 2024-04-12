lern_char = int(input())
col_string = int(input())

out_line = ''
for _ in range(col_string):
    string = input()
    out_line += string + '\n'

if len(out_line) - 3 > lern_char:
    out_line = out_line[:lern_char - 3] + '...'
print(out_line, sep=' ')

# Нерабочий вариант кода
length: int = int(input())  # L — необходимая длина заголовка
n: int = int(input())  # N — количество строк в заголовке новости

title: str = ""
for i in range(n):  # N строк записано по одной строке заголовка.
    title += input()
    if i != n - 1:
        title += '\n'

title_length = len(title)

slash_n_count = title.count('\n')
dots: str = "..."
if (title_length - slash_n_count) > length:
    slash_n_count = title[:length - 3].count('\n')
    title = title[:length - 3 + slash_n_count] + dots

    # ...

    print(title)
else:
    print(title)
