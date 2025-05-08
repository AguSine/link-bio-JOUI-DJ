import reflex as rx

def video(url: str) -> rx.Component:
    return rx.box(
            rx.video(
                url = url,
                width="100%",
                height="300px"
            ),
            border_radius="16px",
            overflow="hidden",
            width="100%",
            max_width="560px",
            margin="auto"
    )