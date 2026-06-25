"""Core business logic for the CSV budget CLI app."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def add_transaction(
    transactions: list[dict[str, Any]],
    transaction: dict[str, Any],
) -> list[dict[str, Any]]:
    """Add a transaction to the transaction list and return the updated list."""
    pass


def get_balance(transactions: list[dict[str, Any]]) -> float:
    """Return the net balance from the transaction list."""
    pass


def filter_by_category(
    transactions: list[dict[str, Any]],
    category: str,
) -> list[dict[str, Any]]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(file_path: Path) -> list[dict[str, Any]]:
    """Load transactions from a CSV file and return them as dictionaries."""
    pass


def monthly_summary(transactions: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    """Return monthly income, expense, and net totals."""
    pass
