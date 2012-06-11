
from pygments.scanner import Scanner
from pygments.lexer import Lexer, RegexLexer, include, bygroups, using,\
	this, combined
from pygments.util import get_bool_opt, get_list_opt
from pygments.token import\
	Text, Comment, Operator, Keyword, Name, String, Number, Punctuation,\
	Error

import re

__all__ = ['UIL']

class UIL(RegexLexer):
	name = 'UIL'
	aliases = ['uil']
	filenames = ['*.uil']
	mimetypes = ['text/x-uil']

	flags = re.MULTILINE | re.DOTALL

	#: optional Comment or Whitespace
	_ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

	tokens = {
		'root': [
			(r'[^\S\n]+', Text),

			(r'(function|return|if|else|while|for|begin|end)\b',
			 Keyword),

			(r'//.*?\n', Comment.Single),
			(r'/\*.*?\*/', Comment.Multiline),




			(r'(var|const)\b', Keyword.Declaration),

			(r'(TRUE|FALSE|PI|E|I|INF)\b', Keyword.Constant),
			(r'(not|and|or|union|intersect|setminus|in)\b', Name.Attribute),
			(r'"(\\\\|\\"|[^"])*"', String),
			(r'[a-zA-Z_][a-zA-Z0-9_]*', Name.Label),
			#(r'([~\^\*!%&\[\]\(\)\{\}<>\|+=:;,./?-]|and|or|intersect)', Operator),
			#(r'[~\^\*!%&\[\]\(\)\{\}<>\|+=:;,./?-]', Name.Attribute),
			(r'[~\^\*!%&<>\|+=:./?-]', Name.Attribute),
			(r'[\(\)\[\]\{\},;]', Operator),
			(r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?', Number.Float),
			(r'[0-9]+L?', Number.Integer),

			(r'\n', Text),
		]
	}