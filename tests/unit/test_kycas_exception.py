"""Unit tests for the "Know Your Class and Section" fetch error exception."""

from app.exceptions.authentication import KYCASFetchError
from app.exceptions.base import PESUAcademyError


def test_kycas_fetch_error_default_message():
    """Test that the default message is set correctly."""
    error = KYCASFetchError()
    assert 'Failed to fetch "Know Your Class and Section" data from PESU Academy.' in str(error)


def test_kycas_fetch_error_custom_message():
    """Test that a custom message overrides the default."""
    error = KYCASFetchError('Custom "Know Your Class and Section" error message.')
    assert 'Custom "Know Your Class and Section" error message.' in str(error)


def test_kycas_fetch_error_status_code():
    """Test that the status code is 502."""
    error = KYCASFetchError()
    assert error.status_code == 502


def test_kycas_fetch_error_inherits_from_pesu_academy_error():
    """Test that the "Know Your Class and Section" fetch error subclasses PESUAcademyError."""
    assert issubclass(KYCASFetchError, PESUAcademyError)


def test_kycas_fetch_error_is_exception():
    """Test that the "Know Your Class and Section" fetch error can be raised and caught."""
    try:
        raise KYCASFetchError("test")
    except PESUAcademyError as e:
        assert "test" in str(e)
