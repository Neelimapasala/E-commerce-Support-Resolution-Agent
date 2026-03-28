from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)

def run_groq_agent(role, goal, backstory, instructions, ticket, order_context, policies):
    context = "\n\n".join([f"{name}:\n{content}" for name, content in policies.items()])
    prompt = f"""
Role: {role}
Goal: {goal}
Backstory: {backstory}

Customer ticket: {ticket}
Order context: {order_context}

Relevant policies:
{context}

Instructions:
{instructions}
    """

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
)
    return response.choices[0].message.content


# Define agent configs as dictionaries
triage_agent = {
    "role": "Triage Agent",
    "goal": "Classify issue type and ask clarifying questions",
    "backstory": "You categorize tickets into refund, shipping, payment, promo, fraud, or other.",
    "instructions": """
    Classify the issue type with confidence.
    If information is missing, ask up to 3 clarifying questions.
    Output: Classification + Clarifying Questions.
    """
}

retriever_agent = {
    "role": "Policy Retriever Agent",
    "goal": "Retrieve relevant policy excerpts with citations",
    "backstory": "You query the provided policies and return evidence only.",
    "instructions": """
    Search the policies for relevant rules.
    Return only excerpts with citations (doc + section).
    Do not invent policy.
    """
}

resolution_agent = {
    "role": "Resolution Writer Agent",
    "goal": "Draft customer-ready responses using only retrieved evidence",
    "backstory": "You write polite, accurate, citation-backed resolutions.",
    "instructions": """
    Draft a structured resolution:
    - Decision: approve/deny/partial/escalate
    - Rationale: policy-based explanation
    - Citations: bullet list
    - Customer Response Draft
    - Internal Notes
    Use only retrieved evidence.
    """
}

compliance_agent = {
    "role": "Compliance Agent",
    "goal": "Block unsupported claims, enforce citations, escalate conflicts",
    "backstory": "You ensure safety, compliance, and abstention when needed.",
    "instructions": """
    Verify the resolution:
    - Check for unsupported statements
    - Ensure citations are present
    - Escalate if conflict or missing policy
    Output: Final safe resolution or escalation notice.
    """
}
