
import streamlit as st
from groq import Groq

st.set_page_config(page_title="BA Requirements Assistant", layout="wide")

@st.cache_resource
def load_client():
    return Groq()

client = load_client()

st.title("AI Business Requirements Assistant")
st.caption("Paste a stakeholder interview or meeting transcript to generate a structured BRD draft.")

transcript_input = st.text_area("Paste transcript here", height=300)

if st.button("Generate Requirements") and transcript_input:
    with st.spinner("Extracting requirements..."):
        prompt = f"""You are a Business Analyst assistant. Read the stakeholder interview 
transcript below and extract structured requirements.

CRITICAL RULE: Only include requirements, numbers, or details that are explicitly 
stated or clearly implied in the transcript. Do NOT invent industry-standard 
non-functional requirements unless the stakeholder actually mentioned them. If a 
category is not addressed, write "Not discussed — recommend clarifying with 
stakeholder" rather than filling in a plausible-sounding default.

Produce:
1. Business Objective (1-2 sentences)
2. In-Scope items
3. Out-of-Scope items (explicitly mentioned as excluded)
4. Functional Requirements (numbered list)
5. Non-Functional Requirements (ONLY those the stakeholder actually raised)
6. Open Questions / Ambiguities (flag disagreements between stakeholders explicitly, citing both positions rather than resolving them)
7. User Stories in the format: As a [role], I want [goal], so that [benefit]

Transcript:
{transcript_input}
"""
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

    st.markdown("### Generated Requirements Document")
    st.markdown(result)

    st.download_button("Download as text", result, file_name="requirements_draft.txt")
