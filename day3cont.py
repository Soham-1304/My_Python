
import random
def get_user_input(prompt,valid_inputs):
     while True:
          user_input=input(prompt).upper()
          if user_input in valid_inputs:
               return user_input
          else:
               print("Invalid Input, Please Try Again")

class KyaKhana:
    def __init__(self):
        self.khana={
            "Breakfast":{
                "South-Indian":["Dosa","Idli Plate","Vada Plate","Idli Vada Plate"],
                "Maharashtrian":["Misal Pav","Upma","Pohe","Vada Pav"],
                "North-Indian":["Paratha","Puri Bhaji","Pakode","Samosa"]
            },
            "Lunch":{
                "South-Indian":["Rassam and Rice","Biryani","Uttapa"],
                "Maharashtrian":["Thaalipeeth","Bhakari Bhaji","Tandulachi Khichdi"],
                "North-Indian":["Dal Roti","Chole Bhature","Roti Sabzi"]
            },
            "Dinner":{
                "South-Indian":["Upma","Biryani","Payasam"],
                "Maharashtrian":["Amti Bhaat","Zhunka Bhakari","Usal and Poli"],
                "North-Indian":["Kheer","Kadhi Pakoda","Sarso ka Saag"]
            }
        }
    def recommend_meal(self,time_of_day,dietary_preference):
        if time_of_day not in self.khana:
            return "Invalid time of day, Please choose from breakfast, lunch or dinner"
        if dietary_preference not in self.khana[time_of_day]:
            return "Invalid preference, Please choose from South-Indian, North-Indian and Maharashtrian"
        meal_options=self.khana[time_of_day][dietary_preference]
        return random.choice(meal_options)
    
def get_time_of_day():
     return get_user_input("What Time of the day is it? (B=Breakfast/L=Lunch/D=Dinner): ",['B','L','D'])
def get_dietary_preference():
     return get_user_input("What is your preference? N=North-Indian,S=South-Indian,M=Maharashtrian: ",['N','S','M'])
     
def main():
        recommender=KyaKhana()
        print("\nWelcome to the Meal Recommendation Program! ")
        time_of_day=get_time_of_day()
        if time_of_day=='B':
             time_of_day='Breakfast'
        elif time_of_day=='L':
             time_of_day='Lunch'
        else:
             time_of_day='Dinner'
        
        dietary_preference=get_dietary_preference()
        if dietary_preference=='N':
             dietary_preference='North-Indian'
        elif dietary_preference=='S':
             dietary_preference='South-Indian'
        else:
             dietary_preference='Maharashtrian'
    
        recommended_meal=recommender.recommend_meal(time_of_day,dietary_preference)
        print(f"Based on your preference , We recommend you {recommended_meal}")

if __name__=="__main__":
        main()












        