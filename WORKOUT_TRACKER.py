# WORK OUT MONITORING PROJECT

#TODO import modules
import requests
import datetime as dt

#TODO constants
NUTRITIONIX_APPID="aba1aef5"
NUTRITIONIX_APPKEY="a96ab95c4df192946bf890eb5710e3ee"
GENDER="male"
AGE="21"
WEIGHT=62
HEIGHT=178

#TODO find calories burnt
natural_exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
headers={
          "x-app-id":NUTRITIONIX_APPID
         ,"x-app-key":NUTRITIONIX_APPKEY
         ,"Content-Type":"application/json"
         }
content={
    "query":input("Tell me which exercise you did ? \n"),
    "gender":GENDER,
    "height_cm":HEIGHT,
    "age":AGE
}
response=requests.post(url=natural_exercise_endpoint,json=content,headers=headers)
print(response)

#TODO find necessary variables for googlesheet
exercise_data=response.json()
print(exercise_data)
today_date=dt.datetime.now()
time_hour=today_date.hour
time_minute=today_date.minute

calories_burnt=exercise_data["exercises"][0]["nf_calories"]
duration=exercise_data["exercises"][0]["duration_min"]
type_of_exercise=exercise_data["exercises"][0]["name"].title()
formatted_time=f"{time_hour}:{time_minute}"
formatted_date=today_date.strftime("%d/%m/%y")

print(calories_burnt,duration,type_of_exercise,formatted_date,formatted_time)


#TODO upload variables to googlesheet through sheety
sheety_endpoint="https://api.sheety.co/eb1d80cb386cef1092824698410439ad/myWorkouts/workouts"
sheet_variables={
    "workout":{
        "Date":formatted_date
        ,"Time":formatted_time
        ,"Exercise":type_of_exercise
        ,"Duration":duration
        ,"Calories":calories_burnt
    }
}
print(sheet_variables)
sheety_response=requests.post(url=sheety_endpoint,json=sheet_variables)
print(sheety_response)
print(sheety_response.text)