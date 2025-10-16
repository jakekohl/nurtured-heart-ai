def create_nurtured_heart_prompt(
    recipient_name: str,
    relationship: str,
    qualities: list[str],
    context: str | None = None,
    tone: str = "warm"
) -> str:
    """
    Creates a prompt for generating Nurtured Heart compliments.

    Nurtured Heart Approach focuses on:
    - Recognizing positive behaviors and qualities
    - Being specific and genuine
    - Highlighting inner wealth and greatness
    - Avoiding comparative language
    - Celebrating who they are, not just what they do
    """

    qualities_text = ", ".join(qualities)
    context_section = f"\n\nRecent context: {context}" if context else ""

    tone_guidance = {
        "warm": "warm and caring",
        "encouraging": "encouraging and uplifting",
        "celebratory": "celebratory and joyful",
        "gentle": "gentle and supportive"
    }.get(tone, "warm and caring")

    prompt = f"""You are writing a warm, genuine compliment for {recipient_name}, who is a {relationship}.

Focus on these qualities: {qualities_text}{context_section}

Make it {tone_guidance} and conversational. Keep it to 2-3 sentences. Highlight their positive character traits and impact.

IMPORTANT: Output ONLY the compliment text itself. Do not include any preamble, introduction, or meta text like "Here's a compliment" or "Here's what I would say". Start directly by addressing {recipient_name} by name.

Example format: "{recipient_name}, [your compliment here]"

Your compliment:"""

    return prompt

