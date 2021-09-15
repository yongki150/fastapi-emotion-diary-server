from enum import Enum


class ModelName(str, Enum):
    KIM = "KIM"
    YONGKI = "YONGKI"


class EmotionColor(str, Enum):
    angry = "backgroundColor6"
    happy = "backgroundColor4"
    sensitiveness = "backgroundColor3"
    blue = "backgroundColor2"
    timid = "backgroundColor5"
