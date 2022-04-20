import platform


def get_os():
    os = platform.system()
    if os == "Darwin":
        return "Mac"
    elif os == "Java":
        pass
    else:
        return os
