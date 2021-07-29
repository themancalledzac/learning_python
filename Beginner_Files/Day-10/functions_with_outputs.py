# Functions with Outputs


def format_name(first, last):
    first_title = first.title()
    last_title = last.title()

    return f"{first_title} {last_title}"


print(format_name("zac", "edens"))
