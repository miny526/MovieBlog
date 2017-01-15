import fresh_tomatoes
import media

# list of movies and their title, storyline, poster image, and youtube link info 
toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
beauty_beast = media.Movie("Beauty and the Beast",
                           "Love story of the arrogant young prince who turns into a hideous beast and the spirited, headstrong village girl Belle.",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcQw5EdCfwRxbxIsSqtadz0uU5yBAVzJwDK0sq0dSIA1aHbShc_N",
                           "https://www.youtube.com/watch?v=KVOAC7gczX0")
notebook = media.Movie("The Notebook", "A contemporary love story of Noah and Allie set in the pre- and post-World War II era",
                       "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg","https://www.youtube.com/watch?v=4M7LIcH8C9U")
inception = media.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
avengers = media.Movie("Avengers", "Earth's mightiest heroes come together to fight as a team to stop the mischievous Loki from enslaving humanity",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
frozen = media.Movie("Frozen", "Newly crowned Queen Elsa accidentally uses her power to turn things into ice",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
sound_of_music = media.Movie("The Sound of Music", "A woman leaves an Austrian convent to become a governess to the children of a Naval officer widower",
                             "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
                             "https://www.youtube.com/watch?v=UY6uw3WpPzY")

movies = [toy_story, avatar, beauty_beast, notebook, inception, avengers, frozen, sound_of_music]

# calling open_movies_page function in fresh_tomatoes file 
fresh_tomatoes.open_movies_page(movies)


