import reflex as rx 
import datetime
from link_bio import constants as const
from link_bio.styles.fonts import Font, FontWeight
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="footer.png",
            height=Size.PLUS_BIG.value
            ),
        rx.link(
            f"© 2020-{datetime.date.today().year} | Joui | DJ and Producer.", 
            href=const.YOUTUBE_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
            color=Color.PRIMARY.value,
            _hover= {"text_color" : Color.SECONDARY.value}
            ),
        rx.hstack(
                rx.text("Making music with"), 
                rx.image(src="lover.svg", width=Size.INTRO_LARGE.value), 
                rx.text("from Argentina to the world."),
            font_size=Size.MEDIUM.value,
            font_family=Font.OTHER.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        align_items="center",
        justify_content="center",
        color=TextColor.FOOTER.value,
        width="100%"
    )
    