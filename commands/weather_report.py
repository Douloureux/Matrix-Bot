from lib import weather
from datetime import datetime

def _weather_report() -> weather.WeatherReport:
    return weather.getWeather()

def weatherData() -> str:
    data = _weather_report()
    current_time = int(datetime.now().strftime('%H'))
    
    return_list = ["<table>", "<tr>", "<th>Time</th>", "<th>Temperature</th>", "<th>Chance of rain</th>", "</tr>"]

    i = current_time
    while i < len(data.getTime()):
        return_list.append("<tr>")
        return_list.append(f"<td>{data.getTime()[i]}</td>")
        return_list.append(f"<td>{data.getTemperature()[i]}°C</td>")
        return_list.append(f"<td>{data.getPrecipitation()[i]}%</td>")
        return_list.append("</tr>")
        i += 1

    table = '\n'.join(return_list)   
    message = (
f"""
<h1>Weather Report</h1>

<table>
    <tr>
        <th>Current</th>
        <th>UV Index</th>
        <th>High</th>
        <th>Low</th>
    </tr>
    <tr>
        <td>{data.getTemperature()[current_time]}°C</td>
        <td>{data.getUvIndex()[0]}</td>
        <td>{data.getMaxTemp()[0]}°C</td>
        <td>{data.getMinTemp()[0]}°C</td>
    </tr>
</table>

<br>

{table}
"""
    )

    return message