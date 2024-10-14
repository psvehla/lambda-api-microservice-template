from app.service import service


def test_health_check():
    assert service.health_check() is True
