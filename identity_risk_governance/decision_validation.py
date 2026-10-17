"""Validation for proposed access-review decisions.

This module validates decision input only; it never changes access.
"""

VALID_DECISIONS = ("manter", "investigar", "revogar")


def validate_review_decision(
    decision: str,
    approver_id: str | None = None,
) -> None:
    """Raise ValueError if a decision is unknown or lacks required approval data."""
    if decision not in VALID_DECISIONS:
        raise ValueError("Decisão inválida. Use manter, investigar ou revogar.")

    if decision == "revogar" and (
        not isinstance(approver_id, str) or not approver_id.strip()
    ):
        raise ValueError("A decisão revogar exige a identificação do aprovador humano.")
