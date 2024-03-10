from django import template
from ..helpers import GreggorTypes
import os
import holidays
import datetime

register: template.Library = template.Library()


@register.filter
def get_greggor(greggor_type: str = "") -> str:
    """Returns the filepath for the wanted greggor logo"""
    base_path: str = os.path.join("images", "icons", "greggor-")
    greggor_type: str = greggor_type.lower()

    if len(greggor_type) != 0 and greggor_type in iter(GreggorTypes):
        return f"{base_path}{greggor_type}.png"

    if datetime.datetime.today().strftime(
            '%Y-%m-%d') in holidays.country_holidays('UK'):
        return f"{base_path}{GreggorTypes.PARTY}.png"

    if datetime.time(4, 0, 0) >= datetime.datetime.now().time(
    ) or datetime.datetime.now().time() >= datetime.time(22, 0, 0):
        return f"{base_path}{GreggorTypes.SLEEPY}.png"

    return f"{base_path}{GreggorTypes.NORMAL}.png"


@register.filter
def get_greggor_type_from_completeness(completeness: float) -> str:
    """Returns the desired type of greggor based on the level of completeness of a target"""
    if completeness >= 90:
        return GreggorTypes.PARTY
    elif completeness < 15:
        return GreggorTypes.DISTRAUGHT
    elif completeness < 35:
        return GreggorTypes.SAD
    else:
        return GreggorTypes.NORMAL
