"""Unit tests for the "Know Your Class and Section" Pydantic model."""

import pytest
from pydantic import ValidationError

from app.models.kycas import KYCASModel


def test_kycas_model_all_fields():
    """Test creating the "Know Your Class and Section" model with all fields populated."""
    data = {
        "prn": "PES1201800001",
        "srn": "PES1UG19CS001",
        "name": "John Doe",
        "semester": "Sem-6",
        "section": "Section A",
        "cycle": "NA",
        "department": "CSE(RR Campus)",
        "branch": "CSE",
        "institute_name": "PES University",
    }
    model = KYCASModel(**data)
    assert model.prn == "PES1201800001"
    assert model.srn == "PES1UG19CS001"
    assert model.name == "John Doe"
    assert model.semester == "Sem-6"
    assert model.section == "Section A"
    assert model.cycle == "NA"
    assert model.department == "CSE(RR Campus)"
    assert model.branch == "CSE"
    assert model.institute_name == "PES University"


def test_kycas_model_all_defaults():
    """Test that all fields default to None."""
    model = KYCASModel()
    assert model.prn is None
    assert model.srn is None
    assert model.name is None
    assert model.semester is None
    assert model.section is None
    assert model.cycle is None
    assert model.department is None
    assert model.branch is None
    assert model.institute_name is None


def test_kycas_model_partial_fields():
    """Test creating the "Know Your Class and Section" model with only some fields."""
    model = KYCASModel(prn="PES1201800001", name="Jane Doe")
    assert model.prn == "PES1201800001"
    assert model.name == "Jane Doe"
    assert model.srn is None
    assert model.semester is None


def test_kycas_model_strict_type_enforcement():
    """Test that strict mode rejects non-string types for string fields."""
    with pytest.raises(ValidationError) as exc_info:
        KYCASModel(prn=12345)
    assert "prn" in str(exc_info.value)


def test_kycas_model_serialization():
    """Test that model serializes to dict correctly."""
    data = {
        "prn": "PES1201800001",
        "srn": "PES1UG19CS001",
        "name": "John Doe",
        "semester": "Sem-6",
        "section": "Section A",
        "cycle": "NA",
        "department": "CSE(RR Campus)",
        "branch": "CSE",
        "institute_name": "PES University",
    }
    model = KYCASModel(**data)
    dumped = model.model_dump()
    assert dumped == data


def test_kycas_model_json_serialization():
    """Test that the model can be serialized to JSON."""
    model = KYCASModel(prn="PES1201800001", name="John Doe")
    json_str = model.model_dump_json()
    assert "PES1201800001" in json_str
    assert "John Doe" in json_str
