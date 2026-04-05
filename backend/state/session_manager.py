_sessions = {}

def get_session(client_id: str):
    if client_id not in _sessions:
        _sessions[client_id] = {
            "flow": {
                "step": "START"
            }
        }
    return _sessions[client_id]
