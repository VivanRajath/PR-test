import random
import asyncio

class WeatherEngine:
    """
    The WeatherEngine class simulates weather conditions by generating random temperature, humidity, and wind speed changes.

    Attributes:
        temperature (float): The current temperature.
        humidity (float): The current humidity.
        wind_speed (float): The current wind speed.

    Methods:
        simulate_change: Simulates a change in the weather conditions.
        report: Returns the current weather conditions.
    """
    def __init__(self):
        self.temperature = 25
        self.humidity = 50
        self.wind_speed = 5
        self.report_cache = None

    def simulate_change(self):
        try:
            self.temperature += random.uniform(-1.5, 1.5)
            self.humidity += random.uniform(-3, 3)
            self.wind_speed += random.uniform(-1, 1)

            self.temperature = max(min(self.temperature, 50), -10)
            self.humidity = max(min(self.humidity, 100), 0)
            self.wind_speed = max(self.wind_speed, 0)
            self.report_cache = None
        except Exception as e:
            print(f"An error occurred during simulation: {str(e)}")

    def report(self):
        if self.report_cache is None:
            self.report_cache = {
                "Temperature": round(self.temperature, 2),
                "Humidity": round(self.humidity, 2),
                "Wind Speed": round(self.wind_speed, 2)
            }
        return self.report_cache

async def main():
    """
    The main function initializes the WeatherEngine and runs a simulation of 50 cycles, 
    printing the weather conditions after each cycle.

    The simulation demonstrates how the weather conditions change over time, 
    with random variations in temperature, humidity, and wind speed.
    """
    engine = WeatherEngine()

    print("Weather Simulation Started\n")
    for i in range(50):
        engine.simulate_change()
        print(f"Cycle {i+1}: {engine.report()}")
        await asyncio.sleep(0.2)

if __name__ == "__main__":
    asyncio.run(main())