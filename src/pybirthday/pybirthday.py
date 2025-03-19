import random

def cake(name, words):
    return

def candle(n=None):
    """
    Generate an ASCII art of a candle.

    This function returns an ASCII art candle either randomly or based on a specified index.
    """
    candle_styles = [
        [
            "   (  ",
            "  ) ) ",
            " ( (  ",
            "  ) ) ",
            "   V  ",
            "   |  ",
            " .-+-.",
            " |   |",
            " '---'"
        ],
        [
            "        ,        ",
            "       ( \\       ",
            "        ) \\      ",
            "       ((\\ )     ",
            "      |`-;-._    ",
            "      |`-.   )   ",
            "      |   \\ (   ",
            "      |    \\ )   ",
            "      |    |/    ",
            "      |    `|    ",
            "      |     |    ",
            "      |     |    ",
            "      |     |    ",
            "      |     |    ",
            "      |_____|    ",
            "    _(_______)_  ",
            "   |           | ",
            "   |_____________|"
        ],
        [
            "              :              ",
            "      .       :       .      ",
            "       ::.   :::   .::       ",
            "          ::  :   ::         ",
            "           :  )  :           ",
            "      :::::  (_)  :::::      ",
            "         .: .-;_ :.          ",
            "       .:   |   \\  :.        ",
            "            |    )           ",
            "            |   |     __     ",
            "          . |   |   _) .(    ",
            "         _\\/|   | _) .'_|    ",
            "          -\\|   |) .'_(      ",
            "        ~>>8o<<-'8o-'  `     ",
            "         / /,\\-(  )``.,      ",
            "         | \\.'\\/  ) :(       ",
            "         \\   `'   `) (`      ",
            "          `._____.'`./       "
        ],
        [
            "                   . . ...                   ",
            "                .:::'.`:::::.                ",
            "               ::::::  '::::::               ",
            "              :::::: J6  ::::::              ",
            "              :::::  HMw  :::::              ",
            "              :::::  WNM  :::::              ",
            "              :::::: MAM ::::::              ",
            "               :::::.`;'.:::::               ",
            "                 ::Mmmmmmm;:                 ",
            "                   KKKRRMMA                  ",
            "                   KPPPP9NM                  ",
            "                   K7IIYINN                  ",
            "                   Klll1lNJ                  ",
            "                   Klll1lNR                  ",
            "                   Kl::1lJl                  ",
            "                   L:::1:J                   ",
            "                   L:::!:J                   ",
            "                   L:::::l                   ",
            "                   l:..::l       .           ",
            "             ,nnnnml:...:lmncJP',            ",
            "  :::::::;mCCCc'pdPl:...:l9bqPyj'jm;:::::::::::::::",
            "  ::::::OPCCcc.9b::;.....;::dP ,JCC9O::::::::::::::",
            "  ::::' 98CCccc.9MkmmnnnmmJMP.JacOB8P '::::::::::::",
            "  :::    `9qmCcccc\"\"YAAAY\"\"roseCmpP'    :::::::::::",
            "  :::.     ``9mm,...     ...,mmP''     .:::::::::::",
            "  :::::..       \"YTl995PPPT77\"      ..:::::::::::::",
            "  :::::::::...                 ...:::::::::::::::::",
            "  ::::::::::::::::.........::::::::::::::::::::::::"
        ],
        [
            "     ,?    ",
            "    ( :    ",
            "     ;)    ",
            "     |     ",
            "   ,-.-j   ",
            "  ;|   |   ",
            "  `|   |   ",
            "   |   `.  ",
            "   |,; |; ,-.",
            "   |U  | /();",
            " f`-^-^-',-' ",
            "  `-----'   "
        ]
    ]
    if n is None:
        style = random.choice(candle_styles)
    elif n > len(candle_styles) - 1:
        style = candle_styles[len(candle_styles) - 1]
    else:
        style = candle_styles[n]

    return "\n".join(style)