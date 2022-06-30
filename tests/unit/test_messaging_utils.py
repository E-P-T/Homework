from rss_parse.utils.messaging_utils import print_error


def test_print_error_stdout_empty(capfd):
    print_error("Not stdout")
    out, err = capfd.readouterr()
    assert not out


def test_print_error_stderr_not_empty(capfd):
    print_error("Definitely stderr")
    out, err = capfd.readouterr()
    assert err == "Definitely stderr\n"
