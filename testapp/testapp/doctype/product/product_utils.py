# Copyright (c) 2026, devika and contributors
# For license information, please see license.txt

"""Frappe-free Product helpers so validation can be unit-tested without a site."""

from __future__ import annotations

import re

# Letters, digits, dot, underscore, hyphen. First character must be alphanumeric.
PRODUCT_CODE_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def normalize_product_code(code: str | None) -> str:
	return (code or "").strip()


def is_valid_product_code(code: str) -> bool:
	return bool(code) and bool(PRODUCT_CODE_PATTERN.fullmatch(code))


def default_qr_code(qr_code: str | None, product_code: str | None) -> str:
	return (qr_code or "").strip() or (product_code or "").strip()
