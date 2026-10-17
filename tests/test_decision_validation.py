import unittest

from identity_risk_governance.decision_validation import validate_review_decision


class ValidateReviewDecisionTests(unittest.TestCase):
    def test_accepts_maintain_and_investigate_without_approver(self):
        for decision in ("manter", "investigar"):
            with self.subTest(decision=decision):
                self.assertIsNone(validate_review_decision(decision))

    def test_accepts_revoke_with_human_approver_identifier(self):
        self.assertIsNone(
            validate_review_decision("revogar", approver_id="aprovador-teste-01")
        )

    def test_rejects_revoke_without_approver_identifier(self):
        for approver_id in (None, "", "   "):
            with self.subTest(approver_id=approver_id):
                with self.assertRaisesRegex(ValueError, "identificação do aprovador"):
                    validate_review_decision("revogar", approver_id=approver_id)

    def test_rejects_unknown_or_empty_decision(self):
        for decision in ("aprovar", "", "   "):
            with self.subTest(decision=decision):
                with self.assertRaisesRegex(ValueError, "Decisão inválida"):
                    validate_review_decision(decision)


if __name__ == "__main__":
    unittest.main()
