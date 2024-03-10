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
    0: "story 0: Greggor starts as an innocent penguin, ready to start the journey through life. He's ready with his bow tie, however, he can't do it alone. Give him a helping hand by being productive and working towards your tasks.",
    1: "story 1: Greggor has made it to the first hurdle of life. He is struggling with his university work and is feeling overwhelmed. Keep staying productive so he can complete his work in time and make it to the next level.",
    2: "story 2: Greggor is a little sad. He is struggling to make friends and feels a little lonely. Keep staying productive so he can find friends to have fun with.",
    3: "story 3: Greggor has become a true university student and must take a nap every day to recharge. He's worked out a great routine where he can have a little rest each afternoon. Zzzzzzzz",
    4: "story 4: Greggor has made it to his 21st birthday! Whoooooop Whoooooooop! He's very excited and is having the birthday party of his dreams.",
    5: "story 5: Awww Greggor has fallen in love. He's found a cute penguin that he loves very much. Help him ask them out by completing your tasks.",
    6: "story 6: Greggor's made it! He's finally graduated! He thanks you so much for your help and is so overjoyed he's managed to get through his degree.",
}