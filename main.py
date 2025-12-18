import random
import time

class WeatherEngine:
    def __init__(self):
        self.temperature = 25
        self.humidity = 50
        self.wind_speed = 5

    def simulate_change(self):
        self.temperature += random.uniform(-1.5, 1.5)
        self.humidity += random.uniform(-3, 3)
        self.wind_speed += random.uniform(-1, 1)

        self.temperature = max(min(self.temperature, 50), -10)
        self.humidity = max(min(self.humidity, 100), 0)
        self.wind_speed = max(self.wind_speed, 0)

    def report(self):
        return {
            "Temperature": round(self.temperature, 2),
            "Humidity": round(self.humidity, 2),
            "Wind Speed": round(self.wind_speed, 2)
        }

def main():
    engine = WeatherEngine()

    print("Weather Simulation Started\n")
    for i in range(50):
        engine.simulate_change()
        print(f"Cycle {i+1}: {engine.report()}")
        time.sleep(0.2)

if __name__ == "__main__":
    main()
