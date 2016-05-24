# check-swagger

[pre-commit][pc] hook to validate swagger specs, leveraging Yelp's [swagger_spec_validator][ssv].

Applies to filenames matching the pattern `.*swagger.*\.(json|yaml|yml)`.

## Usage

### pre-commit

Add the following entry to `.pre-commit-config.yaml`:

```yaml
- repo: git://github.com/jstewmon/check-swagger
  sha: v0.1.0
  hooks:
  - id: check-swagger
```

Options:

* `-x PATTERN, --exclude PATTERN` filename patterns to exclude from validation.

## Standalone Usage

[pc]: http://pre-commit.com
[ssv]: https://github.com/Yelp/swagger_spec_validator
