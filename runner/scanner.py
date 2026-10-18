"""Static code security scanner for untrusted Java code."""
import re

# Match string literals, char literals, line comments, and block comments
_STRIP_REGEX = re.compile(
    r'("""[\s\S]*?""")|'          # Java 15+ multiline text block
    r'("(?:\\.|[^"\\])*")|'       # String literal
    r"('(?:\\.|[^'\\])*')|"       # Char literal
    r'(//[^\r\n]*)|'              # Single-line comment
    r'(/\*[\s\S]*?\*/)',          # Block comment
    re.MULTILINE
)

# Ordered rules: (regex_pattern, api_display_name)
_FORBIDDEN_RULES = [
    (re.compile(r'\bRuntime(?:\s*\.\s*getRuntime)?\b'), 'Runtime.getRuntime'),
    (re.compile(r'\b(ProcessBuilder|ProcessHandle|java\s*\.\s*lang\s*\.\s*Process)\b'), 'ProcessBuilder'),
    (re.compile(r'\bSystem\s*\.\s*exit\b'), 'System.exit'),
    (re.compile(r'\bSystem\s*\.\s*getPropert(?:y|ies)\b'), 'System.getProperty'),
    (re.compile(r'\bSystem\s*\.\s*getenv\b'), 'System.getenv'),
    (re.compile(r'\bSystem\s*\.\s*set(?:Out|Err|In)\b'), 'System.setOut/setErr/setIn'),
    (re.compile(r'\bSystem\s*\.\s*(?:load|loadLibrary|inheritedChannel|setSecurityManager)\b'), 'System'),
    (re.compile(r'\b(java\s*\.\s*net|Socket|ServerSocket|HttpURLConnection|HttpClient)\b'), 'java.net'),
    (re.compile(r'\bjava\s*\.\s*nio\s*\.\s*file\b'), 'java.nio.file'),
    (re.compile(r'\bFiles\s*\.\s*'), 'java.nio.file.Files'),
    (re.compile(r'\b(?:java\s*\.\s*io\s*\.\s*)?(?:File|FileInputStream|FileOutputStream|FileReader|FileWriter|RandomAccessFile)\b'), 'java.io.File*'),
    (re.compile(r'\bjava\s*\.\s*lang\s*\.\s*reflect\b'), 'java.lang.reflect'),
    (re.compile(r'\bsetAccessible\b'), 'setAccessible'),
    (re.compile(r'\bClass\s*\.\s*forName\b'), 'Class.forName'),
    (re.compile(r'\bClassLoader\b'), 'ClassLoader'),
    (re.compile(r'\b(?:sun\.[a-zA-Z0-9_.]+|jdk\.internal\.[a-zA-Z0-9_.]+)\b'), 'sun.* or jdk.internal.*'),
    (re.compile(r'\b(Thread|ThreadGroup|ExecutorService|Executors|ThreadPoolExecutor|ForkJoinPool|CompletableFuture)\b'), 'Thread-based sandbox escapes'),
]


def strip_literals_and_comments(source: str) -> str:
    """
    Replace comments and string literals with whitespace preserving newlines.
    This prevents false positives in strings like "System.exit is forbidden"
    or comments explaining why an API is not used.
    """
    def _replace(match):
        text = match.group(0)
        newlines = text.count('\n')
        return '\n' * newlines if newlines > 0 else ' '

    return _STRIP_REGEX.sub(_replace, source)


def scan_untrusted_code(source: str) -> tuple[bool, str | None]:
    """
    Scan Java source code for prohibited APIs.
    Returns:
        (True, None) if clean.
        (False, error_message) if dangerous API is detected.
    """
    if not isinstance(source, str):
        return False, "Source code must be a string."

    cleaned = strip_literals_and_comments(source)
    for pattern, api_name in _FORBIDDEN_RULES:
        if pattern.search(cleaned):
            return False, f"Not allowed in this judge: {api_name}"

    return True, None
