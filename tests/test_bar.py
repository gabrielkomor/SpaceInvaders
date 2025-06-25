import pytest
from unittest.mock import Mock
import scripts.bar_class as bar


@pytest.fixture
def loading_bar(monkeypatch):
    monkeypatch.setattr('pygame.image.load', lambda path: path)
    return bar.LoadingBar()


@pytest.mark.parametrize('tick_val, player_reload, result', [(4, 2, 2), (1, 1, 1), (5, 2, 2.5), (3, 6, 0.5)])
def test_tick(monkeypatch, loading_bar, tick_val, player_reload, result):
    monkeypatch.setattr('scripts.settings_class.Settings.player_reload_time', player_reload)
    loading_bar.tick(tick_val)
    assert loading_bar.loading == result


def test_tick_divide_by_zero(monkeypatch, loading_bar):
    monkeypatch.setattr('scripts.settings_class.Settings.player_reload_time', 0)
    with pytest.raises(ZeroDivisionError):
        loading_bar.tick(5)


@pytest.mark.parametrize('loading, tick_val, result', [(1, 2, 3), (2.3, 1, 3)])
def test_tick_chose(monkeypatch, loading_bar, loading, tick_val, result):
    monkeypatch.setattr('scripts.settings_class.Settings.player_reload_time', 1)
    loading_bar.loading = loading
    loading_bar.tick(tick_val)
    assert loading_bar.chose_image == result


@pytest.mark.parametrize('number, result', [(1, 1), (2, 2), (3, 3)])
def test_draw_blit_success(loading_bar, number, result):
    window = Mock()
    loading_bar.chose_image = number
    loading_bar.draw(window)
    assert window.blit.call_count == 1
    args, kwargs = window.blit.call_args
    assert args[0] == loading_bar.image[result]
    assert args[1] == (loading_bar.x_cord, loading_bar.y_cord)


def test_draw_blit_exception(loading_bar):
    window = Mock()
    window.blit.side_effect = [Exception('fail'), None]
    loading_bar.chose_image = 2
    loading_bar.draw(window)
    assert window.blit.call_count == 2
    args, kwargs = window.blit.call_args
    assert args[0] == loading_bar.image[0]
    assert args[1] == (loading_bar.x_cord, loading_bar.y_cord)
