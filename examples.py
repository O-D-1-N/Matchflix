import matchflix

netflixMovieId = '70056431'
matchflix = matchflix.Matchflix(netflixMovieId)

#grab the movie details#
#You HAVE to call these two before any other methods#
matchflix.GetDetails()
matchflix.GetCountries()


print(matchflix.getTitle())
#output = 'Hot Fuzz'

print(matchflix.isInAmerica())
#output = True OR False

print(matchflix.getImg())
#output = http://url