def make_short_answer(response: str) -> str:
    """
    Split the response into sentences and return only the sentences that have a sum of characters less than 2500.

    Args:
        response (str): The response from ChatGPT.

    Returns:
        str: The shortened response.
    """
    # Take full sentences that have a sum of characters less than 2500 in total
    sentences = response.split('.')
    total_chars = 0
    short_sentences = []
    for sentence in sentences:
        if total_chars + len(sentence) < 2500:
            short_sentences.append(sentence)
            total_chars += len(sentence)
        else:
            break

    return '.'.join(short_sentences)    