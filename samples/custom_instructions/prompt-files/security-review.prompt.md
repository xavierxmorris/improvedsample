# API Security Review

Your goal is to perform a security review of REST API endpoints.

## Review Checklist

### Authentication & Authorization

- [ ] All sensitive endpoints require authentication
- [ ] Authorization checks are performed before data access
- [ ] User can only access their own resources
- [ ] Admin-only routes are properly protected

### Input Validation

- [ ] All user inputs are validated before processing
- [ ] Input types are checked (string, int, etc.)
- [ ] Input lengths are limited appropriately
- [ ] Special characters are sanitized or escaped
- [ ] SQL injection prevention through parameterized queries

### Data Protection

- [ ] Sensitive data is not logged
- [ ] Passwords are hashed, not stored in plain text
- [ ] API keys and secrets are not exposed in responses
- [ ] Personal data follows privacy requirements

### Rate Limiting

- [ ] Rate limiting is implemented on public endpoints
- [ ] Login endpoints have brute-force protection
- [ ] API abuse prevention mechanisms exist

### Error Handling

- [ ] Error messages don't expose system internals
- [ ] Stack traces are not sent to clients
- [ ] Errors are logged for monitoring
- [ ] Consistent error response format

### HTTPS & Headers

- [ ] All traffic uses HTTPS
- [ ] Security headers are set (CORS, CSP, etc.)
- [ ] Cookies have secure flags when used

## Common Vulnerabilities to Check

1. **SQL Injection** - Use ORM or parameterized queries
2. **XSS** - Sanitize user input, escape output
3. **CSRF** - Use tokens for state-changing operations
4. **IDOR** - Verify user owns the resource
5. **Mass Assignment** - Whitelist allowed fields

## Report Format

For each issue found:
```
## [SEVERITY] Issue Title

**Location:** file.py:line_number
**Description:** What the vulnerability is
**Impact:** What could happen if exploited
**Recommendation:** How to fix it
```

Severity levels: CRITICAL, HIGH, MEDIUM, LOW, INFO
