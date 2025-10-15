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

    prompt = f"""Write a warm, genuine compliment for {recipient_name}, who is a {relationship}. 

Focus on these qualities: {qualities_text}{context_section}

Make it {tone_guidance} and conversational. Keep it to 2-3 sentences. Highlight their positive character traits and impact. Start the compliment by addressing {recipient_name} directly.

Write the compliment directly:"""

    return prompt

