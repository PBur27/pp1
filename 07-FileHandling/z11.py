film_titles = ['Cars', 'Green Book', 'The Conjuring', 'Nobody', 'Fast and Furious']

file = open('films.txt', 'w')

for title in film_titles:
    file.write(f"{title}\n")