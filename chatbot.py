import streamlit as st
from orchestrator import resolve_ticket

st.set_page_config(
    page_title="ResolveIQ Chatbot",
    page_icon="⚡",
    layout="wide",
)

st.title("🤖 ResolveIQ Chatbot")
st.markdown("Ask me anything about support tickets, or paste a ticket to get a full resolution!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your support ticket or question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Determine if it's a ticket or question
    if "order" in prompt.lower() or "#" in prompt or "ticket" in prompt.lower():
        # Treat as ticket
        with st.chat_message("assistant"):
            with st.spinner("Analyzing ticket..."):
                try:
                    result = resolve_ticket(prompt, "")  # Empty order_context for now
                    response = f"""
**Classification:** {result['classification']}

**Evidence:** {result['evidence']}

**Draft Response:** {result['draft']}

**Final Response:** {result['final']}
"""
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    st.markdown(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
    else:
        # Treat as general question
        with st.chat_message("assistant"):
            response = "I'm ResolveIQ, your enterprise support intelligence assistant. I can help resolve customer support tickets by classifying them, gathering evidence, drafting responses, and ensuring compliance. Paste a ticket above to get started!"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})