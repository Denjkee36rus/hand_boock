# Команды для ВО

MacOS/Linux

---

Создать вирутальное окружение (ВО)

```shell
python3 -m venv .venv
```

Активировать ВО

```shell
source .venv/bin/activate
```

Вынести зависмости проекта в `requirements.txt`

```shell
pip3 freeze > requirements.txt
```

Установка зависимостей из файла `requirements.txt`

```shell
pip3 install -r requirements.txt
```


```python
def some_func(*args, **kwargs):
    pass
```
