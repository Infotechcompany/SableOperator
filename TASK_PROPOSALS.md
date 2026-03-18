# Task Proposals from Codebase Review

## 1) Typo fix task
**Title:** Correct README typo: `cyrptography` → `cryptography`

**Why:** The project description currently contains a spelling error that looks unpolished and can hurt discoverability.

**Acceptance criteria:**
- Update the README sentence to use `cryptography`.
- Ensure no other occurrences of `cyrptography` exist in the repository.

---

## 2) Bug fix task
**Title:** Allow input strings with spaces in decipher workflow

**Why:** The README says users must provide "a string with no spaces," which suggests the parsing/CLI flow likely breaks or truncates when whitespace is present. This is a usability bug for normal text deciphering.

**Acceptance criteria:**
- Update argument/input parsing so quoted strings with spaces are accepted end-to-end.
- Preserve backward compatibility for single-token input.
- Add explicit error handling when input is empty.

---

## 3) Documentation discrepancy task
**Title:** Align README with actual interface and behavior

**Why:** The README is too terse and likely diverges from the real behavior (input format, command usage, outputs). This discrepancy increases onboarding friction.

**Acceptance criteria:**
- Add a proper usage section (`install`, `run`, and concrete examples).
- Document whether spaces are supported in input and expected output format.
- Include constraints and known limitations that reflect implementation.

---

## 4) Test improvement task
**Title:** Add regression tests for input parsing edge cases

**Why:** Input handling is a likely risk area and currently under-documented. Tests should protect against regressions for common decipher inputs.

**Acceptance criteria:**
- Add tests for: empty input, single-word input, multi-word input, punctuation, and non-ASCII characters.
- Ensure tests assert both successful decode paths and expected error messages.
- Integrate tests into CI so failures block merges.
