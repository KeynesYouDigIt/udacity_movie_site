import webbrowser

class Movie ():
    """ This class stores a movie for the trailer db
    Title - Movie's name
    
    Image - any related image for the link
    
    Plot - a short description of the movie, should not exceed a paragraph.
    should avoid spilers too!!

    RT_rating - Link to rating on Rotten Tomatoes

    Trailer - Link to the Trailer. Target of instance method show_trailer.

    """
    def __init__ (self, Title, Image, Plot, RT_rating, Trailer):
        self.Title = Title
        self.Image = Image
        self.Plot = Plot
        self.RT_rating = RT_rating
        self.Trailer = Trailer


    def show_trailer(self):
        #This method can be called to open tabs with the RT rating and trailer.
        #it has only been tested in chrome.
        webbrowser.open(self.RT_rating)
        webbrowser.open(self.Trailer)