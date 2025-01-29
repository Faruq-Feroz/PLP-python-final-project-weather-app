# PLP python final project: Django Weather App 🌤️

## Description
A simple weather application built with Django that displays current weather information for any city using the OpenWeatherMap API.

## Features ✨
* Search for weather by city name
* Display current temperature in Celsius
* Show weather description and icon
* Display humidity and wind speed
* Responsive design using Tailwind CSS
* Error handling for invalid city names

## Technologies Used 🛠️
* Python 3.8+
* Django 4.0+
* OpenWeatherMap API
* HTML

## Prerequisites 📋
* Python 3.8 or higher
* Django 4.0 or higher
* requests library
* OpenWeatherMap API key

## Installation & Setup 🚀

### 1. Clone the repository
```bash
git clone Faruq-Feroz/PLP-python-final-project-weather-app.git
cd PLP-python-final-project-weather-app

### 2. Set up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django requests
```

### 4. API Setup
* Sign up at [OpenWeatherMap](https://openweathermap.org/api)
* Copy your API key
* Replace 'YOUR_API_KEY' in weather_app/views.py with your actual API key

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Start Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Visit http://127.0.0.1:8000/ in your web browser

## Project Structure 📁
```
weather_project/
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather_app/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── weather_app/
│           └── index.html
└── manage.py
```

## Usage Guide 📖
1. Enter a city name in the search box
2. Click the "Search" button
3. View the current weather information:
   * Temperature
   * Weather description
   * Weather icon
   * Humidity
   * Wind speed

## Error Handling ⚠️
The application includes handling for:
* Invalid city names
* API request failures
* Missing input validation

## Contributing 🤝
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏
* OpenWeatherMap API for weather data


## Contact 📧
Hassan Faruq - hassanferoz333@gmail.com
