import reflex as rx
from link_bio.styles import colors
from link_bio.routes import Route
from link_bio.styles.styles import Size, Spacing
from link_bio.components.audio import audio
from link_bio import constants as const
from link_bio.components.drawer import lateral_menu

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="navbar.png",
                height=Size.VERY_BIG.value,
                width="auto",
                justify="start"
            ),
            href=Route.INDEX.value
        ),
        rx.spacer(),
        lateral_menu(),
        bg=colors.Color.PRIMARY.value,
        position="sticky",
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=Size.BIG.value,
        padding_y=Size.ZERO.value,
        z_index="999",
        top="0",
        width="100%",
        align="center"
    )