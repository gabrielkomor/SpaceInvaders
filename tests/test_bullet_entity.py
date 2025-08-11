import pytest
from unittest.mock import Mock


@pytest.mark.parametrize('counter, result, y_cord', [(2, 55, 55), (3, 45, 55), (7, 45, 55), (10, 55, 55)])
def test_tick(mock_bullet_entity, mock_player, counter, result, y_cord):
    entity_bullets = []
    explosions = []
    mock_bullet_entity.counter = counter
    mock_bullet_entity.x_cord = 50
    mock_bullet_entity.y_cord = 50
    mock_bullet_entity.speed = 5
    mock_bullet_entity.tick(mock_bullet_entity, entity_bullets, mock_player, explosions)
    assert mock_bullet_entity.x_cord == result
    assert mock_bullet_entity.y_cord == y_cord


def test_remove_entity(mock_bullet_entity, mock_player, monkeypatch):
    entity_bullets = [mock_bullet_entity]
    explosions = []
    mock_bullet_entity.y_cord = 200
    mock_bullet_entity.height = 10
    monkeypatch.setattr('src.settings_class.Settings.window_height', 250)
    mock_bullet_entity.tick(mock_bullet_entity, entity_bullets, mock_player, explosions)
    assert mock_bullet_entity not in entity_bullets


def test_draw(mock_bullet_entity):
    window = Mock()
    mock_bullet_entity.draw(window)
    assert window.blit.call_count == 1
    args, kwargs = window.blit.call_args
    assert args[0] == mock_bullet_entity.image
    assert args[1] == (mock_bullet_entity.x_cord, mock_bullet_entity.y_cord)
