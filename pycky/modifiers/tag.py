from ..checks.check import Check

def tag(tag, check_or_case):
    """Adds the given tag to the check or case."""
    if isinstance(check_or_case, Check):
        check_or_case.tags.add(tag)
    else: # It's a case
        case = check_or_case
        case.