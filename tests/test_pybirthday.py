import pytest
from src.pybirthday.pybirthday import cake, candle, balloon

class Tests:

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    # Test for Candles
    def test_specific_candle(self):
        """
        Test if calling 'candle(n)' returns the correct candle at index 'n'.
        """
        # Check first candle
        first_candle = candle(0)
        expected_candle = "\n".join([
            "   (  ",
            "  ) ) ",
            " ( (  ",
            "  ) ) ",
            "   V  ",
            "   |  ",
            " .-+-.",
            " |   |",
            " '---'"
        ])
        assert first_candle == expected_candle, f"Expected first candle, but got:\n{first_candle}"

    def test_out_of_range(self):
        """
        Test if calling 'candle(n)' with 'n' greater than the available styles returns the last candle.
        """
        last_candle = candle(100)
        expected_last_candle = "\n".join([
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
        ])
        assert last_candle == expected_last_candle, f"Expected last candle, but got:\n{last_candle}"
        
    def test_random_candle(self):
        """
        Test if calling 'candle()' without arguments returns a valid candle from the list.
        """
        result = candle().split("\n")
        # Define possible candle options
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
        assert any(result == candle for candle in candle_styles)


    #Test for balloons
    def test_specific_balloon(self):
        """
        Test if calling 'balloon(n)' returns the correct balloon at index 'n'.
        """
        first_balloon = balloon(0)
        expected_balloon = "\n".join([
            "                          __",
            "                        ,\"  \".",
            "     _      .---.    _ /#     \\",
            "   ,' `.  ,'     `.." ".      ,--.",
            "   |#   `/ #      (#    )    /    )",
            "    `.   |         )   (`.__/    /",
            "      `. \\        (     )/'/    /",
            "        `.\\       /)   (( /    /",
            "           `.   .'(     )y    /",
            "             >_<\\  `._.'(    /",
            "             /   ) /'-`.->,-'",
            "            (   ( (   (",
            "             )     )   )",
            "                  ("
        ])
        assert first_balloon == expected_balloon, f"Expected first balloon, but got:\n{first_ballon}"

    def test_random_balloon(self):
        """
        Test if calling 'balloon()' without arguments returns a valid balloon from the list.
        """
        result = balloon().split("\n")
        # Define possible balloon styles
        balloon_styles = [
            [
                "                          __",
                "                        ,\"  \".",
                "     _      .---.    _ /#     \\",
                "   ,' `.  ,'     `.." ".      ,--.",
                "   |#   `/ #      (#    )    /    )",
                "    `.   |         )   (`.__/    /",
                "      `. \\        (     )/'/    /",
                "        `.\\       /)   (( /    /",
                "           `.   .'(     )y    /",
                "             >_<\\  `._.'(    /",
                "             /   ) /'-`.->,-'",
                "            (   ( (   (",
                "             )     )   )",
                "                  ("
            ],
            [
                "     ,-''''-.",
                "   ,'      _ `.",
                "  /       )_)  \\",
                " :              :",
                " \\              /",
                "  \\            /",
                "   `.        ,'",
                "     `.    ,'",
                "       `.,'",
                "        /\\`.   ,-._",
                "            `-'"
            ],
            [
                "     ######",
                "   ##########",
                "  ######    _\\_",
                "  ##===----[.].]",
                "  #(     ,   _\\",
                "   #      )\\__|",
                "    \\        /",
                "     `-._``-'",
                "        >@",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |",
                "         |"
            ],
            [
                "     .;;;;;;       ;;;;;;,.",
                "   .;;;;;;;;;     ;;;;;;;;;;,",
                " .;;;;;;;;;;;;   ;;;;;;;;;;;;;.",
                " ;;;;;@;;;;;;;; ;;;;;;;;;;;;;;;'",
                " ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'",
                " ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'",
                " `;;;;@;;;;;;;;;;;;;;;@;;;;;;;'",
                "  `;;;;;;;;;;;;;;;;;;;@@;;;;;'",
                "    `;;;;;;;;;;;;;;;;@@;;;;'",
                "      `;;;;;;;;;;;;;@;;;;'",
                "         `;;;;;;;;;;;;'",
                "            `;;;;;;'",
                "               ;;",
                "               `",
                "              `",
                "             `",
                "            `",
                "           `",
                "          `",
                "         `",
                "         `",
                "         `",
                "          `",
                "            `.",
            ]
        ]
        assert any(result == balloon for balloon in balloon_styles)