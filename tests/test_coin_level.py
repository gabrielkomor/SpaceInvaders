import pytest
from unittest.mock import Mock


def test_tick_coin(mock_coin, monkeypatch, mock_image):
    monkeypatch.setattr('src.settings_class.Settings.player_cash', 100)
    mock_coin.tick()
    assert mock_coin.text == mock_image


def test_draw_coin(mock_coin):
    window = Mock()
    mock_coin.draw(window)
    assert window.blit.call_count == 2
    calls = window.blit.call_args_list

    first_args = calls[0][0]
    assert first_args[0] == mock_coin.image
    assert first_args[1] == (mock_coin.x_cord, mock_coin.y_cord)

    second_args = calls[1][0]
    assert second_args[0] == mock_coin.text
    assert second_args[1] == (mock_coin.x_cord + mock_coin.width, mock_coin.y_cord + 7)


def test_tick_icon(mock_icon, monkeypatch, mock_image):
    monkeypatch.setattr('src.settings_class.Settings.game_level', 10)
    mock_icon.tick()
    assert mock_icon.text == mock_image
