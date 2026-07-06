# Security Policy

Do not commit credentials, OAuth client secrets, refresh tokens, browser profiles, chat IDs, private customer data, or machine-specific absolute home paths.

If a workflow requires credentials, document the expected environment variable or local secret store name only. Never include a real value.

Before publishing a release, scan the repository for private paths and secret-like values, then manually inspect all matches.
