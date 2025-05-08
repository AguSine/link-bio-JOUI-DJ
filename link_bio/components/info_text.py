import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.fonts import Font, FontWeight
from link_bio.styles.colors import Color, TextColor

def info_text(image: str, title: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                image,
                width="24px",
                height="auto"
            ),
            rx.text.span(
                title,
                font_size=Size.SMALL_MEDIUM.value,
                fond_weight=FontWeight.MEDIUM.value,
                color=Color.PRIMARY.value
            ),
            align_items="center",
            width="100%"
        )
    )