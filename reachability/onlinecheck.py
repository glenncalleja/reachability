import socket


def isonline(host="1.1.1.1", port=53, timeout=3) -> bool:
    """
    Check if we are currently connecting to the host or not
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(timeout)
            s.connect((host, port))
            return True
    except Exception:
        return False
