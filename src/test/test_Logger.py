import io
from contextlib import redirect_stdout
from unittest import TestCase
from Logger import Logger, Level


class TestLogger(TestCase):
    def test_log(self):
        Logger.verbose(True)
        string = 'test'

        with io.StringIO() as buf1:
            with redirect_stdout(buf1):
                Logger.log(Level.INFO, string)
                Logger.log(Level.WARNING, string)
                self.assertRaises(SystemExit, Logger.log, Level.ERROR, string)
            for line in buf1.getvalue().strip().split('\n'):
                self.assertRegex(line, string)

        Logger.verbose(False)
        with io.StringIO() as buf2:
            with redirect_stdout(buf2):
                Logger.log(Level.INFO, string)
                Logger.log(Level.WARNING, string)
            self.assertEqual(len(buf2.getvalue()), 0)

        with io.StringIO() as buf3:
            with redirect_stdout(buf3):
                self.assertRaises(SystemExit, Logger.log, Level.ERROR, string)
            self.assertRegex(buf3.getvalue(), string)
