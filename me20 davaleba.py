import requests
import json

def fetch_all_characters():
    base_url = "https://rickandmortyapi.com/api/character"
    characters = []

    while base_url:
        response = requests.get(base_url)
        data = response.json()
        characters.extend(data['results'])
        base_url = data['info']['next']

    return characters

def fetch_episode_names(episode_urls):
    episode_names = []
    for url in episode_urls:
        episode_data = requests.get(url).json()
        episode_names.append(episode_data['name'])
    return episode_names

def main():
    character_episodes = {}
    characters = fetch_all_characters()

    for character in characters:
        character_episodes[character['name']] = fetch_episode_names(character['episode'])

    with open('character_episodes_version2.json', 'w', encoding='utf-8') as file:
        json.dump(character_episodes, file, ensure_ascii=False, indent=4)

    print("Saved to character_episodes_version2.json")

if __name__ == "__main__":
    main()
