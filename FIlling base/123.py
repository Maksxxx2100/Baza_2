from DATAbase import Film, Actor, Category,Film_Actor, Filmmaker, Film_Filmmaker
from DATAbase import get_session

session = get_session()

"""session.query(Film).delete()  # отчистка всего
session.commit()
session.query(Category).delete()  # отчистка всего
session.commit()"""

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
    fmakers_check = session.query(Filmmaker).filter(Filmmaker.fmakers_name == new[i+4]).all()
    if(len(fmakers_check) == 0):
        session2 = get_session()
        new_Fmaker = Filmmaker(fmakers_name=new[i + 4])
        session2.add(new_Fmaker)
        session2.commit()
        session2.close()
        fmaker = session.query(Filmmaker).filter(Filmmaker.fmakers_name == new[i+4]).all()
    else:
        fmaker = session.query(Filmmaker).filter(Filmmaker.fmakers_name == new[i+4]).all()

    """if (len(category_check) == 0):  # если нет категории добавляем новую
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
    new_film = Film(film_title=new[i], film_duration=new[i + 2], category_id=category[0].category_id, film_release_date=new[i+3])"""
    #film = session.query(Film).filter(Film.film_title == new[i]).all()
    #new_film_actor = Film_Actor(film_id=film[0].film_id, actor_id=actor[0].actor_id)
    #new_film_actor2 = Film_Actor(film_id=film[0].film_id, actor_id=actor2[0].actor_id)

        #session.add(new_film_actor)
        #session.add(new_film_actor2)
    #session.add(new_film)
    session.commit()
    film = session.query(Film).filter(Film.film_title == new[i]).all()
    fmaker = session.query(Filmmaker).filter(Filmmaker.fmakers_name == new[i+4]).all()
    new_Film_Fmaker = Film_Filmmaker(film_id=film[0].film_id, fmaker_id=fmaker[0].fmaker_id)

    session.add(new_Film_Fmaker)
    session.commit()
    i += 7

# session.add(new_Category)
session.commit()
session.close()