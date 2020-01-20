# PYTHON POWER

All utils python function

```python
def scrape(id = None):
    if not id:
        raise InsufficientInformation

    cs = CaptchaSolver('rfb_cnpj')
    captcha_val = cs._solve_recaptcha(POST_URL, GOOGLE_KEY)
    print(captcha_val)

    headers = {
        'recaptcha': captcha_val
    }

    s = session.requests_retry_session()
    response = s.post(POST_URL, headers=headers, json={"id":id,"naturezas":"0000000"})
    print(response.content)
```
 
