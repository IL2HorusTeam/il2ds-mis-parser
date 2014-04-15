# -*- coding: utf-8 -*-
"""
Different constants.
"""
from candv import Constants, SimpleConstant, ValueConstant, Values

from il2ds_mis_parser.helpers import _


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

ARMIES_NAMES = {
    ARMY_NONE: _("none"),
    ARMY_RED: _("red"),
    ARMY_BLUE: _("blue"),
}

ARMIES_MAP = {
    '0': ARMY_NONE,
    '1': ARMY_RED,
    '2': ARMY_BLUE,
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
TARGET_TYPE_DESTROY_BRIDGE_CODE = '1'
TARGET_TYPE_DESTROY_AREA_CODE = '2'
TARGET_TYPE_RECON_CODE = '3'
TARGET_TYPE_ESCORT_CODE = '4'
TARGET_TYPE_COVER_CODE = '5'
TARGET_TYPE_COVER_AREA_CODE = '6'
TARGET_TYPE_COVER_BRIDGE_CODE = '7'

TARGET_TYPE_DESTROY = 'destroy'
TARGET_TYPE_DESTROY_BRIDGE = 'destroy_bridge'
TARGET_TYPE_DESTROY_AREA = 'destroy_area'
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
# Weather
###############################################################################

# Weather types ---------------------------------------------------------------
WEATHER_CLEAR = 'clear'
WEATHER_GOOD = 'good'
WEATHER_HAZY = 'hazy'
WEATHER_POOR = 'poor'
WEATHER_BLIND = 'blind'
WEATHER_RAIN_OR_SNOW = 'rain_or_snow'
WEATHER_THUNDERSTORM = 'thunderstorm'

WEATHER_TYPES_NAMES = {
    WEATHER_CLEAR: _("clear"),
    WEATHER_GOOD: _("good"),
    WEATHER_HAZY: _("hazy"),
    WEATHER_POOR: _("poor"),
    WEATHER_BLIND: _("blind"),
    WEATHER_RAIN_OR_SNOW: _("rain or snow"),
    WEATHER_THUNDERSTORM: _("thunderstorm"),
}

WEATHER_TYPES_MAP = {
    '0': WEATHER_CLEAR,
    '1': WEATHER_GOOD,
    '2': WEATHER_HAZY,
    '3': WEATHER_POOR,
    '4': WEATHER_BLIND,
    '5': WEATHER_RAIN_OR_SNOW,
    '6': WEATHER_THUNDERSTORM,
}

# Gust ------------------------------------------------------------------------
GUST_NONE = 'none'
GUST_LOW = 'low'
GUST_MODERATE = 'moderate'
GUST_STRONG = 'strong'

GUST_TYPES_NAMES = {
    GUST_NONE: _("none"),
    GUST_LOW: _("low"),
    GUST_MODERATE: _("moderate"),
    GUST_STRONG: _("strong"),
}

GUST_TYPES_MAP = {
    '0': GUST_NONE,
    '1': GUST_LOW,
    '2': GUST_MODERATE,
    '3': GUST_STRONG,
}

# Turbulence ------------------------------------------------------------------
TURBULENCE_NONE = 'none'
TURBULENCE_LOW = 'low'
TURBULENCE_MODERATE = 'moderate'
TURBULENCE_STRONG = 'strong'
TURBULENCE_VERY_STRONG = 'very_strong'

TURBULENCE_TYPES_NAMES = {
    TURBULENCE_NONE: _("none"),
    TURBULENCE_LOW: _("low"),
    TURBULENCE_MODERATE: _("moderate"),
    TURBULENCE_STRONG: _("strong"),
    TURBULENCE_VERY_STRONG: _("very strong"),
}

TURBULENCE_TYPES_MAP = {
    '0': TURBULENCE_NONE,
    '1': TURBULENCE_LOW,
    '2': TURBULENCE_MODERATE,
    '3': TURBULENCE_STRONG,
    '4': TURBULENCE_VERY_STRONG,
}

###############################################################################
# Flight_Way
###############################################################################

# Way points ----------------------------------------------------------------


class WayPointTypes(Constants):
    TAKEOFF = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('takeoff_normal'),
    )
    TAKEOFF_002 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('takeoff_pair'),
    )
    TAKEOFF_003 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('takeoff_in_line'),
    )
    TAKEOFF_004 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('taxiing'),
    )
    NORMFLY = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('normal'),
    )
    NORMFLY_401 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('patrol'),
        PATROL_TYPE=ValueConstant('triangle'),
    )
    NORMFLY_402 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('patrol'),
        PATROL_TYPE=ValueConstant('square'),
    )
    NORMFLY_403 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('patrol'),
        PATROL_TYPE=ValueConstant('pentagon'),
    )
    NORMFLY_404 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('patrol'),
        PATROL_TYPE=ValueConstant('hexagon'),
    )
    NORMFLY_405 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('patrol'),
        PATROL_TYPE=ValueConstant('random'),
    )
    NORMFLY_407 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('artillery_spotter'),
    )
    GATTACK = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('attack'),
    )
    LANDING = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('landing_on_left'),
    )
    LANDING_101 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('landing_on_right'),
    )
    LANDING_102 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('landing_short_on_left'),
    )
    LANDING_103 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('landing_short_on_right'),
    )
    LANDING_104 = SimpleConstant().to_group(
        Values,
        TYPE=ValueConstant('landing_straight'),
    )


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
