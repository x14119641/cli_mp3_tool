from pathlib import Path
from typing import List


def resolve_paths(base_dir:Path, pattern:str) -> List[Path]:
    """Given a base Dircetoru adn apttern or exact filename, return a list of matching files.
    Handles quoted names, wildcards and direct matches.

    Args:
        base_dir (Path): current path
        pattern (str): string is looking in the path with the tab

    Returns:
        List[Path]:
    """
    pattern = pattern.strip('"').strip("'")
    direct = base_dir / pattern
    if direct.exists():
        return [direct]
    return List(base_dir.glob(pattern))