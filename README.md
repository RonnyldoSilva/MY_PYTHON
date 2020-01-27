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

Filtrando json pela URL:
```
def test():
    s = session.requests_retry_session()
    response = s.post(PAP_TOKEN, headers=HEADERS_TOKEN, data=json.dumps(BODY_TOKEN), verify=True)
    headers = {}
    headers['Authorization'] = 'Bearer {}'.format(response.json()['access'])
    url = 'https://pap.pxs.ch/api/rfb-cnpj/empresas?data_inicio_ativ__lte=20190127&data_inicio_ativ__gte=20180127'
    #url = PAPYRUS_EMPRESAS + '&uf=' + uf + '&porte=' + porte + '&opc_mei=' + opc_mei + '&opc_simples=' + opc_simples
    response = s.get(url, headers=headers)
    print(response.content)
```
