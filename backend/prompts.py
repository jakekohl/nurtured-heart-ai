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

    prompt = f"""You are a Nurtured Heart Approach expert. Generate a genuine, heartfelt compliment for {recipient_name}, who is a {relationship}.

Key qualities to recognize: {qualities_text}{context_section}

Guidelines for the compliment:
1. Be specific and genuine - reference the actual qualities mentioned
2. Focus on their inner greatness and character, not just actions
3. Use "I notice" or "I see" statements when appropriate
4. Highlight their positive impact and presence
5. Avoid comparisons to others or conditional praise
6. Make it {tone_guidance} in tone
7. Keep it to 2-4 sentences
8. Make it feel personal and authentic

Generate a Nurtured Heart compliment now:"""

    return prompt

