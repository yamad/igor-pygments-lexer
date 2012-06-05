from setuptools import setup

__author__ = "Jason Yamada-Hanff"

setup(
    name="Igor Pygments Lexer",
    version="0.1",
    author=__author__,
    description="Pygments Lexer for the Igor Pro Language",
    packages=['igor_lexer'],
    requires=['pygments'],
    entry_points="""
[pygments.lexers]
igor = igor_lexer:IgorLexer
"""
)

