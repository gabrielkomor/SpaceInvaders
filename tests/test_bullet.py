import pytest
from unittest.mock import Mock


def run_bullet_tick(mock_bullet):
    bullets = [mock_bullet]
    entities = []
    entity_bullets = []
    explosions = []
    mock_bullet.tick(mock_bullet, bullets, entities, entity_bullets, explosions)


def test_tick_remove_bullet(mock_bullet):
    bullets = [mock_bullet]
    entities = []
    entity_bullets = []
    explosions = []
    mock_bullet.y_cord = 0
    mock_bullet.tick(mock_bullet, bullets, entities, entity_bullets, explosions)
    assert mock_bullet not in bullets


@pytest.mark.parametrize('value, result', [(5, 95), (0, 100), (20, 80), (-5, 105)])
def test_tick_move_and_hit_box(monkeypatch, mock_bullet, value, result):
    x_cord, y_cord = mock_bullet.x_cord, mock_bullet.y_cord
    width, height = mock_bullet.width, mock_bullet.height
    monkeypatch.setattr('src.settings_class.Settings.player_bullet_speed', value)
    run_bullet_tick(mock_bullet)
    assert mock_bullet.y_cord == result
    hit_box = mock_bullet.hit_box
    assert hit_box.x == x_cord
    assert hit_box.y == result
    assert hit_box.width == width
    assert hit_box.height == height


def test_draw(mock_bullet):
    window = Mock()
    mock_bullet.draw(window)
    assert window.blit.call_count == 1
    args, kwargs = window.blit.call_args
    assert args[0] == mock_bullet.image
    assert args[1] == (mock_bullet.x_cord, mock_bullet.y_cord)
