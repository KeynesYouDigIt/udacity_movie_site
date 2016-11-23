import Media
import web_up

mov_roster=[]


#Title, Image, Plot, RT_rating
ToyStory = Media.Movie('ToyStory',
    'https://upload.wikimedia.org'+
    '/wikipedia/en/1/13/Toy_Story.jpg',
    'toys doing stuff',
    'https://www.rottentomatoes.com/m/toy_story/',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')
mov_roster.append(ToyStory)

FightClub = Media.Movie('FightClub',
    'https://upload.wikimedia.org'+
    '/wikipedia/en/thumb/7/73/Figt_clubb.jpg/220px-Figt_clubb.jpg',
    'people fighting',
    'https://www.rottentomatoes.com/m/fight_club/',
    'https://www.youtube.com/watch?v=SUXWAEX2jlg')
mov_roster.append(FightClub)

print 'I have movies about.'

for Mov in mov_roster:
    print Mov.Plot

web_up.open_movies_page(mov_roster)
#takes list  of movies as arg