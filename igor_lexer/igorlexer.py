import re

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
    Comment, Text, String, Name, Keyword, Operator, Number, Punctuation

import igorbuiltins as builtins

IGOR_STD_ID = r'[A-Z][A-Z0-9_]{,30}(?i)' # Standard name (not a liberal name)
IGOR_PARAMETER = r'\[?\s*'+IGOR_STD_ID+'\s*\]'

class IgorLexer(RegexLexer):
    """
    Pygments Lexer for `Igor Pro <http://www.wavemetrics.com>`
    http://pygments.org
    """
    name = "Igor"
    aliases = ["igor", "igorpro"]
    filenames = ["*.ipf"]

    flags = re.IGNORECASE

    tokens = {
        "root" : [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/[A-Z]+', Keyword.Pseudo), # flags
            # directives
            (r'(#define|#undef|#ifdef|#ifndef)(\s+)',
             bygroups(Comment.Preproc, Text), "symbol_name"),
            (r'(#if|#elif|#endif|#include|#pragma)\b', Comment.Preproc),
            (r'(Structure)(\s+)', bygroups(Keyword, Text), "struct_name"),
            (r'(Function)(/(?:DF|WAVE|[CDS]))?(\s+)',
             bygroups(Keyword, Keyword.Reserved, Text), "proc_name"),
            (r'(Macro|Window|Proc)(\s+)', bygroups(Keyword, Text), "proc_name"),
            (r'((?:Str)?Constant)(\s+)', bygroups(Keyword, Text), "constant_name"),
            # variables declarations/types
            (r'(Variable|String|SVAR|NVAR|DFREF|FUNCREF|STRUCT|Wave)\b', Keyword.Type),
            # keywords
            (r'(if|else|elseif|do|while|for|try|'
             r'catch|switch|strswitch|case|default|'
             r'return|continue|break|AbortOnRTE|AbortOnValue|'
             r'End(?:Structure|Macro|if|for|try|switch)?|'
             r'Static|ButtonControl|CheckboxControl|CursorStyle|FitFunc|'
             r'Graph|GraphMarquee|GraphStyle|GridStyle|Layout|LayoutMarquee|'
             r'LayoutStyle|Panel|PopupMenuControl|SetVariableControl|'
             r'Table|TableStyle)\b', Keyword),
            # strings
            (r'"', String, "string"),
            (r"'", Name.Variable, "liberal_name"),
            (IGOR_STD_ID, Name),
            (r'!=|==|<=|>=|&&|\|\||&^|[-!~^*/+><&|?:$]', Operator),
             # numbers
            (r'\d*\.\d+([Ee][+-]?\d+)?', Number.Float),
            (r'0x[0-9a-f]+', Number.Hex),
            (r'\d+', Number.Integer),
#            (r'([+-]?\d+)?(\.)?\d+(?:[Ee][+-]?\d+)?', Number),
            (r'([+-]?Inf)|NaN', Name.Constant), # Inf/NaN
            (r'[(){}\[\],.=#;]', Punctuation),
            ],
        "string" : [
            (r'"', String, "#pop"),
            (r'\\([trn\'"\\]|[0-7]{3})', String.Escape),
            (r'[^\\"\n]+', String),
            ],
        "liberal_name" : [
            (r"'", Name.Variable, "#pop"),
            (r'[^"\':;]', Name.Variable),
            ],
        "symbol_name"   : [(IGOR_STD_ID, Name.Namespace, "#pop"),],
        "struct_name"   : [(IGOR_STD_ID, Name.Class, "#pop"),],
        "proc_name"     : [(IGOR_STD_ID, Name.Function, "#pop"),],
        "constant_name" : [(IGOR_STD_ID, Name.Constant, "#pop"),],
    }

    def get_tokens_unprocessed(self, text):
        for index, token, value in RegexLexer.get_tokens_unprocessed(self, text):
            if token is Name:
                if value in builtins.BUILTIN_FUNCTIONS:
                    token = Name.Builtin
                elif value in builtins.BUILTIN_OPERATIONS:
                    token = Name.Builtin.Pseudo
            yield index, token, value
