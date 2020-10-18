import socket


def isonline(host="1.1.1.1", port=53, timeout=3) -> bool:
    '''
    Check if we are currently connecting to the host or not
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False
