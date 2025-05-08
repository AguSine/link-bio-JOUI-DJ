import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.video import video
from link_bio.components.title import title
from link_bio.components.card import card
from link_bio import constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("My last set"),
        video(const.VIDEO_URL),
        card("Tour Dates", "Get updates on new shows, music, and more.", "bandsintow.svg", const.DATES_URL),
        title("Community"),
        link_button("Spotify", "icons/spotify.svg", const.SPOTIFY_URL),
        link_button("YouTube", "icons/youtube.svg", const.YOUTUBE_URL),
        link_button("SoundCloud", "icons/soundcloud.svg", const.SOUNDCLOUD_URL),
        link_button("Beatport", "icons/beatport.svg", const.BEATPORT_URL),
        title("Contact me"),
        link_button("Gmail", "icons/gmail.svg", f"mailto:{const.EMAIL}"),
        link_button("CRIB Agency", "icons/crib.ico", const.CRIB_AGENCY),
        align_items="center",
        width="100%"
    )