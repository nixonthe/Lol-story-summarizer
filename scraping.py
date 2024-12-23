import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tqdm import tqdm


def preprocessing(text):
  text = text.lower()
  text = re.sub("['. ]",  '', text)
  return text


if __name__ == '__main__':
    champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia',
                 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard',
                 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia',
                 "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven',
                 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora',
                 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves',
                 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern',
                 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa",
                 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
                 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw",
                 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra', 'Lucian',
                 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi',
                 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus',
                 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf',
                 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn',
                 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata Glasc', 'Renekton',
                 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna',
                 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion',
                 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra',
                 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh',
                 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch',
                 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vex',
                 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick',
                 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick',
                 'Yuumi', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
    new_champions = [preprocessing(x) for x in champions]
    stories = []
    for champion in tqdm(new_champions):
        page = requests.get(
            f'https://universe.leagueoflegends.com/en_AU/story/champion/{champion}/'
        )
        soup = BeautifulSoup(page.content, "html.parser")
        stories.append(soup.find(property="og:description").prettify()[15:-30])
    df = pd.DataFrame(
        {
            'champion': champions,
            'story': stories
        }
    )
    df.to_csv('backend/champions_lore.csv', index=False)
    