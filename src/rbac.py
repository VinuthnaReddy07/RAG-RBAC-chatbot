# RBAC module
def is_allowed(role, chunk_meta, user_id=None):
    dept = chunk_meta.get("department")

    if role == "admin":
        return True

    if role == "manager":
        if dept == "legal":
            return chunk_meta.get("access") == "summary"
        return True

    if role == "employee":
        if dept == "hr":
            # allow general HR data
            if "owner" not in chunk_meta:
                return True
            # allow own records
            return chunk_meta.get("owner") == user_id
        return False

    if role == "auditor":
        return dept in ["finance", "legal"]

    return False