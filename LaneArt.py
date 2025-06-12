###
# Contains "art" representing the supported different lane configurations
###

TWO_LANES_RIGHT_LEFT = [
  ("\t╔═══════════════════╗\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t╚═══════════════════╝",
   ["TwoLaneRL_0", "TwoLaneRL_1", "None", "None", "None"]),
  ("\t╔═══════════════════╗\n" +
   "\t║  x ----           ║\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t╚═══════════════════╝",
   ["None", "TwoLaneRL_0", "TwoLaneRL_1", "None", "None"]),
  ("\t╔═══════════════════╗\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  x ----           ║\n" +
   "\t╚═══════════════════╝",
   ["None", "None", "TwoLaneRL_0", "TwoLaneRL_1", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║  x ----           ║\n" +
    "\t║  x ----           ║\n" +
    "\t║  x ----           ║\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "None", "TwoLaneRL_0", "TwoLaneRL_1", ])
]

TWO_LANES_LEFT_RIGHT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["TwoLaneLR_0", "TwoLaneLR_1", "None", "None", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "TwoLaneLR_0", "TwoLaneLR_1", "None", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "TwoLaneLR_0", "TwoLaneLR_1", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "None", "TwoLaneLR_0", "TwoLaneLR_1"])
]

THREE_LANES_RIGHT_LEFT = [
  ("\t╔═══════════════════╗\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  3 ←---           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t╚═══════════════════╝",
   ["ThreeLaneRL_0", "ThreeLaneRL_1", "ThreeLaneRL_2", "None", "None"]),
  ("\t╔═══════════════════╗\n" +
   "\t║  x ----           ║\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  3 ←---           ║\n" +
   "\t║  x ----           ║\n" +
   "\t╚═══════════════════╝",
   ["None", "ThreeLaneRL_0", "ThreeLaneRL_1", "ThreeLaneRL_2", "None"]),
  ("\t╔═══════════════════╗\n" +
   "\t║  x ----           ║\n" +
   "\t║  x ----           ║\n" +
   "\t║  1 ←---           ║\n" +
   "\t║  2 ←---           ║\n" +
   "\t║  3 ←---           ║\n" +
   "\t╚═══════════════════╝",
   ["None", "None", "ThreeLaneRL_0", "ThreeLaneRL_1", "ThreeLaneRL_2"])
]

THREE_LANES_LEFT_RIGHT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["ThreeLaneLR_0", "ThreeLaneLR_1", "ThreeLaneLR_2", "None", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "ThreeLaneLR_0", "ThreeLaneLR_1", "ThreeLaneLR_2", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "ThreeLaneLR_0", "ThreeLaneLR_1", "ThreeLaneLR_2"])
]

THREE_LANES_TOP_BOTTOM = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  ↓  ↓  |  |   ║\n" +
    "\t║   1  2  3  x  x   ║\n" +
    "\t╚═══════════════════╝",
    ["ThreeLaneTB_0", "ThreeLaneTB_1", "ThreeLaneTB_2", "None", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  ↓  ↓  ↓  |   ║\n" +
    "\t║   x  1  2  3  x   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "ThreeLaneTB_0", "ThreeLaneTB_1", "ThreeLaneTB_2", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  ↓  ↓  ↓   ║\n" +
    "\t║   x  x  1  2  3   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "ThreeLaneTB_0", "ThreeLaneTB_1", "ThreeLaneTB_2"])
]

THREE_LANES_BOTTOM_TOP = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  2  3  x  x   ║\n" +
    "\t║   ↑  ↑  ↑  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "ThreeLaneBT_0", "ThreeLaneBT_1", "ThreeLaneBT_2", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   x  1  2  3  x   ║\n" +
    "\t║   |  ↑  ↑  ↑  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "ThreeLaneBT_0", "ThreeLaneBT_1", "ThreeLaneBT_2", "None"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   x  x  1  2  3   ║\n" +
    "\t║   |  |  ↑  ↑  ↑   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "None", "ThreeLaneBT_0", "ThreeLaneBT_1", "ThreeLaneBT_2"])
]

FOUR_LANES_TOP_BOTTOM = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  ↓  ↓  ↓  ↓   ║\n" +
    "\t║   x  1  2  3  4   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  |  ↓  ↓  ↓   ║\n" +
    "\t║   1  x  2  3  4   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneTB_0", "None", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  ↓  |  ↓  ↓   ║\n" +
    "\t║   1  2  x  3  4   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneTB_0", "FourLaneTB_1", "None", "FourLaneTB_2", "FourLaneTB_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  ↓  ↓  |  ↓   ║\n" +
    "\t║   1  2  3  x  4   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "None", "FourLaneTB_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  ↓  ↓  ↓  |   ║\n" +
    "\t║   1  2  3  4  x   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneTB_0", "FourLaneTB_1", "FourLaneTB_2", "FourLaneTB_3", "None"])
]

