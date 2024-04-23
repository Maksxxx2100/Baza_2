from DATAbase import Category, Film, get_session, Actor

"""with open("Film") as f:
    name = f.readlines()
for i in range(len(name)):
    name[i] = name[i].replace('\n','')
"""

"""def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')
    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()
    return lines
    
name = read2list("Film")"""

with open("Film.txt", 'r', encoding='utf-8') as f:
    new = f.read()
new = new.replace("$",'\n')
new = new.split('\n')

print(new[2])
session = get_session()
#session.query(Category).delete()

"""
with open("Categories") as f1:
    category = f1.readlines()
for i in range(len(category)):
    category[i] = category[i].replace('\n','')
"""
#[(id, title), (id, title)]


films = session.query(Film).order_by(Film.film_release_date).filter(Film.category_id == 354).all()
request = "Вос"
for film in films:
    print(film)


#session.query(Category).delete()
session.commit()
session.close()