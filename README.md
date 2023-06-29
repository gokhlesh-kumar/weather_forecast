# weather_forecast

The Weather Forecast Application is a web-based application that allows users to retrieve the weather forecast for a specific location based on latitude and longitude coordinates. 
The application utilizes the OpenWeatherMap API to fetch weather data and provides users with different options for detailing the forecast.

Key Features:

User Input: Users can enter the latitude and longitude coordinates of the desired location through an input form.
Detailing Type Selection: Users can choose from three options to specify the level of forecast detail: Minute forecast for 1 hour, Hourly forecast for 48 hours, or Daily forecast for 7 days.
Data Storage: The application stores weather forecast data in a local database. It checks the database first to retrieve the requested data and, if not available or outdated, fetches the data from the OpenWeatherMap API and updates the local database.
Time Sensitivity: The stored weather forecast data is time-sensitive and configurable. By default, the application considers data older than 10 minutes as outdated and retrieves fresh data from the API.
Google Maps Integration: The application provides the option to input location coordinates using a Google Maps plugin, enhancing the user experience.
How it Works:

User enters the latitude and longitude coordinates of the desired location.
User selects the desired detailing type for the weather forecast.
The application checks the local database for the requested weather data.
If the data is available and within the time sensitivity threshold, it is retrieved from the database and displayed to the user.
If the data is not available or outdated, the application requests the data from the OpenWeatherMap API and saves it to the local database.
The updated weather forecast data is then displayed to the user.
The frontend of the application is built using HTML, CSS, and JavaScript. It provides a user-friendly interface where users can input their desired location and detailing type. The weather forecast data is presented in a structured manner, with the option to view the output in stylish cards.

The backend of the application is developed using the Django framework in Python. It handles the API requests, data retrieval and storage, and communicates with the OpenWeatherMap API to fetch weather data. The local database stores the weather forecast data and is updated as needed.

Overall, the Weather Forecast Application provides users with an easy and efficient way to obtain accurate weather forecasts for specific locations, with the ability to choose the level of detail required. It combines the power of an external weather API with local data storage for enhanced performance and flexibility.

![Weather](https://github.com/gokhlesh-kumar/weather_forecast/assets/104709144/65ae4487-c54d-4088-8982-621618d7db5b)

