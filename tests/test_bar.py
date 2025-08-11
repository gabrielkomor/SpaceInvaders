import pytest
from unittest.mock import Mock


@pytest.mark.parametrize('tick_val, player_reload, result', [(4, 2, 2), (1, 1, 1), (5, 2, 2.5), (3, 6, 0.5)])
def test_tick(monkeypatch, mock_loading_bar, tick_val, player_reload, result):
    monkeypatch.setattr('src.settings_class.Settings.player_reload_time', player_reload)
    mock_loading_bar.tick(tick_val)
    assert mock_loading_bar.loading == result


def test_tick_divide_by_zero(monkeypatch, mock_loading_bar):
    monkeypatch.setattr('src.settings_class.Settings.player_reload_time', 0)
    with pytest.raises(ZeroDivisionError):
        mock_loading_bar.tick(5)


@pytest.mark.parametrize('loading, tick_val, result', [(1, 2, 3), (2.3, 1, 3)])
def test_tick_chose(monkeypatch, mock_loading_bar, loading, tick_val, result):
    monkeypatch.setattr('src.settings_class.Settings.player_reload_time', 1)
    mock_loading_bar.loading = loading
    mock_loading_bar.tick(tick_val)
    assert mock_loading_bar.chose_image == result


@pytest.mark.parametrize('number, result', [(1, 1), (2, 2), (3, 3)])
def test_draw_blit_success(mock_loading_bar, number, result):
    window = Mock()
    mock_loading_bar.chose_image = number
    mock_loading_bar.draw(window)
    assert window.blit.call_count == 1
    args, kwargs = window.blit.call_args
    assert args[0] == mock_loading_bar.image[result]
    assert args[1] == (mock_loading_bar.x_cord, mock_loading_bar.y_cord)


def test_draw_blit_exception(mock_loading_bar):
    window = Mock()
    window.blit.side_effect = [Exception('fail'), None]
    mock_loading_bar.chose_image = 2
    mock_loading_bar.draw(window)
    assert window.blit.call_count == 2
    args, kwargs = window.blit.call_args
    assert args[0] == mock_loading_bar.image[0]
    assert args[1] == (mock_loading_bar.x_cord, mock_loading_bar.y_cord)
