"""Helpers for reading benchmark result files."""

import logging
import math

logger = logging.getLogger(__name__)


def parse_result_value(result: str, result_path: str) -> float:
    """Parse numeric and boolean evaluator output, treating invalid values as failures."""
    normalized = result.strip().casefold()
    if normalized == "true":
        return 1.0
    if normalized == "false":
        return 0.0

    try:
        value = float(normalized)
    except ValueError:
        logger.warning("Invalid result in %s; treating as failure.", result_path)
        return 0.0

    if not math.isfinite(value):
        logger.warning("Non-finite result in %s; treating as failure.", result_path)
        return 0.0

    return value
