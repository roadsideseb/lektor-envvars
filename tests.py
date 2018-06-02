from lektor_envvars import LektorEnv


def test_initialize_without_config():
    assert LektorEnv().prefix == "LEKTOR_"


def test_initialize_with_config():
    config = {"envvar.prefix": "NOT_THE_DEFAULT_"}
    assert LektorEnv(config).prefix == "NOT_THE_DEFAULT_"


def test_getting_envvar_bool(monkeypatch):
    env = LektorEnv()

    monkeypatch.setenv("LEKTOR_IS_BOOL", "true")
    assert env.envvars("IS_BOOL") == "true"
    assert env.envvars("IS_BOOL", "bool") is True

    monkeypatch.setenv("LEKTOR_IS_BOOL", "false")
    assert env.envvars("IS_BOOL") == "false"
    assert env.envvars("IS_BOOL", "bool") is False


def test_getting_envvar_int(monkeypatch):
    env = LektorEnv()

    monkeypatch.setenv("LEKTOR_INTEGER", "234")
    assert env.envvars("INTEGER") == "234"
    assert env.envvars("INTEGER", "int") == 234


def test_getting_envvar_without_prefix(monkeypatch):
    env = LektorEnv()

    monkeypatch.setenv("INTEGER", "234")
    assert env.envvars("INTEGER", no_prefix=True) == "234"
    assert env.envvars("INTEGER", "int", no_prefix=True) == 234
