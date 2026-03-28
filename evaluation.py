from orchestrator import resolve_ticket

test_tickets = [
    {"ticket":"My order arrived late and cookies melted. I want refund.", "context":{"item_category":"perishable"}},
    {"ticket":"Shoes delivered wrong size. Can I exchange?", "context":{"item_category":"apparel"}},
    {"ticket":"I want refund for opened headphones.", "context":{"item_category":"electronics"}},
]

def evaluate():
    citation_coverage = 0
    unsupported_claims = 0
    for t in test_tickets:
        result = resolve_ticket(t["ticket"], t["context"])
        print("Ticket:", t["ticket"])
        print("Final:", result["final"])
        # Add manual rubric checks here
    print("Evaluation complete.")
