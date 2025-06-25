import pytest
from unittest.mock import Mock
import scripts.bar_class as bar
import scripts.bullet_class as bullet_class


@pytest.fixture
def mock_loading_bar(monkeypatch, mock_image):
    monkeypatch.setattr('pygame.image.load', lambda path: mock_image)
    return bar.LoadingBar()


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
