import re

def parse_movies(text):
    pattern = re.compile(r'(.*?)\((\d{4})\)\s*\n(#.+)')
    matches = pattern.findall(text)
    print(matches)
    return {title.strip(): {'year': year, 'tags': tags_list.strip().split()} 
            for title, year, tags_list in matches}
  # {
  # 'American Gangster': {
  #     'year': '2007',
  #     'tags': ['#biográfica', '#crimen']
   #    }
   #}

text = """
American Gangster (2007)
#biográfica #crimen
The Theory of Everything (2014)
#biográfica #drama
Men of Honor (2000)
#drama 
amélie (2001)
#comedia-romántica
A Beautiful Mind (2001)
#biográfica #drama 
The Man Who Knew Infinity (2015)
#biográfica #drama 
Kundun (1997)
#biográfica #épica
seven years in tibet (1997)
#biográfica #guerra
amadeus (1984)
#biográfica #histórica #drama
the shape of water (2017)
#fantasía-romántica #histórica 
the lord of the rings (trilogía 2001-2003)
#aventura #fantasía #épica 
tombstone (1993)
#western
unforgiven (1992)
#western 
hell or high water (2016)
#neo-western #crimen 
la historia oficial (1985)
#histórica #drama  
LA 92 (2017)
#documental
The pianist (2002)
#biográfica 
Gladiator (2000)
#histórica #épica 
American History X (1998)
#crimen #drama 
BlacKkKlansman (2018)
#comedia-dramática #crimen #biográfica
The zone of interest (2023)
#histórica 
Seven (1995)  
#crimen #suspenso #thriller-psicológico  
Pizza, birra, faso (1998)  
#drama #crimen  
Contratiempo (2016)  
#thriller #misterio
Goodfellas (1990)  
#biográfica #gangster
Primal Fear (1996)  
#crimen #thriller #judicial #misterio  
Training Day (2001) 
#crimen #thriller    
Road to Perdition (2002)  
#crimen #drama #thriller    
Witness for the Prosecution (1957)  
#drama #misterio #thriller-legal
The Terminator (1984)  
#ciencia-ficción #acción #thriller    
Baby Driver (2017)  
#acción #crimen #thriller    
Indiana Jones and the Raiders of the Lost Ark (1981)  
#aventura #acción    
Django Unchained (2012)  
#western #drama #acción    
Batman (1989)  
#superhéroes #acción #crimen    
Los siete samuráis (1954)  
#aventura #drama #acción    
The Dark Knight (2008)  
#superhéroes #acción #crimen    
The Gentlemen (2019)  
#crimen #comedia #acción    
Harakiri (1962)  
#drama #histórica    
Ford v Ferrari (2019)  
#biográfica #drama #deportes    
Saga Rocky  
#deportes #drama    
7 cajas (2012)  
#thriller #acción #drama
The Silence of the Lambs (1991)  
#thriller-psicológico #terror #crimen
Suspiria (1977)  
#terror #sobrenatural
Suspiria (2018)  
#terror #sobrenatural    
Cam (2018)  
#terror #thriller-psicológico    
Raw (2016)  
#terror #drama    
Antrum (2018)  
#terror #experimental    
Black Swan (2010)  
#thriller-psicológico #drama    
The Sixth Sense (1999)  
#thriller-psicológico #misterio #drama
El estafador de Tinder (2022)  
#documental #crimen
Choke: Rickson Gracie (1999)  
#documental #artes-marciales
The Creative Brain (2019)  
#documental #ciencia
Night on Earth (2020)  
#documental #naturaleza
Searching for Sugar Man (2012)  
#documental #biografía #música
Open Season (2006)  
#animación #comedia #aventura
El rey león (1994)  
#animación #aventura #drama
La princesa Mononoke (1997)  
#animación #fantasía #aventura
The Banshees of Inisherin (2022)  
#tragicomedia #drama #comedia
War Dogs (2016)  
#comedia #crimen #biografía
Saturday Night Fever (1977)  
#drama #música
Superbad (2007)  
#comedia #adolescente
Perfetti sconosciuti (2016)  
#comedia #drama
Airplane! (1980)  
#comedia #parodia
Color Me Kubrick (2005)  
#comedia #biografía
El hijo de la novia (2001)  
#comedia #drama #romance
Office Space (1999)  
#comedia #satírica
Gosford Park (2001)  
#comedia #drama #misterio
The Good, the Bad and the Ugly (1966)  
#western #acción
The King of Staten Island (2020)  
#comedia #drama
Jojo Rabbit (2019)  
#comedia #drama #guerra
The Sting (1973)  
#crimen #drama
Crawl (2019)  
#terror #suspenso
Withnail and I (1987)  
#comedia #drama
The Name of the Rose (1986)  
#misterio #drama
Shutter Island (2010)  
#thriller #misterio
Inception (2010)  
#ciencia-ficción #thriller
Interstellar (2014)  
#ciencia-ficción #aventura
Edge of Tomorrow (2014)  
#ciencia-ficción #acción
After Yang (2021)  
#ciencia-ficción #drama
Bicentennial Man (1999)  
#ciencia-ficción #drama
Scent of a Woman (1992)  
#drama
Saving Private Ryan (1998)  
#bélica #drama 
The Invisible Man (2020)
#terror #ciencia-ficción 
La vita è bella (1997)
#comedia-dramática 
The Prestige (2006)  
#thriller-psicológico 
Any Given Sunday (1999)  
#drama #deportes
Diario de una pasión (2004)  
#romance #drama
Secreto en la montaña (2005)  
#romance #drama
Beginners (2010)  
#comedia #drama #romance
1917 (2019)  
#bélica #drama
Ladyhawke (1985)  
#fantasía #aventura
12 Angry Men (1957)  
#drama #judicial    
Chariots of Fire (1981)  
#drama #deporte #biográfica    
Menace II Society (1993)  
#drama #crimen    
The Grand Budapest Hotel (2014)  
#comedia #drama    
Manhattan (1979)  
#comedia #romántica    
Rumble Fish (1983)  
#drama #crimen    
Burning (2018)  
#drama #misterio    
The Yards (2000)  
#crimen #drama    
Apocalypse Now (1979)  
#bélica #drama    
Adventureland (2009)  
#comedia #drama #romántica    
Anatomy of a Murder (1959)  
#drama #judicial    
The Pursuit of Happyness (2006)  
#drama #biográfica    
Matchstick Men (2003)  
#comedia #drama #crimen    
Punch-Drunk Love (2002)  
#comedia #drama #romántica    
(500) Days of Summer (2009)  
#comedia #drama #romántica    
Anything Else (2003)  
#comedia #romántica    
La Flor (2018)  
#drama #experimental    
Sátántangó (1994)  
#drama #experimental    
Magnolia (1999)  
#drama    
The Kids Are All Right (2010)  
#comedia #drama    
Taxi Driver (1976)  
#drama #crimen    
Zodiac (2007)  
#crimen #drama #misterio    
The Evil Dead (1981)  
#terror    
Don't Breathe (2016)  
#terror #suspenso    
El Secreto de Sus Ojos (2009)  
#drama #misterio #crimen    
Angel Heart (1987)  
#misterio #terror    
Jacob's Ladder (1990)  
#terror #misterio    
No Country for Old Men (2007)  
#crimen #drama #suspenso    
Fanny y Alexander (1982)  
#drama    
Misión Imposible (1996)  
#acción #aventura #suspenso    
Avatar (2009)  
#ciencia-ficción #aventura    
El Gigante de Hierro (1999)  
#animación #ciencia-ficción #familia    
Alita: Battle Angel (2019)  
#ciencia-ficción #acción    
Citizen Kane (1941)  
#drama #misterio    
Juice (1992)  
#crimen #drama    
Straight Outta Compton (2015)  
#biográfica #drama #música    
Notorious (2009)  
#biográfica #drama #música    
Wild Style (1983)  
#drama #música    
The Wailing (2016)  
#terror #misterio    
American Psycho (2000)  
#terror #sátira    
Mother (2009)  
#drama #misterio    
Pulse (2001)  
#terror #ciencia-ficción    
El Ángel (2018)  
#crimen #drama    
La Corazonada (2020)  
#crimen #suspenso    
Divergente (2014)  
#ciencia-ficción #aventura    
Trilogía de El Protegido    
    El Protegido (2000)  
    #suspenso #superhéroes 
    Fragmentado (2016)  
    #suspenso #terror   
    Glass (2019)  
    #suspenso #superhéroes
    The Big Short (2015)  
#biográfica #drama #comedia    
40 Years of Hip Hop (2014)  
#documental #música    
Rhyme & Reason (1997)  
#documental #música    
Wall Street (1987)  
#drama #crimen    
Assault on Precinct 13 (1976)  
#acción #suspenso    
Double Indemnity (1944)  
#film-noir #suspenso    
Ferris Bueller's Day Off (1986)  
#comedia #adolescente    
Mr. Smith Goes to Washington (1939)  
#drama    
Heat (1995)  
#crimen #drama #suspenso    
Blood Simple (1984)  
#crimen #suspenso    
Eyes Wide Shut (1999)  
#drama #suspenso    
Fear and Desire (1953)  
#bélica #drama    
Killer's Kiss (1955)  
#film-noir #suspenso
The Killing (1956)  
#film-noir #crimen
Paths of Glory (1957)  
#bélica #drama 
Spartacus (1960)  
#histórica #épica 
Lolita (1962)  
#drama #romántica
Eraserhead (1977)  
#terror #experimental    
Los Crímenes de Grindelwald (2018)  
#fantasía #aventura    
Dolor y Gloria (2019)  
#drama #biográfica    
Bacurau (2019)  
#drama #misterio    
Tetsuo: The Iron Man (1989)  
#terror #ciencia-ficción #experimental    
A Bronx Tale (1993)  
#crimen #drama    
Dorian Gray (2009)  
#drama #fantasía    
Carlito's Way (1993)  
#crimen #drama    
La Haine (1995)  
#drama #crimen    
Moulin Rouge! (2001)  
#drama #musical #romántica    
In Fabric (2018)  
#terror #comedia    
It Follows (2014)  
#terror #suspenso    
El Ritual (2017)  
#terror #misterio    
45 Years (2015)  
#drama #romántica    
Entre Navajas y Secretos (2019)  
#misterio #comedia    
Us (2019)  
#terror #suspenso    
Dragged Across Concrete (2018)  
#crimen #drama    
Bone Tomahawk (2015)  
#terror #western    
Muere, Monstruo, Muere (2018)  
#terror #misterio    
The Guilt (2018)  
#drama #suspenso    
Retrato de una Mujer en Llamas (2019)  
#drama #romántica    
Les Misérables (2019)  
#drama #crimen    
Don’t Look Up (2021)  
#comedia #drama    
Escape Room (2019)  
#terror #suspenso    
Películas de Fernandel  
#comedia #drama    
Sisi (1955-1957)  
#biográfica #histórica    
La Muerte en Directo (1980)  
#ciencia-ficción #drama    
Ocean's Trilogy (2001-2007)  
#crimen #comedia    
The Thieves (2012)  
#acción #crimen
Casablanca (1942)  
#romántica #drama    
Gone with the Wind (1939)  
#histórica #romántica    
Some Like It Hot (1959)  
#comedia #romántica    
Rebel Without a Cause (1955)  
#drama #adolescente    
The Wizard of Oz (1939)  
#fantasía #musical    
Citizen Kane (1941)  
#drama #misterio    
It’s a Wonderful Life (1946)  
#drama #fantasía    
Rear Window (1954)  
#suspenso #misterio    
A Streetcar Named Desire (1951)  
#drama    
Singin’ in the Rain (1952)  
#musical #comedia
Lawrence of Arabia (1962)  
#histórica #drama    
The Right Stuff (1983)  
#histórica #aventura    
The Godfather Part II (1974)  
#drama #crimen
Amici Miei (1975)  
#comedia #drama"""

movies_dict = parse_movies(text)
#print(movies_dict)
sorted_movies = sorted(movies_dict.items(), key=lambda x: x[1]['year'], reverse=True)

for title, data in sorted_movies:
    print(f"{title} ({data['year']})")
    print(" ".join(data['tags']))
