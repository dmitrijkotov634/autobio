from modules.memberscount import MembersCount
from modules.strings import Ticker
from modules.time import Time

"""
from modules.supercell import BrawlStarsTrophies, ClashRoyaleTrophies
from modules.openweathermap import OpenWeatherMap
from modules.blockedcount import BlockedCount
from modules.entityinfo import EntityInfo
from modules.lastfm import LastFm
from modules.strings import Cycle
"""

SESSION_NAME = "session"

API_ID = 1890553
API_HASH = "c6f46b5330f5953e5201c3185337ed73"

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = ""

# http://www.last.fm/api/account/create
LASTFM_KEY = "50c4da48aa16885c9e91a6d417d601e7"  # usable example key
LASTFM_USERNAME = ""  # enter your last.fm username

# https://openweathermap.org
OPENWEATHERMAP_APP_ID = ""

PLACEHOLDER = "_"

MODULES = {
    # Current time
    "time": Time("%H:%M"),

    # Number of blocked accounts
    # "blocked": BlockedCount(),

    # Number of channel or group members
    "members": MembersCount("androidsmsbomber"),

    # About of the entity
    # "about": EntityInfo("wavecat"),

    # BrawlStars Trophies by tag
    # "trophies": BrawlStarsTrophies("9PG9RCUVY", BRAWLSTARS_TOKEN),

    # Iterates strings
    # "first_name": Cycle("wavecat", "retrocat"),

    # Ticker
    "first_name": Ticker("retrocat "),

    # LastFM now playing
    # "music": LastFm(LASTFM_KEY, LASTFM_USERNAME),

    # Weather
    # "weather": OpenWeatherMap(OPENWEATHERMAP_APP_ID, "Moscow"),
}

INTERVAL = 60

TEMPLATES = {
    "about": "@androidsmsbomber ($members) -> @CTRLIntelligence",
    "first_name": "$first_name",
    "last_name": ": $time"
}
