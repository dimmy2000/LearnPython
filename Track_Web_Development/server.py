from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        return f'Погода: {weather["temp_C"]}ºC, {weather["lang_ru"][0]["value"].lower()}. ' \
               f'Ощущается как {weather["FeelsLikeC"]}ºC'
    else:
        return "Сервис погоды временно недоступен."

if __name__ == "__main__":
    app.run(debug=True)