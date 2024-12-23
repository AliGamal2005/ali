from datetime import date 
class Movie:
    def __init__(self,name,year,director):
        self.name=name
        self.year=year
        self.director=director
        

    def display_info(self):
       
        print(f"the movie {self.name} was released in {self.year} by {self.director}")

    def get_seniority(self):
        currentyear= date.today().year
        return currentyear - self.year







movie1=Movie("inception",2010,"nolan")
print(movie1.name,movie1.year) 
movie1.display_info()
print("seniority:",movie1.get_seniority())