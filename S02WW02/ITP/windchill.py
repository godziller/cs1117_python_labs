airTemp = float(input("What is the wind temperature: "))
windSpeed = float(input("What is the wind Speed: "))

def wind_chill_index(temp, speed):
    WCI = 13.12 + 0.6215 * temp - 11.37 * speed ** 0.16 + 0.3965 * temp * speed * 0.16
    print(f"The Wind Chill Index is: {int(WCI)}")

#wind_chill_index(airTemp, windSpeed)

#now i will import this 