# 📒 Homework: CLI Assistant Bot — Persistence with Pickle

У цьому домашньому завданні було реалізовано збереження та відновлення адресної книги на диск за допомогою серіалізації `pickle`.

Головна мета — забезпечити збереження даних між запусками програми. Після закриття бота всі контакти записуються у файл, а при наступному запуску автоматично завантажуються.

---

# 🧠 Основна ідея

При завершенні роботи програми:

```
AddressBook → pickle → файл
```

При запуску програми:

```
файл → pickle → AddressBook
```

Якщо файл відсутній — створюється нова порожня адресна книга.

---

# 📦 Серіалізація даних

Для збереження використовується модуль `pickle`.

## Функція збереження

```python
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)
```

---

# 📥 Десеріалізація даних

## Функція завантаження

```python
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
```

Якщо файл не знайдено — повертається нова адресна книга.

---

# 🔁 Інтеграція у головний цикл бота

При запуску програми:

```python
book = load_data()
```

Перед завершенням роботи:

```python
save_data(book)
```

---

# 🚀 Приклад роботи

```
Welcome to the assistant bot!
Enter a command: add John 1234567890
Contact added.

Enter a command: all
Contact name: John, phones: 1234567890

Enter a command: exit
Good bye!
```

Після повторного запуску:

```
Welcome to the assistant bot!
Enter a command: all
Contact name: John, phones: 1234567890
```

Контакт збережено.

---

# 📂 Файл збереження

Адресна книга зберігається у файл:

```
addressbook.pkl
```

Файл створюється автоматично після першого збереження.

---

# 🛡 Переваги використання pickle

- швидка серіалізація об'єктів Python
- збереження складних структур даних
- просте відновлення стану програми
- мінімальна кількість коду

---

# 📊 Реалізований функціонал

✔ серіалізація AddressBook  
✔ десеріалізація AddressBook  
✔ автоматичне відновлення даних  
✔ автоматичне збереження при виході  

---

# 🎯 Результат

CLI-асистент тепер **зберігає всі контакти між сеансами роботи**, що робить застосунок значно практичнішим для використання.
