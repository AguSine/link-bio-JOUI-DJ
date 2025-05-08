import reflex as rx
from link_bio import constants as const
from link_bio.styles import styles
from link_bio.styles import colors 

class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open

def popover_content():
    return rx.popover.content(
        rx.flex(
            rx.hstack(
                rx.heading("Welcome to my music",color=colors.Color.BACKGROUND.value, size="5"),
                rx.spacer(),
                rx.popover.close(
                    rx.button(
                        rx.image(
                            src="icons/close.svg",
                            width=styles.Size.BIG.value,
                            height=styles.Size.BIG.value
                        ),
                        padding="0px",
                        margin="0px"
                    ),
                margin_bottom="0px",
                width="10%",
                on_click=DrawerState.toggle_drawer,
                background_color=colors.Color.PRIMARY.value
                )
            ),
            rx.text("Listen to my tracks directly from here", color=colors.Color.BACKGROUND.value, size="3"),
            rx.audio(
                url=const.AUDIO1_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.audio(
                url=const.AUDIO2_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.audio(
                url=const.AUDIO3_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.audio(
                url=const.AUDIO4_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.audio(
                url=const.AUDIO5_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.audio(
                url=const.AUDIO6_URL,
                width="400px",
                height="80px",
                controls=True
            ),
            rx.spacer(),
            rx.hstack(
                rx.spacer(),
                rx.image(
                    src="icons/footer_popover.png",
                    height="auto",
                    width=styles.Size.PLUS_BIG.value,
                    align_items="center",
                    margin="0px"
                ),
                rx.spacer()
            ),
            direction="column",
            spacing="1"
        ),
        padding_top=styles.Size.SMALL.value,
        padding_left=styles.Size.BIG.value,
        padding_right=styles.Size.SMALL_MEDIUM.value,
        padding_bottom=styles.Size.MORE_BIG.value,
        direction="right",
        width="100%",
        height="auto%",
        background_color=colors.Color.PRIMARY.value
    )

def lateral_menu():
    return rx.flex(
        rx.popover.root(
            rx.popover.trigger(
                rx.button(
                    rx.hstack(
                         rx.text(
                            "Music now",
                            style=styles.button_title_style
                        ),
                        rx.image(
                            src="icons/playlist.svg",
                            width=styles.Size.BIG.value,
                            height=styles.Size.BIG.value
                        )
                    ),
                    on_click=DrawerState.toggle_drawer,
                    size="1",
                    padding=styles.Size.SMALL.value,
                    background_color=colors.Color.PRIMARY.value,
                    _hover= {
                        }
                )
            ),
            popover_content(),
            open=DrawerState.is_open,
            modal=False
        ),
        justify="end",
        width="100%"
    )

def popover_sidebar():
    return rx.vstack(
        lateral_menu()
    )

def app():
    return rx.box(
        popover_sidebar(),
        height="100vh",
        width="100vw"
    )