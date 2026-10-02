import pytest

from atis_parser import parse_atis


@pytest.mark.parametrize('text, expected', [
    ('EGLL AUTO 04008KT 9999 NCD 16/06 Q1019', 10000 / 1609.344),
    ('EGLL 021250Z 04008KT 7000 -RA BKN010 16/06 Q1019', 7000 / 1609.344),
    ('EGLL 04008KT 010V080 0800 FG VV002', 800 / 1609.344),
    ('EGLL 00000KT 0000 FG VV000', 0),
    ('EGLL 04008KT CAVOK 16/06 Q1019', 10000 / 1609.344),
    ('ENGM VIS 10KM', 10000 / 1609.344),
    ('ENGM VIS 2300M', 2300 / 1609.344),
    ('KSFO 28012KT 1/2SM FG', 0.5),
    ('KSFO 28012KT 1 1/2SM BR', 1.5),
    ('KSFO 28012KT 0SM FG', 0),
    ('KSFO 28012KT M1/4SM FG', 0.25),
])
def test_visibility_units_and_precision(text, expected):
    assert parse_atis(text).visibility == pytest.approx(expected)


@pytest.mark.parametrize('text', [
    '', 'VIS UNKNOWN', 'ATIS INFO A 1234Z Q1019',
    'EGLL 04008KT NCD 16/06 Q1019 R27L/0800',
    'EGLL 04008KT NCD RMK VIS 1SM',
    'EGLL 04008KT NCD TEMPO 04008KT 0800 FG',
    'KSFO 28012KT 1/0SM',
])
def test_unknown_visibility_is_null(text):
    result = parse_atis(text)
    assert result.visibility is None
    assert result.to_dict()['visibility'] is None
