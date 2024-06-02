import dataclasses

@dataclasses.dataclass
class HighScore:
    levelId: str
    difficulty: int
    beatmapCharacteristicName: str
    highScore: int
    maxCombo: int
    fullCombo: bool
    maxRank: int
    validScore: bool
    playCount: int