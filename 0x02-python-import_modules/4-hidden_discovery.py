#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    name = dir(hidden_4)
    for module in name:
        if module[:2] == '__':
            continue
        print(module)
