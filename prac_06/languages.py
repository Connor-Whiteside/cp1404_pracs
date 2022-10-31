"""CP1404 Languages program."""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Runs languages program."""
    print("Hello welcome to Programming Language Program.")

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


# print(python)

main()