FOUR_LANES_BOTTOM_TOP = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║   x  1  2  3  4   ║\n" +
    "\t║   |  ↑  ↑  ↑  ↑   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["None", "FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  x  2  3  4   ║\n" +
    "\t║   ↑  |  ↑  ↑  ↑   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneBT_0", "None", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  2  x  3  4   ║\n" +
    "\t║   ↑  ↑  |  ↑  ↑   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneBT_0", "FourLaneBT_1", "None", "FourLaneBT_2", "FourLaneBT_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  2  3  x  4   ║\n" +
    "\t║   ↑  ↑  ↑  |  ↑   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "None", "FourLaneBT_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  2  3  4  x   ║\n" +
    "\t║   ↑  ↑  ↑  ↑  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneBT_0", "FourLaneBT_1", "FourLaneBT_2", "FourLaneBT_3", "None"])
]

FOUR_LANES_CORNERS = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1             4  ║\n" +
    "\t║   ↖           ↗   ║\n" +
    "\t║     >       <     ║\n" +
    "\t║   ↙           ↘   ║\n" +
    "\t║  2             3  ║\n" +
    "\t╚═══════════════════╝",
    ["CornersTL", "CornersBL", "None", "CornersBR", "CornersTR"])
]

FOUR_LANES_LEFT_RIGHT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t╚═══════════════════╝",
    ["None", "FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneLR_0", "None", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneLR_0", "FourLaneLR_1", "None", "FourLaneLR_2", "FourLaneLR_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "None", "FourLaneLR_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t║           ---- x  ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneLR_0", "FourLaneLR_1", "FourLaneLR_2", "FourLaneLR_3", "None"])
]

FOUR_LANES_RIGHT_LEFT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║  x ----           ║\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["None", "FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  x ----           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneRL_0", "None", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  x ----           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneRL_0", "FourLaneRL_1", "None", "FourLaneRL_2", "FourLaneRL_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  x ----           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "None", "FourLaneRL_3"]),
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t║  x ----           ║\n" +
    "\t╚═══════════════════╝",
    ["FourLaneRL_0", "FourLaneRL_1", "FourLaneRL_2", "FourLaneRL_3", "None"])
]

FIVE_LANES_TOP_BOTTOM = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║                   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   ↓  ↓  ↓  ↓  ↓   ║\n" +
    "\t║   1  2  3  4  5   ║\n" +
    "\t╚═══════════════════╝",
    ["FiveLaneTB_0", "FiveLaneTB_1", "FiveLaneTB_2", "FiveLaneTB_3",
     "FiveLaneTB_4"])
]

FIVE_LANES_BOTTOM_TOP = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║   1  2  3  4  x   ║\n" +
    "\t║   ↑  ↑  ↑  ↑  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║   |  |  |  |  |   ║\n" +
    "\t║                   ║\n" +
    "\t╚═══════════════════╝",
    ["FiveLaneBT_0", "FiveLaneBT_1", "FiveLaneBT_2", "FiveLaneBT_3",
     "FiveLaneBT_4"])

]

FIVE_LANES_RIGHT_LEFT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1 ←---           ║\n" +
    "\t║  2 ←---           ║\n" +
    "\t║  3 ←---           ║\n" +
    "\t║  4 ←---           ║\n" +
    "\t║  5 ←---           ║\n" +
    "\t╚═══════════════════╝",
    ["FiveLaneRL_0", "FiveLaneRL_1", "FiveLaneRL_2", "FiveLaneRL_3",
     "FiveLaneRL_4"])
]

FIVE_LANES_LEFT_RIGHT = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║           ---→ 1  ║\n" +
    "\t║           ---→ 2  ║\n" +
    "\t║           ---→ 3  ║\n" +
    "\t║           ---→ 4  ║\n" +
    "\t║           ---→ 5  ║\n" +
    "\t╚═══════════════════╝",
    ["FiveLaneLR_0", "FiveLaneLR_1", "FiveLaneLR_2", "FiveLaneLR_3",
     "FiveLaneLR_4"])
]

FIVE_LANES_CORNER_MIDDLE_TOP_BOTTOM = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1             4  ║\n" +
    "\t║   ↖     |     ↗   ║\n" +
    "\t║     >   |   <     ║\n" +
    "\t║   ↙     ↓     ↘   ║\n" +
    "\t║  2      5      3  ║\n" +
    "\t╚═══════════════════╝",
    ["CornersTL", "CornersBL", "FiveLaneTB_2", "CornersBR", "CornersTR"])
]

FIVE_LANES_CORNER_MIDDLE_BOTTOM_TOP = [
  (
    "\t╔═══════════════════╗\n" +
    "\t║  1      5      4  ║\n" +
    "\t║   ↖     ↑     ↗   ║\n" +
    "\t║     >   |   <     ║\n" +
    "\t║   ↙     |     ↘   ║\n" +
    "\t║  2             3  ║\n" +
    "\t╚═══════════════════╝",
    ["CornersTL", "CornersBL", "FiveLaneBT_2", "CornersBR", "CornersTR"])
]
