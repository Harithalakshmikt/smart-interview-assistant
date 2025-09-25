def chunk_and_clean(snippets):
    return [s.strip() for s in snippets if len(s.strip()) > 50][:3]
