"""Validation for proposed access-review decisions.

This module validates decision input only; it never changes access.
"""

VALID_DECISIONS = ("manter", "investigar", "revogar")


def validate_review_decision(
    decision: str,
    approver_id: str | None = None,
) -> None:
    """Validate decision input; raise ValueError for invalid or incomplete data.

    For ``revogar``, checks only that an approver ID is non-empty; it does not
    authenticate or authorize the approver or change access.
    """
    if decision not in VALID_DECISIONS:
        raise ValueError("Decisão inválida. Use manter, investigar ou revogar.")

    if decision == "revogar" and (
        not isinstance(approver_id, str) or not approver_id.strip()
    ):
        raise ValueError("A decisão revogar exige a identificação do aprovador humano.")
