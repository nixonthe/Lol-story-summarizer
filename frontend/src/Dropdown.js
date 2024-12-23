import React, { useState } from "react";

const Dropdown = ({ onChampionSelect }) => {
  // State to store selected option
  const [selectedChampion, setSelectedChampion] = useState("");

  // List of champion names for the dropdown
  const champions = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia",
    "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard",
    "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia",
    "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven",
    "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora",
    "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves",
    "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa",
    "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
    "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw",
    "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian",
    "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi",
    "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus",
    "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu", "Olaf",
    "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn",
    "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton",
    "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna",
    "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion",
    "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
    "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh",
    "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex",
    "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick",
    "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick",
    "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra",
  ];

  // Handle selection change
  const handleSelectChange = (event) => {
    const champion = event.target.value;
    setSelectedChampion(champion); // Update state
    onChampionSelect(champion); // Trigger parent function (if provided)
  };

  return (
    <div className="dropdown-container">
      <label
        htmlFor="champion-select"
        className="dropdown-label" // Highlighting class
      >
        Choose a champion:
      </label>
      <select
        id="champion-select"
        value={selectedChampion}
        onChange={handleSelectChange}
      >
        <option value="">Select a champion</option>
        {champions.map((champion) => (
          <option key={champion} value={champion}>
            {champion}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Dropdown;
