import requests
import json
from datetime import datetime

class JokeGenerator:
    """Random joke generator using external APIs"""
    
    def __init__(self):
        self.api_url = "https://api.jokes.one/joke"
        self.fallback_api = "https://v2.jokeapi.dev/joke/Any"
        self.joke_history = []
    
    def get_random_joke_from_api(self):
        """Fetch a random joke from jokes.one API"""
        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if data.get('success'):
                joke_text = data.get('contents', {}).get('jokes', [{}])[0].get('joke', '')
                return {
                    'joke': joke_text,
                    'source': 'jokes.one',
                    'timestamp': datetime.now().isoformat()
                }
        except (requests.RequestException, json.JSONDecodeError, IndexError) as e:
            print(f"Error fetching from jokes.one: {e}")
        
        return None
    
    def get_random_joke_fallback(self):
        """Fetch a random joke from fallback API (JokeAPI)"""
        try:
            response = requests.get(self.fallback_api, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if data.get('type') == 'single':
                joke_text = data.get('joke', '')
            else:
                joke_text = f"{data.get('setup', '')} {data.get('delivery', '')}"
            
            return {
                'joke': joke_text,
                'source': 'JokeAPI',
                'category': data.get('category', 'General'),
                'timestamp': datetime.now().isoformat()
            }
        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f"Error fetching from JokeAPI: {e}")
        
        return None
    
    def get_joke(self):
        """Get a random joke, trying primary API first, then fallback"""
        joke = self.get_random_joke_from_api()
        
        if not joke:
            joke = self.get_random_joke_fallback()
        
        if joke:
            self.joke_history.append(joke)
        
        return joke
    
    def get_multiple_jokes(self, count=5):
        """Get multiple random jokes"""
        jokes = []
        for _ in range(count):
            joke = self.get_joke()
            if joke:
                jokes.append(joke)
        return jokes
    
    def get_joke_history(self):
        """Get all jokes fetched in current session"""
        return self.joke_history
    
    def clear_history(self):
        """Clear joke history"""
        self.joke_history = []


def main():
    """Main function to demonstrate joke generator"""
    print("🎭 Random Joke Generator 🎭")
    print("=" * 50)
    
    generator = JokeGenerator()
    
    # Get a single joke
    print("\n📢 Fetching a random joke...\n")
    joke = generator.get_joke()
    
    if joke:
        print(f"📝 Joke: {joke['joke']}")
        print(f"📍 Source: {joke['source']}")
        if 'category' in joke:
            print(f"🏷️  Category: {joke['category']}")
        print()
    else:
        print("❌ Could not fetch a joke. Please check your internet connection.\n")
    
    # Get multiple jokes
    print("=" * 50)
    print("\n🎪 Fetching 3 more jokes...\n")
    multiple_jokes = generator.get_multiple_jokes(3)
    
    for i, j in enumerate(multiple_jokes, 1):
        print(f"{i}. {j['joke']}")
        print(f"   (Source: {j['source']})\n")
    
    # Show history
    print("=" * 50)
    print(f"\n📊 Total jokes fetched: {len(generator.get_joke_history())}\n")


if __name__ == "__main__":
    main()
