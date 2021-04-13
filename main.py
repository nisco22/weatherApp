from tkinter import *
import requests
import json

def zipcode():
    global mylabel
    try:

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=5CFF84B7-DD95-4435-8C53-8A5D61F3E3B2")
        api = json.loads(api_request.content)

        place = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "green"

        elif category == "Moderate":
            weather_color = "yellow"

        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "brown"

        elif category == "Unhealthy":
            weather_color = "purple"

        elif category == "Very Unhealthy":
            weather_color = "pink"

        elif category == "Harzadous":
            weather_color = "red"
        
        root.config(background=weather_color)

        mylabel.destroy()

        mylabel = Label(root, text = place +" " + "Air Quality" + " " + str(quality) + " " + category, font=('Helvetica', 15), background=weather_color)
        mylabel.grid(row=0, column=0, padx=15, pady=10)

        zip.delete(0, END)

    except Exception as e:
        api = 'Error...'
    


root = Tk()
root.geometry('400x200')

mylabel = Label(root)

zip = Entry(root, width=35, bd=2)
zip.grid(row=1, column=0, padx=15, pady=(15, 0))

zipBtn = Button(root, text="Submit Area Zipcode", command=zipcode)
zipBtn.grid(row=2, column=0, padx=15, pady=5)


root.mainloop()