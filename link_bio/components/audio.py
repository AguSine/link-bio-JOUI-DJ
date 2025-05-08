import reflex as rx 
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color

def audio(url: str) -> rx.Component:
    return rx.audio(
        url= url,
        width="320px",
        height="40px",
        controls=True,
        loop=True,
        padding_x=Size.BIG.value, 
        padding_y=Size.SMALL.value
    )