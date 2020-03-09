# PYTHON UTILITY 
 
### Filter Numbers from string 
``` python
doc = ''.join(filter(lambda x: x.isdigit(), doc)
```

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

"Coloque data_inicio_atv__lte=20192701, esse "__lte" no final significa "less than or equal", ai só vai pegar empresas qu abriram até um ano atras, e como eu faço para filtrar por um intervalo de tempo? por exemplo, entre 1 e 3 anos? 
tu pode mandar a mesma string duas vezes, primeiro manda data_inicio_atv__lte=20192701 e depois data_inicio_atv__gte=20162701" 

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

### parser string

```python
def string_parser(response):
    results = {}
    resp_str = response.text
    head = 0

    while head < len(resp_str) - 1:
        cod_reg = resp_str[head:head+4]

        structure_reg = sr.regs_maps[cod_reg]
        reg = {}
        for row in structure_reg:
            reg[row[4]] = resp_str[head:head + row[2]]
            head += row[2]

        if not cod_reg in results:
            results[cod_reg] = reg
        else:
            if isinstance(results[cod_reg], dict):
                results[cod_reg] = [ results[cod_reg], reg ]
            else:
                results[cod_reg].append(reg)
                
    return results
```

### FLASK: send data to front-end:
```python
@app.route('/smileCounter')
def smileCounter():
    return str(faceHunter.getSmileCounter())
    
app.jinja_env.globals.update(smileCounter=smileCounter) 
```

### Parser HTML to print:
```python
response = s.post(URL_ROOT, data=DATA, timeout = 15)

print(response.content.decode('utf-8'))
```

### Print JSON 
```python
print(json.dumps(result, indent=4, ensure_ascii=False))
```
