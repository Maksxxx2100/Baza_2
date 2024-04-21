from DATAbase import Film, Actor, Category
from DATAbase import get_session

session = get_session()

# session.query(Category).delete()  # отчистка всего
# session.commit()
session.query(Film).delete()  # отчистка всего
session.commit()

with open('Film.txt', encoding='utf-8') as f:
    new = f.read()
new = new.replace("$", "\n")  # Заменяем все символы $ на пробелы
#new = new.replace("", "\n")  # Заменяем все , на пробелы
new = new.split("\n")  # Разбиваем текст на список строк
print(new)
i = 0
print(len(new))
while i in range(len(new)):
    category_check = session.query(Category).filter(Category.category_title == new[i + 1]).all()
    if (len(category_check) == 0):  # если нет категории добавляем новую
        session2 = get_session()
        new_Category = Category(category_title=new[i + 1])
        session2.add(new_Category)
        session2.commit()
        session2.close()
        category = session.query(Category).filter(Category.category_title == new[i + 1]).all()
    else:
        session = get_session()
        category = session.query(Category).filter(Category.category_title == new[i + 1]).all()
        # print(category[0].category_id)
    new_film = Film(film_title=new[i], film_duration=new[i + 2], category_id=category[0].category_id, film_release_date=new[i+3])
    session.add(new_film)
    session.commit()
    i += 7

# session.add(new_Category)
session.commit()
session.close()