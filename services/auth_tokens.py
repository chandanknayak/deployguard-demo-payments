def refresh_token(user_id: str, ttl: int = 3600) -> dict:
    """Refresh OAuth session token with fixed TTL."""
    return {"user_id": user_id, "ttl": ttl}
