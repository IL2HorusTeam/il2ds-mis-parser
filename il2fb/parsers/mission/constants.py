# -*- coding: utf-8 -*-
"""
Different constants.
"""
from il2fb.parsers.mission.helpers import _


###############################################################################
# Commons
###############################################################################

# Skills ----------------------------------------------------------------------
SKILL_ROOKIE = 'rookie'
SKILL_AVERAGE = 'average'
SKILL_VETERAN = 'veteran'
SKILL_ACE = 'ace'

SKILLS_NAMES = {
    SKILL_AVERAGE: _("rookie"),
    SKILL_ROOKIE: _("average"),
    SKILL_VETERAN: _("veteran"),
    SKILL_ACE: _("ace"),
}

SKILLS_MAP = {
    '0': SKILL_ROOKIE,
    '1': SKILL_AVERAGE,
    '2': SKILL_VETERAN,
    '3': SKILL_ACE,
}

###############################################################################
# Structure
###############################################################################

# Armies ----------------------------------------------------------------------
ARMY_NONE = 'none'
ARMY_RED = 'red'
ARMY_BLUE = 'blue'
ARMY_GREEN = 'green'
ARMY_GOLD = 'gold'
ARMY_PURPLE = 'purple'
ARMY_AQUA = 'aqua'
ARMY_MAROON = 'maroon'
ARMY_NAVY = 'navy'
ARMY_EMERALD = 'emerald'
ARMY_OLIVE = 'olive'
ARMY_MAGENTA = 'magenta'
ARMY_TEAL = 'teal'
ARMY_ORANGE = 'orange'
ARMY_TURQUOISE = 'turquoise'
ARMY_BROWN = 'brown'
ARMY_SALAD = 'salad'

ARMIES_NAMES = {
    ARMY_NONE: _("none"),
    ARMY_RED: _("red"),
    ARMY_BLUE: _("blue"),
    ARMY_GREEN: _("green"),
    ARMY_GOLD: _("gold"),
    ARMY_PURPLE: _("purple"),
    ARMY_AQUA: _("aqua"),
    ARMY_MAROON: _("maroon"),
    ARMY_NAVY: _("navy"),
    ARMY_EMERALD: _("emerald"),
    ARMY_OLIVE: _("olive"),
    ARMY_MAGENTA: _("magenta"),
    ARMY_TEAL: _("teal"),
    ARMY_ORANGE: _("orange"),
    ARMY_TURQUOISE: _("turquoise"),
    ARMY_BROWN: _("brown"),
    ARMY_SALAD: _("salad"),
}

ARMIES_MAP = {
    '0': ARMY_NONE,
    '1': ARMY_RED,
    '2': ARMY_BLUE,
    '3': ARMY_GREEN,
    '4': ARMY_GOLD,
    '5': ARMY_PURPLE,
    '6': ARMY_AQUA,
    '7': ARMY_MAROON,
    '8': ARMY_NAVY,
    '9': ARMY_EMERALD,
    '10': ARMY_OLIVE,
    '11': ARMY_MAGENTA,
    '12': ARMY_TEAL,
    '13': ARMY_ORANGE,
    '14': ARMY_TURQUOISE,
    '15': ARMY_BROWN,
    '16': ARMY_SALAD,
}

# Air forces ------------------------------------------------------------------

AIR_FORCES = {
    'ru': 'vvs_rkka',
    'fr': 'vvs_france',
    'pl': 'vvs_poland',
    'gb': 'raf',
    'du': 'vvs_holland',
    'rz': 'rnzaf',
    'ra': 'raaf',
    'rn': 'royal_navy',
    'us': 'usaaf',
    'um': 'usmc',
    'un': 'usn',
    'de': 'luftwaffe',
    'fi': 'vvs_finland',
    'it': 'vvs_italy',
    'ro': 'vvs_romania',
    'hu': 'vvs_hungary',
    'sk': 'vvs_slovakia',
    'ja': 'ija',
    'in': 'ijn',
    'nn': None,
    'null': None,
}

###############################################################################
# Targets
###############################################################################

# Target types ----------------------------------------------------------------
TARGET_TYPE_DESTROY_CODE = '0'
TARGET_TYPE_DESTROY_AREA_CODE = '1'
TARGET_TYPE_DESTROY_BRIDGE_CODE = '2'
TARGET_TYPE_RECON_CODE = '3'
TARGET_TYPE_ESCORT_CODE = '4'
TARGET_TYPE_COVER_CODE = '5'
TARGET_TYPE_COVER_AREA_CODE = '6'
TARGET_TYPE_COVER_BRIDGE_CODE = '7'

