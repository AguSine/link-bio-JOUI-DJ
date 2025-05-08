from enum import Enum

class Font(Enum):
   DEFAULT = "space-mono"
   TITLE = "roc-grotesk-wide"
   OTHER = "space-mono"

class FontWeight(Enum):
   LIGHT = "300"
   DEFAULT = "400"
   MEDIUM = "500"
   BOLD = "600"