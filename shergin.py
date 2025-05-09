class Soldier:
    def _init_(self, name, heart_rate, temperature):
        self.name = name
        self.heart_rate = heart_rate
        self.temperature = temperature

    def check_health(self):
        if self.heart_rate < 50 or self.heart_rate > 100:
            return f"Alert: {self.name}'s heart rate is abnormal!"
        if self.temperature < 36 or self.temperature > 38:
            return f"Alert: {self.name}'s body temperature is abnormal!"
        return f"{self.name} is healthy."

# Example usage
soldier1 = Soldier("John Doe", 120, 37)
soldier2 = Soldier("Jane Doe", 70, 35)

print(soldier1.check_health())
print(soldier2.check_health())