TARGET_TYPE_DESTROY = 'destroy'
TARGET_TYPE_DESTROY_AREA = 'destroy_area'
TARGET_TYPE_DESTROY_BRIDGE = 'destroy_bridge'
TARGET_TYPE_RECON = 'recon'
TARGET_TYPE_ESCORT = 'escort'
TARGET_TYPE_COVER = 'cover'
TARGET_TYPE_COVER_AREA = 'cover_area'
TARGET_TYPE_COVER_BRIDGE = 'cover_bridge'

TARGET_TYPES_NAMES = {
    TARGET_TYPE_DESTROY: _("destroy"),
    TARGET_TYPE_DESTROY_BRIDGE: _("destroy bridge"),
    TARGET_TYPE_DESTROY_AREA: _("destroy area"),
    TARGET_TYPE_RECON: _("recon"),
    TARGET_TYPE_ESCORT: _("escort"),
    TARGET_TYPE_COVER: _("cover"),
    TARGET_TYPE_COVER_AREA: _("cover area"),
    TARGET_TYPE_COVER_BRIDGE: _("cover bridge"),
}

TARGET_TYPES_MAP = {
    TARGET_TYPE_DESTROY_CODE: TARGET_TYPE_DESTROY,
    TARGET_TYPE_DESTROY_BRIDGE_CODE: TARGET_TYPE_DESTROY_BRIDGE,
    TARGET_TYPE_DESTROY_AREA_CODE: TARGET_TYPE_DESTROY_AREA,
    TARGET_TYPE_RECON_CODE: TARGET_TYPE_RECON,
    TARGET_TYPE_ESCORT_CODE: TARGET_TYPE_ESCORT,
    TARGET_TYPE_COVER_CODE: TARGET_TYPE_COVER,
    TARGET_TYPE_COVER_AREA_CODE: TARGET_TYPE_COVER_AREA,
    TARGET_TYPE_COVER_BRIDGE_CODE: TARGET_TYPE_COVER_BRIDGE,
}

# Target priorities -----------------------------------------------------------
TARGET_PRIORITY_PRIMARY = 'primary'
TARGET_PRIORITY_SECONDARY = 'secondary'
TARGET_PRIORITY_HIDDEN = 'hidden'

TARGET_PRIORITIES = {
    TARGET_PRIORITY_PRIMARY: _("primary"),
    TARGET_PRIORITY_SECONDARY: _("secondary"),
    TARGET_PRIORITY_HIDDEN: _("hidden"),
}

TARGET_PRIORITIES_MAP = {
    '0': TARGET_PRIORITY_PRIMARY,
    '1': TARGET_PRIORITY_SECONDARY,
    '2': TARGET_PRIORITY_HIDDEN,
}

###############################################################################
# Flight_Way
###############################################################################

# Way points ----------------------------------------------------------------

WAY_POINT_TYPES = {
    'TAKEOFF': {
        'type': "takeoff_normal",
    },
    'TAKEOFF_002': {
        'type': "takeoff_pair",
    },
    'TAKEOFF_003': {
        'type': "takeoff_in_line",
    },
    'TAKEOFF_004': {
        'type': "taxiing",
    },
    'NORMFLY': {
        'type': 'normal',
    },
    'NORMFLY_401': {
        'type': 'patrol',
        'patrol_type': 'triangle',
    },
    'NORMFLY_402': {
        'type': 'patrol',
        'patrol_type': 'square',
    },
    'NORMFLY_403': {
        'type': 'patrol',
        'patrol_type': 'pentagon',
    },
    'NORMFLY_404': {
        'type': 'patrol',
        'patrol_type': 'hexagon',
    },
    'NORMFLY_405': {
        'type': 'patrol',
        'patrol_type': 'random',
    },
    'GATTACK': {
        'type': 'attack',
    },
    'LANDING': {
        'type': 'landing_on_left',
    },
    'LANDING_101': {
        'type': 'landing_on_right',
    },
    'LANDING_102': {
        'type': 'landing_short_on_left',
    },
    'LANDING_103': {
        'type': 'landing_short_on_right',
    },
    'LANDING_104': {
        'type': 'landing_straight',
    },
}

WAY_POINT_FORMATIONS = {
    'F1': 'echelon_right',
    'F2': 'echelon_left',
    'F3': 'rank',
    'F4': 'line_abreast',
    'F5': 'line_asteam',
    'F6': 'vic',
    'F7': 'finger_four',
    'F8': 'diamond',
}
