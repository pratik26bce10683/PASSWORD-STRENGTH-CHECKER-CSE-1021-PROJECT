from src.password_checker import analyze_password
from src.password_generator import generate_password
from src.password_validator import validate_password


def test_strong_password():
    result = analyze_password("Abcd1234!")
    assert result["score"] == 5
    assert result["strength"] == "VERY STRONG"


def test_weak_password():
    result = analyze_password("abc")
    assert result["score"] < 3
    assert result["strength"] == "WEAK"


def test_password_generator():
    password = generate_password(12)

    assert len(password) == 12
    assert any(ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for ch in password)
    assert any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in password)
    assert any(ch in "0123456789" for ch in password)
    assert any(ch in "!@#$%^&*()_+" for ch in password)


def test_valid_password():
    assert validate_password("Abcd1234!") == True


def test_invalid_password():
    assert validate_password("abc") == False