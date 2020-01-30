# PYTHON POWER

### Captcha Solver

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

### Filtrando json pela URL:

tu pode colocar data_inicio_atv__lte=20192701

esse "__lte" no final significa "less than or equal"

ai só vai pegar empresas qu abriram até um ano atras

e como eu faço para filtrar por um intervalo de tempo? por exemplo, entre 1 e 3 anos?

tu pode mandar a mesma string duas vezes

primeiro manda data_inicio_atv__lte=20192701 e depois data_inicio_atv__gte=20162701

``` python
def test():
    s = session.requests_retry_session()
    response = s.post(URL, headers=HEADERS_TOKEN, data=json.dumps(BODY_TOKEN), verify=True)
    headers = {}
    headers['Authorization'] = 'Bearer {}'.format(response.json()['access'])
    url = 'https://suaAPI/empresas?data_inicio_ativ__lte=20190127&data_inicio_ativ__gte=20180127'
    response = s.get(url, headers=headers)
    print(response.content)
```
