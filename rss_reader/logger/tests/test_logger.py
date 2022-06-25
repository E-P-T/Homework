

def test_stream_config():
    sc = StreamHandlerConfig()
    logger = sc.set_config('name')
    assert isinstance(sc, Logger)
