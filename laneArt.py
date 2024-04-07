two_lanes_left_right = [
    ("""
    ╔═══════════════════╗
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  x ----           ║
    ║  x ----           ║
    ║  x ----           ║
    ╚═══════════════════╝
    """, ["TwoLaneLR_0", "TwoLaneLR_1", "None", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  x ----           ║
    ║  x ----           ║
    ╚═══════════════════╝
    """, ["None", "TwoLaneLR_0", "TwoLaneLR_1", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ║  x ----           ║
    ╚═══════════════════╝
    """, ["None", "None", "TwoLaneLR_0", "TwoLaneLR_1", "None"]),
    ("""
    ╔═══════════════════╗
    ║  x ----           ║
    ║  x ----           ║
    ║  x ----           ║
    ║  1 ←---           ║
    ║  2 ←---           ║
    ╚═══════════════════╝
    """, ["None", "None", "None", "TwoLaneLR_0", "TwoLaneLR_1", ])
]

two_lanes_right_left = [
    ("""
    ╔═══════════════════╗
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["TwoLaneRL_0", "TwoLaneRL_1", "None", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["None", "TwoLaneRL_0", "TwoLaneRL_1", "None", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ║           ---- x  ║
    ╚═══════════════════╝
    """, ["None", "None", "TwoLaneRL_0", "TwoLaneRL_1", "None"]),
    ("""
    ╔═══════════════════╗
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---- x  ║
    ║           ---→ 1  ║
    ║           ---→ 2  ║
    ╚═══════════════════╝
    """, ["None", "None", "None", "TwoLaneRL_0", "TwoLaneRL_1"])
]

four_lanes_top_bottom = [
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

four_lanes_bottom_top = [
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

four_lanes_corners = [
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

four_lanes_left_right = [
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

four_lanes_right_left = [
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

five_lanes_top_bottom = [
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

five_lanes_bottom_top = [
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

five_lanes_right_left = [
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

five_lanes_left_right = [
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

five_lanes_corner_middle_top_bottom = [
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

five_lanes_corner_middle_bottom_top = [
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
