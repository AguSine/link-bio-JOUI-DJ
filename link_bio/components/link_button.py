import reflex as rx 
from link_bio.styles import styles

def link_button(text: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value
                ),
                rx.text(text, style=styles.button_title_style)
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )