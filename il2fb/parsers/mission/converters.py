# coding: utf-8

import datetime
import math

from il2fb.commons import Skills, UnitTypes
from il2fb.commons.organization import AirForces, Belligerents

from .constants import NULL


def to_bool(value):
    """
    Converts a string representation of a number into boolean.

    :param str value: a string representation of a number to convert

    :returns: `False` if `value` is equal to `'0'`, `True` otherwise
    :rtype: :class:`bool`

    **Examples:**

    .. code-block:: python

       >>> to_bool('0')
       False
       >>> to_bool('1')
       True
       >>> to_bool('-1')
       True
    """
    return int(value) != 0


def to_belligerent(value):
    return Belligerents.get_by_value(int(value))


def to_skill(value):
    return Skills.get_by_value(int(value))


def to_unit_type(value):
    return UnitTypes.get_by_value(value.lower())


def to_air_force(value):
    if value == NULL:
        return AirForces.vvs_rkka
    elif value:
        return AirForces.get_by_value(value)


def to_time(value):
    time = float(value)
    minutes, hours = math.modf(time)
    return datetime.time(int(hours), int(minutes * 60))