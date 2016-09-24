import numpy as np

users_file = "Database/users.dat"
movies_file = "Database/movies.dat"
ratings_file = "Database/ratings.dat"

def parse_input():
    read_file = lambda x : open(x).read().split("\n")[:-1]
    users = read_file(users_file)
    movie = read_file(movies_file)
    rating = read_file(ratings_file)

    get_len = lambda x : int(x[-1].split("::")[0]) + 1
    number_users = get_len(users)
    number_movie = get_len(movie)

    rating_parsed = [[int(l) for l in x.split("::")[:3]] for x in rating if x]
    rating_matrix = [[0 for x in range(number_movie)] for y in range(number_users)]

    for i in rating_parsed:
        rating_matrix[i[0]][i[1]] = i[2]
    
    return np.array(rating_matrix)

if __name__ == "__main__" :
    parse_input()
