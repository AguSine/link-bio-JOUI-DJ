import reflex as rx
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.fonts import Font, FontWeight
from link_bio import constants as const 
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                size="8",
                src="avatar.jpg",
                radius="full",
                padding="2px",
                border="2px solid",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Joui",
                    size="6"
                ),
                rx.text(
                    "@jouimusic",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "icons/facebook.svg",
                        const.FACEBOOK_URL
                    )
                )
            ),
            spacing=Spacing.BIG.value,
            align_items="center"
        ),
        rx.flex(
            info_text(
                "icons/dj.svg",
                "Progressive House"
            ),
            rx.spacer(
                spacing=Spacing.VERY_SMALL.value
            ),
            info_text(
                "icons/dj1.svg",
                "Melodic Techno"
            ),
            rx.spacer(
                spacing=Spacing.VERY_SMALL.value
            ),
            info_text(
                "icons/dj2.svg",
                "Indie Dance"
            ),
        padding_right="3px",
        padding_left="3px",
        spacing=Spacing.BIG.value,
        align_items="start",
        width="100%",
        align_self="stretch"
    ),
    rx.flex(
        rx.text(
                f"""Joui is DJ and producer from Argentina. Her sets are characterized by their energetic nature, 
                combining dark, acidic sounds with vibrant, progressive melodies, all fused with the deep 
                basslines of techno, creating a groove and an unforgettable listening experience. Welcome to my profile.""",
               font_size=Size.MEDIUM.value,
               color=TextColor.BODY.value
            ),
        width="100%",
        align_items="start",
        align_self="stretch",
        padding_right="2px"
        )
    )
    
    