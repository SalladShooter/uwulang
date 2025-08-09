import re

REPLACEMENTS = {
    r"\btwue\b": "True",
    r"\bfawse\b": "False",
    r"\bpwint\b": "print",
    r"\bwetun\b": "return",
    r"\bewse\b": "else",
    r"\bewse if\b": "elif",
    r"\bwhiwe\b": "while",
    r"\bfoh\b": "for",
    r"\bfwom\b": "from",
    r"\bimpowt\b": "import",
    r"\bcwass\b": "class",
    r"\bfwunc\b": "def",
    r"\bnyone\b": "None",
}

INDENT = " " * 4

def replace_keywords(src):
    for pattern, repl in REPLACEMENTS.items():
        src = re.sub(pattern, repl, src)
    return src

def braces_to_indent(src):
    lines = []
    indent_level = 0
    for line in src.splitlines():
        line = line.strip()
        if line.endswith("{"):
            line = line[:-1].rstrip() + ":"
            lines.append(" " * (indent_level * 4) + line)
            indent_level += 1
        elif line == "}":
            indent_level = max(indent_level - 1, 0)
        else:
            lines.append(" " * (indent_level * 4) + line)
    return "\n".join(lines) + "\n"

def transpile(src):
    replaced = replace_keywords(src)
    indented = braces_to_indent(replaced)
    return indented
