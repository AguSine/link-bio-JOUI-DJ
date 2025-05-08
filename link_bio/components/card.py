import reflex as rx 
from link_bio.styles import styles
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.styles import Size, Spacing
from link_bio import constants as const 

def card(heading: str, text: str, image: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=styles.Size.MORE_BIG.value,
                        height=styles.Size.MORE_BIG.value
                    ),
                    rx.vstack(
                        rx.heading(heading, size="2", margin=Spacing.ZERO.value, padding=Spacing.ZERO.value),
                        rx.text(text, size="1", margin=Spacing.ZERO.value, padding=Spacing.ZERO.value),
                        spacing=Spacing.ZERO.value
                    )
                    ),
                    background_color=Color.PRIMARY.value,
                     _hover= {
            "background_color" : Color.CONTENT.value
       },
            ),
            href=url,
            is_external=True,
            width="70%"
        )
