from modules import *

SESSION_NAME = 'session'

API_ID = 1890553
API_HASH = 'c6f46b5330f5953e5201c3185337ed73'

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = ''

MODULES = {
    # Current time
    'time': Time('%H:%M'),

    # Number of blocked accounts
    #'blocked': BlockedCount(),

    # Number of channel or group members
    'members': MembersCount('androidsmsbomber'),

    # About of the entity
    #'about': EntityInfo('wavecat'),

    # BrawlStars Trophies by tag
    #'trophies': BrawlStarsTrophies('9PG9RCUVY', BRAWLSTARS_TOKEN),
    
    # Iterates strings
    'first_name': Cycle('wavecat', 'retrocat')
}

INTERVAL = 60

TEMPLATES = {
    'about': '⌛: $time 💣: @androidsmsbomber ($members) 🔗: @CTRLIntelligence',
    'first_name': '$first_name',
    'last_name': None
}
