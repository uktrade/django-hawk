# Django HAWK

## 1.2.2
- Add tests and update dependencies for Django 5.0
- Update Django to 3.2.23

## 1.2.1
- Update Django to 3.2.19
- Update asgiref to 3.7.2

## 1.2.0
- Dropped support for Python versions under 3.7
- Dropped support for Django versions under 3.2

## 1.1.1
- `HawkResponseMiddleware` will no longer overwrite the "Server-Authorization" header if
  it is already set

## 1.1.0
- Update middleware so it can be inherited and altered as needed
- Add tests for Django 4.1

## 1.0.0
- Improve the authentication implementation

## 0.0.2
- Add Python typing compatibility as per https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages

## 0.0.1
Initial release to PyPI
