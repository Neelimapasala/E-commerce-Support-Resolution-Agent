from pipeline import load_policies
from agents import run_groq_agent, triage_agent, retriever_agent, resolution_agent, compliance_agent

def resolve_ticket(ticket, order_context):
    policies = load_policies()

    triage = run_groq_agent(**triage_agent, ticket=ticket, order_context=order_context, policies=policies)
    evidence = run_groq_agent(**retriever_agent, ticket=ticket, order_context=order_context, policies=policies)
    draft = run_groq_agent(**resolution_agent, ticket=ticket, order_context=order_context, policies=policies)
    final = run_groq_agent(**compliance_agent, ticket=ticket, order_context=order_context, policies=policies)

    return {
        "classification": triage,
        "evidence": evidence,
        "draft": draft,
        "final": final
    }
