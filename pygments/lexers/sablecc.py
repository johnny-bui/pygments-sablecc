# -*- coding: utf-8 -*-
"""
	pygments.lexers.sablecc
	~~~~~~~~~~~~~~~~~~~~~~~

	Lexers for parser generators.

	:copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
	:license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, DelegatingLexer, \
	include, bygroups, using
from pygments.token import Punctuation, Other, Text, Comment, Operator, \
	 Keyword, Name, String, Number, Whitespace
from pygments.lexers.compiled import JavaLexer, CLexer, CppLexer, \
	ObjectiveCLexer, DLexer
from pygments.lexers.dotnet import CSharpLexer
from pygments.lexers.agile import RubyLexer, PythonLexer, PerlLexer
from pygments.lexers.web import ActionScriptLexer


__all__ = ['SableCC']

class SableCC(RegexLexer):
	"""
	Generic `SableCC`_ Lexer.
	.. _SableCC: http://sablecc.org/
	"""

	name = 'SableCC'
	aliases = ['sablecc']
	filenames = ['*.scc']

	#SCC_ID = r'[a-z]([a-z0-9])*(_[a-z]([a-z0-9])*)*',
	#_id = r'[a-z]+'
	_id = r'[a-z][a-z0-9_]*'
	tokens = {
		'package':[
			(r'[a-zA-Z_$]([a-zA-Z_$0-9])*',Other),
			(r';',Punctuation,'root'),
			include('whitespace'),
			include('comment'),
			include('common')
		],
		'root':[
			include('whitespace'),
			include('comment'),
			include('common'),
			(r'Package',Keyword,'package'),
			(r';',Punctuation)
		],
		'common':[
			(r'States',Keyword),
			(r'Helpers',Keyword),
			(r'Tokens',Keyword),
			(r'Ignored',Keyword),
			(r'Productions',Keyword),

			(r'Abstract',Keyword),
			(r'Syntax',Keyword),
			(r'Tree',Keyword),
			(r'New',Keyword),
			(r'Null',Keyword),

			#(r'T',Keyword.Reserved),
			#(r'P',Keyword.Reserved),

			(r'[.]',Punctuation),
			(r'[.][.]',Punctuation),

			(r'=',Operator),
			#(r'\[',Operator),
			#(r']',Operator),
			(r'\(',Operator),
			(r'\)',Operator),
			#(r'{',Operator),
			#(r'[}]',Operator),
			(r'[+]',Operator),
			#(r'[-]',Operator),
			(r'[?]',Operator),
			(r'[*]',Name.Tag),
			(r'[|]',Operator),
			(r'[,]',Operator),
			(r'[/]',Operator),
			#(r'>',Operator),
			(r':',Operator),
			# identifier
			(r'(' + _id + ')',Text),
			
			# char
			(r'(\')([^\n])(\')',bygroups(Operator,String,Operator)),
			
			# dec
			(r'[0-9]+',Name.Class),
			
			# hex
			(r'(0)(x|X)([abcdef]|[ABCDEF]|[0-9])+',
			bygroups(Name.Entity,Text,Name.Attribute)),
			
			# string
			(r'\'(?:\\\\|\\\'|[^\']*)\'',Name.Property),
			
			(r'(' + _id + r')(\s*)(=)',
			bygroups(String,Whitespace,Operator)),

			(r'(\[)(\s*)(' + _id +')(\s*)(])' + r'(\s*)(:)(\s*)(' + _id + r')',
			bygroups(Operator,Whitespace ,Keyword.Label,Whitespace, \
				Operator, Whitespace, Keyword.Namespace, Whitespace ,Text)),

			(r'({)(\s*)(' + _id + ')(\s*)([}])',
			bygroups(Operator,Whitespace,Name.Attribute,Whitespace,Operator)),

			(r'({)(\s*)(->)(\s*)(' + _id + ')(\s*)(\*?)(\s*)(})',
			bygroups(Operator, Whitespace, Operator,Whitespace, \
				Name.Constant, Whitespace, Name.Tag,Whitespace, Operator))
		],
		'whitespace':[
			(r'[ \t\n\r\f\v]+',Whitespace)
		],
		'comment':[
			(r'//.*$',Comment),
			(r'(/[*])([^*]*)([*]+)([^*/][^*]*[*]+)*[/]',Comment)
		]
	}

	#def analyse_text(text):
	#	return re.search(r'^\s*grammar\s+[a-zA-Z0-9]+\s*;', text, re.M)


