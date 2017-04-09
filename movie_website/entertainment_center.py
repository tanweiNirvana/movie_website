import media
import fresh_tomatoes

movies_name = ["Game of Thrones 6","Avengers Infinity War","Grand Theft Auto","Wolverine 3 : Logan"]

head_image = "https://upload.wikimedia.org/wikipedia/"
suffixes_image = ["en/d/d1/Game_of_Thrones_Season_6.jpeg",
"en/c/c5/Avengers_Infinity_War_logo_update.jpg",
"zh/9/9f/Rogue_One_A_Star_Wars_Story_Poster.jpg",
"zh/8/81/Logan_2017_Poster.jpg"]
urls_image = [head_image + suffix_image for suffix_image in suffixes_image]

head_youtube = "https://www.youtube.com/watch?v="
suffixes_youtube = ["2pwQl3-EZGU","LwSqIJzVBZQ","mU26T0IToyw","F1f6NsHTIpA"]
urls_youtube = [head_youtube + suffix_youtube for suffix_youtube in suffixes_youtube]

movies = []
index = 0
while index < len(movies_name):
	movies.append(media.Movie(movies_name[index],urls_image[index],urls_youtube[index]))
	index+=1
fresh_tomatoes.open_movies_page(movies)
