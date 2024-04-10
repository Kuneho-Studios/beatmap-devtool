###
# Contains all the "art" for representing the different lane configurations that are currently supported.
###

TWO_LANES_RIGHT_LEFT = [
    ("""╔═══════════════════╗
║  1 ←---           ║
║  2 ←---           ║
║  x ----           ║
║  x ----           ║
║  x ----           ║
╚═══════════════════╝""", ["TwoLaneRL_0", "TwoLaneRL_1", "None", "None", "None"]),
    ("""╔═══════════════════╗
║  x ----           ║
║  1 ←---           ║
║  2 ←---           ║
║  x ----           ║
║  x ----           ║
╚═══════════════════╝""", ["None", "TwoLaneRL_0", "TwoLaneRL_1", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  x ----           ║
    ╚═══════════════════╝
    """, ["None", "None", "TwoLaneRL_0", "TwoLaneRL_1", "None"]),
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  x ----           ║
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ╚═══════════════════╝
    """, ["None", "None", "None", "TwoLaneRL_0", "TwoLaneRL_1", ])
]

TWO_LANES_LEFT_RIGHT = [
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["TwoLaneLR_0", "TwoLaneLR_1", "None", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["None", "TwoLaneLR_0", "TwoLaneLR_1", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["None", "None", "TwoLaneLR_0", "TwoLaneLR_1", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ╚═══════════════════╝
    """, ["None", "None", "None", "TwoLaneLR_0", "TwoLaneLR_1"])
]

FOUR_LANES_TOP_BOTTOM = [
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   |  ↓  ↓  ↓  ↓   ║
    ║   x  1  2  3  4   ║
    ╚═══════════════════╝
    """, ["None", "FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3"]),
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   ↓  |  ↓  ↓  ↓   ║
    ║   1  x  2  3  4   ║
    ╚═══════════════════╝
    """, ["FourLaneTB_0", "None", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3"]),
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   ↓  ↓  |  ↓  ↓   ║
    ║   1  2  x  3  4   ║
    ╚═══════════════════╝
    """, ["FourLaneTB_0", "FourLaneTB_1", "None", "FourLaneTB_2", "FourLaneTB_3"]),
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   ↓  ↓  ↓  |  ↓   ║
    ║   1  2  3  x  4   ║
    ╚═══════════════════╝
    """, ["FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "None", "FourLaneTB_3"]),
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   ↓  ↓  ↓  ↓  |   ║
    ║   1  2  3  4  x   ║
    ╚═══════════════════╝
    """, ["FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3", "None"])
]

FOUR_LANES_BOTTOM_TOP = [
    ("""
    ╔═══════════════════╗
    ║   x  1  2  3  4   ║
    ║   |  ↑  ↑  ↑  ↑   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["None", "FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3"]),
    ("""
    ╔═══════════════════╗
    ║   1  x  2  3  4   ║
    ║   ↑  |  ↑  ↑  ↑   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["FourLaneBT_0", "None", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3"]),
    ("""
    ╔═══════════════════╗
    ║   1  2  x  3  4   ║
    ║   ↑  ↑  |  ↑  ↑   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["FourLaneBT_0", "FourLaneBT_1", "None", "FourLaneBT_2", "FourLaneBT_3"]),
    ("""
    ╔═══════════════════╗
    ║   1  2  3  x  4   ║
    ║   ↑  ↑  ↑  |  ↑   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "None", "FourLaneBT_3"]),
    ("""
    ╔═══════════════════╗
    ║   1  2  3  4  x   ║
    ║   ↑  ↑  ↑  ↑  |   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3", "None"])
]

FOUR_LANES_CORNERS = [
    ("""
    ╔═══════════════════╗
    ║  1             4  ║
    ║   ↖           ↗   ║
    ║     >       <     ║
    ║   ↙           ↘   ║
    ║  2             3  ║
    ╚═══════════════════╝
    """, ["CornersTL", "CornersBL", "None", "CornersBR", "CornersTR"])
]

FOUR_LANES_LEFT_RIGHT = [
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---→ 3  ║
    ║           ---→ 4  ║
    ╚═══════════════════╝
    """, ["None", "FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3"]),
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---- x  ║
    ║           ---→ 2  ║
    ║           ---→ 3  ║
    ║           ---→ 4  ║
    ╚═══════════════════╝
    """, ["FourLaneLR_0", "None", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3"]),
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ║           ---→ 3  ║
    ║           ---→ 4  ║
    ╚═══════════════════╝
    """, ["FourLaneLR_0", "FourLaneLR_1", "None", "FourLaneLR_2", "FourLaneLR_3"]),
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---→ 3  ║
    ║           ---- x  ║
    ║           ---→ 4  ║
    ╚═══════════════════╝
    """, ["FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "None", "FourLaneLR_3"]),
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---→ 3  ║
    ║           ---→ 4  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3", "None"])
]

FOUR_LANES_RIGHT_LEFT = [
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  3 ←---           ║
    ║  4 ←---           ║
    ╚═══════════════════╝
    """, ["None", "FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3"]),
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  x ----           ║
    ║  2 ←---           ║
    ║  3 ←---           ║
    ║  4 ←---           ║
    ╚═══════════════════╝
    """, ["FourLaneRL_0", "None", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3"]),
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  x ----           ║
    ║  3 ←---           ║
    ║  4 ←---           ║
    ╚═══════════════════╝
    """, ["FourLaneRL_0", "FourLaneRL_1", "None", "FourLaneRL_2", "FourLaneRL_3"]),
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  3 ←---           ║
    ║  x ----           ║
    ║  4 ←---           ║
    ╚═══════════════════╝
    """, ["FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "None", "FourLaneRL_3"]),
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  3 ←---           ║
    ║  4 ←---           ║
    ║  x ----           ║
    ╚═══════════════════╝
    """, ["FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3", "None"])
]

