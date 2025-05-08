import reflex as rx 
from link_bio.components.navbar import navbar as navbar
from link_bio.components.footer import footer as footer
from link_bio.components.video import video as video
from link_bio.views.header import header as header
from link_bio.styles import styles
from link_bio.styles.styles import Size
from link_bio.views.links import links as links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)

app.add_page(
    index,
    title="Joui | Listen to my music from here",
    description="Joui is an emerging DJ and producer from Argentina who captivates audiences with her mixes and unique style that fuses Progressive House, Melodic Techno, Indie Dance, and more."
)

app._compile()