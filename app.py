from typing import Dict, List, Tuple
import datetime
from dataclasses import dataclass
from groq import Groq

# Constants
GROQ_API_KEY = "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"  # Replace with your Groq API key
client = Groq(api_key=GROQ_API_KEY)

ZODIAC_DATES = [
    ((3, 21), (4, 19), "Aries"),
    ((4, 20), (5, 20), "Taurus"),
    ((5, 21), (6, 20), "Gemini"),
    ((6, 21), (7, 22), "Cancer"),
    ((7, 23), (8, 22), "Leo"),
    ((8, 23), (9, 22), "Virgo"),
    ((9, 23), (10, 22), "Libra"),
    ((10, 23), (11, 21), "Scorpio"),
    ((11, 22), (12, 21), "Sagittarius"),
    ((12, 22), (1, 19), "Capricorn"),
    ((1, 20), (2, 18), "Aquarius"),
    ((2, 19), (3, 20), "Pisces")
]

ZODIAC_CHARACTERISTICS = {
    "Aries": {
        "element": "Fire",
        "ruling_planet": "Mars",
        "qualities": ["Leadership", "Courage", "Energy"],
        "compatible_signs": ["Leo", "Sagittarius", "Gemini"],
        "lucky_numbers": [1, 8, 17],
        "lucky_colors": ["Red", "Orange"],
        "lucky_days": ["Tuesday", "Saturday"]
    }
    # Add characteristics for other signs here
}

@dataclass
class UserProfile:
    name: str
    dob: datetime.date
    time_of_birth: datetime.time
    gender: str
    state: str
    city: str
    language: str
    zodiac_sign: str = None

    def __post_init__(self):
        self.zodiac_sign = self.calculate_zodiac_sign()

    def calculate_zodiac_sign(self) -> str:
        """Calculate zodiac sign based on date of birth"""
        day = self.dob.day
        month = self.dob.month

        for (start_month, start_day), (end_month, end_day), sign in ZODIAC_DATES:
            if ((month == start_month and day >= start_day) or
                    (month == end_month and day <= end_day)):
                return sign
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        return "Unknown"

class SpiritualGuide:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def _get_response(self, prompt: str) -> str:
        """Get response from Groq API"""
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert spiritual guide providing detailed and complete responses."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                stream=False
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating response: {str(e)}. Please try again later."

    def get_daily_horoscope(self, sign: str) -> str:
        prompt = f"""As an expert astrologer, provide a comprehensive daily horoscope for {sign}.
        Include:
        - General Outlook
        - Love & Relationships
        - Career & Money
        - Health & Wellness"""
        return self._get_response(prompt)

    def get_gemstone_recommendation(self, sign: str) -> str:
        prompt = f"""As an expert gemologist and astrologer, provide detailed gemstone recommendations for {sign}.
        Include:
        - Primary Gemstones
        - Wearing Guidelines
        - Alternative Options
        - Care Instructions"""
        return self._get_response(prompt)

    def generate_kundali(self, dob: datetime.date, time_of_birth: datetime.time) -> str:
        prompt = f"""Provide a detailed kundali analysis for:
        Date: {dob}
        Time: {time_of_birth}
        Include:
        - Planetary Positions
        - Life Path Analysis
        - Key Life Areas
        - Recommendations"""
        return self._get_response(prompt)

    def get_meditation_guidance(self, sign: str) -> str:
        prompt = f"""Provide meditation guidance for {sign}.
        Include:
        - Type of meditation
        - Focus points
        - Duration and frequency
        - Benefits"""
        return self._get_response(prompt)

    def get_workout_recommendations(self, sign: str) -> str:
        prompt = f"""Provide workout recommendations for {sign}.
        Include:
        - Exercise types
        - Routines
        - Frequency
        - Benefits"""
        return self._get_response(prompt)

    def predict_future_triggers(self, sign: str) -> str:
        prompt = f"""Predict astrological triggers for {sign}.
        Include:
        - Types of triggers
        - Expected impacts
        - Strategies
        - Timing"""
        return self._get_response(prompt)

    def get_pooja_recommendation(self, sign: str) -> str:
        prompt = f"""Recommend specific Poojas for {sign}.
        Include:
        - Types of Poojas
        - Timing
        - Mantras
        - Benefits"""
        return self._get_response(prompt)

    def spiritual_chatbot(self, query: str, sign: str) -> str:
        prompt = f"""As a spiritual guide, respond to this query for {sign}: '{query}'
        Include:
        - Zodiac-specific insights
        - Astrological influences
        - Practical guidance"""
        return self._get_response(prompt)

def main():
    # Example usage
    guide = SpiritualGuide(GROQ_API_KEY)
    
    # Create user profile
    user = UserProfile(
        name="John Doe",
        dob=datetime.date(1990, 5, 15),
        time_of_birth=datetime.time(12, 30),
        gender="Male",
        state="California",
        city="Los Angeles",
        language="English"
    )
    
    # Get various spiritual insights
    horoscope = guide.get_daily_horoscope(user.zodiac_sign)
    gemstones = guide.get_gemstone_recommendation(user.zodiac_sign)
    kundali = guide.generate_kundali(user.dob, user.time_of_birth)
    meditation = guide.get_meditation_guidance(user.zodiac_sign)
    
    # Print results
    print(f"Welcome {user.name}! Your zodiac sign is {user.zodiac_sign}")
    print("\nDaily Horoscope:")
    print(horoscope)
    print("\nGemstone Recommendations:")
    print(gemstones)
    print("\nKundali Analysis:")
    print(kundali)
    print("\nMeditation Guidance:")
    print(meditation)

if __name__ == "__main__":
    main()