FIVE_LANES_TOP_BOTTOM = [
    ("""
    ╔═══════════════════╗
    ║                   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║   ↓  ↓  ↓  ↓  ↓   ║
    ║   1  2  3  4  5   ║
    ╚═══════════════════╝
    """, ["FiveLaneTB_0", "FiveLaneTB_1", "FiveLaneTB_2", "FiveLaneTB_3", "FiveLaneTB_4"])
]

FIVE_LANES_BOTTOM_TOP = [
    ("""
    ╔═══════════════════╗
    ║   1  2  3  4  x   ║
    ║   ↑  ↑  ↑  ↑  |   ║
    ║   |  |  |  |  |   ║
    ║   |  |  |  |  |   ║
    ║                   ║
    ╚═══════════════════╝
    """, ["FiveLaneBT_0", "FiveLaneBT_1", "FiveLaneBT_2", "FiveLaneBT_3", "FiveLaneBT_4"])

]

FIVE_LANES_RIGHT_LEFT = [
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  3 ←---           ║
    ║  4 ←---           ║
    ║  5 ←---           ║
    ╚═══════════════════╝
    """, ["FiveLaneRL_0", "FiveLaneRL_1", "FiveLaneRL_2", "FiveLaneRL_3", "FiveLaneRL_4"])
]

FIVE_LANES_LEFT_RIGHT = [
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---→ 3  ║
    ║           ---→ 4  ║
    ║           ---→ 5  ║
    ╚═══════════════════╝
    """, ["FiveLaneLR_0", "FiveLaneLR_1", "FiveLaneLR_2", "FiveLaneLR_3", "FiveLaneLR_4"])
]

FIVE_LANES_CORNER_MIDDLE_TOP_BOTTOM = [
    ("""
    ╔═══════════════════╗
    ║  1             4  ║
    ║   ↖     |     ↗   ║
    ║     >   |   <     ║
    ║   ↙     ↓     ↘   ║
    ║  2      5      3  ║
    ╚═══════════════════╝
    """, ["CornersTL", "CornersBL", "FiveLaneTB_2", "CornersBR", "CornersTR"])
]

FIVE_LANES_CORNER_MIDDLE_BOTTOM_TOP = [
    ("""
    ╔═══════════════════╗
    ║  1      5      4  ║
    ║   ↖     ↑     ↗   ║
    ║     >   |   <     ║
    ║   ↙     |     ↘   ║
    ║  2             3  ║
    ╚═══════════════════╝
    """, ["CornersTL", "CornersBL", "FiveLaneBT_2", "CornersBR", "CornersTR"])
]
