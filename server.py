
# f2134c3272e8b021ff7a2d1342f83ddd


from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/getCity', methods=['POST'])
def getCity():
    city = request.form['city']
    api_key = "f2134c3272e8b021ff7a2d1342f83ddd"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        weather_data = {
            "city": city,
            "country": data["sys"]["country"],
            # 'flag': weather_data['flags']['png'],
            "temperature": round(data["main"]["temp"] - 273.15, 2),  # Convert from Kelvin to Celsius
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
            "weather_description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "visibility": data.get("visibility", "N/A")
        }
    else:
        weather_data = {"error": "City not found"}   

    return render_template('home.html', data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
