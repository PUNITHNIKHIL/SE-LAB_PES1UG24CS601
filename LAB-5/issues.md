# Lab 5: Static Code Analysis — Issue Table

| Issue | Type | Original location | Description | Fix approach |
|---|---|---|---|---|
| `eval()` on input expression | Security | `calculateParkingFee` | Executes a string as Python code and can run unintended commands. | Accept a numeric surge multiplier and calculate `base_rate * multiplier`. |
| Mutable default argument | Bug | `parkVehicle(..., entry_logs=[])` | The same list can be reused across calls. | Use `None` and create a new list inside the function. |
| Bare exception | Reliability | `releaseSlot` | Catches every exception and hides errors. | Validate the slot ID and return `False` for an invalid slot. |
| Shell command execution | Security | `exportParkingManifest` | Uses `os.system` for a simple message and concatenates a filename into a shell command. | Use `print()` instead. |
| File not managed by context manager | Reliability | `exportParkingManifest` | If writing fails, `close()` may not run. | Use `with open(..., encoding="utf-8")`. |
| Hardcoded secret | Security | `main` | Secret-like value is embedded in source code and printed. | Read the setting from an environment variable and do not print the secret. |
| Weak hash algorithm | Security | `generateVehicleHash` | MD5 is not appropriate when a modern hash is required. | Use SHA-256 for the sample identifier hash. |
| Weak PIN generation | Security | `generateTicketPin` | `random` is not designed for security-sensitive PINs. | Use `secrets.randbelow`. |
| Unused imports/variables | Quality | Imports and availability function | Unused names make code harder to maintain. | Remove unused imports and variables. |
| Naming and formatting | Style | Multiple functions | CamelCase names and long lines conflict with common Python conventions. | Use snake_case and standard formatting. |

Note: Replace descriptions of line numbers with the exact line numbers shown by your own analyzer output if your instructor requires line numbers. The before/after report text files must be generated locally with the installed tools; this package does not pretend that unrun tools produced results.
