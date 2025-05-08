import reflex as rx
from enum import Enum
from link_bio.styles.colors import Color as Color 
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font as Font
from link_bio.styles.fonts import FontWeight as FontWeight

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.2em"
    SMALL = "0.5em"
    SMALL_MEDIUM = "0.7em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    INTRO_LARGE = "1.3em"
    LARGE = "1.5em"
    BIG = "2em"
    MORE_BIG = "2.5em"
    VERY_BIG ="3em"
    PLUS_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Styles
STYLESHEETS = [
    "https://use.typekit.net/qng8xuj.css"
]

BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color" : Color.BACKGROUND.value,
    rx.heading : {
        "size" : "6",
        "color" : TextColor.HEADER.value,
        "font_family" : Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button : {
       "width" : "100%",
       "height" : "100%",
       "display" : "block",
       "padding" : Size.SMALL.value,
       "border_radius" : Size.DEFAULT.value,
       "color" : TextColor.HEADER.value,
       "background_color" : Color.CONTENT.value,
       "_hover" : {
            "background_color" : Color.PRIMARY.value
       }
    },
    rx.link : {
        "text_decoration" : "none",
        "_hover" : {}
    },
    rx.audio : {
        "background" : Color.PRIMARY.value,
        "_hover" : {
            "background_color" : Color.PRIMARY.value
       }
    }

}

title_style = dict(
    width="100%",
    font_size= Size.INTRO_LARGE.value,
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.INTRO_LARGE.value,
    color=TextColor.HEADER.value
)