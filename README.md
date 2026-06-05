# HTTP Security Headers Scanner

A command-line tool that scans a website's HTTP response headers against the OWASP recommended security headers and produces a security grade report.

## What It Does

1. Accepts a URL (with `http://` or `https://` scheme)
2. Sends a request and inspects the response headers
3. Checks for the presence of OWASP-recommended security headers
4. Calculates a weighted security score and assigns a grade
5. Writes a detailed report to `inspect.txt`

## Checked Headers

| Header | Severity | Score |
|--------|----------|-------|
| `Strict-Transport-Security` | High | 10 |
| `Content-Security-Policy` | High | 10 |
| `X-Frame-Options` | Medium | 5 |
| `X-Content-Type-Options` | Medium | 5 |
| `Referrer-Policy` | Low | 2 |
| `Permissions-Policy` | Low | 2 |
| `Content-Type` | Low | 2 |
| `X-Robots-Tag` | Low | 2 |

**Max score: 38 points**

## Grading

| Grade | Score Range |
|-------|-------------|
| A | 90% – 100% |
| B | 65% – 80% |
| C | 50% – 65% |
| F | 0% – 50% |

## Requirements

- Python 3.8+
- [httpx](https://www.python-httpx.org/)

```
pip install httpx
```

## Usage

```bash
python main.py
```

You will be prompted to enter a URL:

```
Insert URL with the scheme (http:// or https://) : https://example.com
```

After the scan, results are printed to the terminal and saved to `inspect.txt`.

## Output

- Terminal: security grade and score percentage
- `inspect.txt`: list of missing headers with their severity levels

## References

- [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
