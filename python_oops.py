# class Web_Series:
#     show_name = "Resident Evil"
#     show_length = "67"
    
# web_series_obj = Web_Series()
# print(web_series_obj.show_name)
# print(web_series_obj.show_length)

class Web_Series:
    def __init__(self, name, season, episode):
        self.name = name
        self.season = season
        self.episode = episode
        print("i am hit")

web_1 = Web_Series("Games of Thrones",2,1)
web_2 = Web_Series("Hatim",1,1)        
