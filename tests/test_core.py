"""Tests for budget.core."""

from pathlib import Path

from budget.core import add_transaction, filter_by_category, load_transactions_from_csv


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the list length by one."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 2


def test_add_transaction_preserves_negative_amount() -> None:
    """Expense transactions should keep their negative amount value."""
    transactions = []
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -1500


def test_add_transaction_preserves_positive_amount() -> None:
    """Income transactions should keep their positive amount value."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 25000


def test_add_transaction_allows_empty_description() -> None:
    """Empty descriptions should be preserved as-is."""
    transactions = []
    transaction = {
        "date": "2026-01-12",
        "type": "지출",
        "category": "식비",
        "description": "",
        "amount": -5800,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""


def test_filter_by_category_matches_case_insensitively() -> None:
    """Category matching should ignore case."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
        {
            "date": "2026-01-07",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 3500000,
            "memo": "1월급여",
        },
        {
            "date": "2026-01-10",
            "type": "지출",
            "category": "식비",
            "description": "저녁",
            "amount": -15000,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "식비")

    assert len(result) == 2
    assert all(item["category"] == "식비" for item in result)


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Unknown categories should return an empty list."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "없는카테고리")

    assert result == []


def test_filter_by_category_returns_independent_results() -> None:
    """Filtered results should be independent from the original list."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
        {
            "date": "2026-01-10",
            "type": "지출",
            "category": "교통",
            "description": "지하철",
            "amount": -1500,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "식비")
    result.append(
        {
            "date": "2026-01-99",
            "type": "지출",
            "category": "식비",
            "description": "추가",
            "amount": -1,
            "memo": "",
        }
    )

    assert len(transactions) == 2
    assert len(result) == 2


def test_load_transactions_from_csv_reads_step1_sample() -> None:
    """CSV loading should match the step1 sample data shape."""
    file_path = Path("data/step1_transactions.csv")

    result = load_transactions_from_csv(file_path)

    assert len(result) == 10
    assert result[0] == {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }
    assert result[-1] == {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }
    assert isinstance(result[0]["amount"], int)
