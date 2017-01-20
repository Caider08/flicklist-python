import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movielist = ["Dumb&Dumber", "IndependanceDay", "Fight Club", "Fantasia", "Mars Attack"]


        # TODO: randomly choose one of the movies, and return it
        movie = random.choice(movielist)
        return movie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tom_movie = self.getRandomMovie()

        while tom_movie == movie:
            tom_movie = self.getRandomMovie()


        content += "<h1>Tomorrow's Movie</h1>"
        content += "<p>" + tom_movie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
