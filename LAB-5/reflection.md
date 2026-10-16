# Lab 5 Reflection

## 1. What is static code analysis?
Static code analysis examines source code without running the program. It can identify likely bugs, security weaknesses, and style violations before deployment.

## 2. What are the roles of Pylint, Bandit, and Flake8?
Pylint checks code quality, likely programming mistakes, naming, and design issues. Bandit searches Python code for common security risks. Flake8 reports style and formatting problems, including many PEP 8 violations.

## 3. What problems were identified and how were they addressed?
The original program used `eval()` for fee calculation, a mutable default list, a bare exception handler, shell execution for a simple message, a file without a context manager, a hardcoded secret-like value, MD5, and non-cryptographic random PIN generation. The revised program uses a numeric multiplier, initializes the log list safely, validates slot IDs, uses a context manager, removes shell execution, reads the secret configuration from an environment variable, and uses SHA-256 and `secrets`.

## 4. How does static analysis improve software quality?
Static analysis finds issues early, encourages consistent code, and helps reduce maintainability and security risks. It does not prove that a program is bug-free, so tests and code review are still needed.

## Verification note
Run the three tools on both the original and corrected files and use their actual outputs as the before/after reports. Do not claim a specific score unless it appears in your Pylint output.
