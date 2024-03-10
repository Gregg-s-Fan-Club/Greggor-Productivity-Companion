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

level_stories = {
    0: "story 0",
    1: "story 1",
    2: "story 2",
    3: "story 3",
    4: "story 4",
    5: "story 5",
    6: "story 6",
}