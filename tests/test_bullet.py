import pytest
from unittest.mock import Mock
import scripts.bullet_class as bullet_class


@pytest.fixture
def mock_player():
    player = Mock()
    player.x_cord = 100
    player.y_cord = 100
    player.width = 20
    player.height = 20
    return player


@pytest.fixture
def mock_image():
    image = Mock()
    image.convert_alpha.return_value = image
    image.get_width.return_value = 10
    image.get_height.return_value = 10
    return image


@pytest.fixture
def mock_bullet(monkeypatch, mock_player, mock_image):
    monkeypatch.setattr('pygame.image.load', lambda path: mock_image)
    return bullet_class.Bullet(mock_player)


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
    monkeypatch.setattr('scripts.settings_class.Settings.player_bullet_speed', value)
    bullets = [mock_bullet]
    entities = []
    entity_bullets = []
    explosions = []
    mock_bullet.tick(mock_bullet, bullets, entities, entity_bullets, explosions)
    assert mock_bullet.y_cord == result
    hit_box = mock_bullet.hit_box
    assert hit_box.x == x_cord
    assert hit_box.y == result
    assert hit_box.width == width
    assert hit_box.height == height

