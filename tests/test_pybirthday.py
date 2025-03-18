import pytest
from src.pybirthday.pybirthday import cake, candle

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