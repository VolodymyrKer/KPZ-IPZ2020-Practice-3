import platform


def get_os():
    os = platform.system()
    if os == "Darwin":
        print("Mac")
    elif os == "Java":
        pass
    else: print(os)