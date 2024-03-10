from .enums import GreggorTypes

level_icons = {
    0: [GreggorTypes.NORMAL],
    1: [GreggorTypes.NORMAL, GreggorTypes.SAD],
    2: [GreggorTypes.NORMAL, GreggorTypes.SAD, GreggorTypes.SLEEPY],
    3: [GreggorTypes.NORMAL, GreggorTypes.SAD, GreggorTypes.SLEEPY, GreggorTypes.PARTY],
    4: [GreggorTypes.NORMAL, GreggorTypes.SAD, GreggorTypes.SLEEPY, GreggorTypes.PARTY, GreggorTypes.DISTRAUGHT],
    5: [GreggorTypes.NORMAL, GreggorTypes.SAD, GreggorTypes.SLEEPY, GreggorTypes.PARTY, GreggorTypes.DISTRAUGHT, GreggorTypes.CUPID],
    6: [GreggorTypes.NORMAL, GreggorTypes.SAD, GreggorTypes.SLEEPY, GreggorTypes.PARTY, GreggorTypes.DISTRAUGHT, GreggorTypes.CUPID, GreggorTypes.GRAD],
}