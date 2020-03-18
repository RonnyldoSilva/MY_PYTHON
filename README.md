# MY PYTHON NOTES
 
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

### Remove NULL bytes
```shell
sed -i 's/\x0//g' empresas.csv
```

### Split CSV 1000 lines each
```shell
split -l 1000 empresas.csv new.csv
```

### Reading the first column of a CSV
```python
def get_protestos_from_cenprot(csv_file):
    with open(csv_file, 'r') as read_obj, \
        open('output.csv', 'w', newline='') as write_obj:
            csv_reader = csv.reader(read_obj, delimiter=';')
            csv_writer = csv.writer(write_obj, delimiter=';')
            jump_first_line = True
            for row in csv_reader:
                if jump_first_line:
                    jump_first_line = False
                    continue
                print(row[0])
                protestos = sc.scrape(row[0])
                if protestos['qtdTitulos'] > 0:
                    print(protestos['cartorio'])
                else:
                    print(protestos['qtdTitulos'])
```

## BeautifulSoup
### get input tag from html
```python
    soup = BeautifulSoup(response.text.strip(), 'html.parser')
    inputs = soup.find_all('input')
    token = inputs[7]['name'] #to get the value of attribute name.
```
### get text between tags:
```python
results = []
    for i in range(0,len(rows[1]), 9):
        results.append({
            'nome_do_funcionario': rows[1][i+1].text.strip(),
            'sigla_orgao': rows[1][i+2].text.strip(),
            'cargo': rows[1][i+3].text.strip(),
            'data_admissao': rows[1][i+4].text.strip(),
            'valor_bruto': rows[1][i+5].text.strip(),
            'descontos': rows[1][i+6].text.strip(),
            'valor_bruto_descontos': rows[1][i+7].text.strip()
        })
```

## PDF
### pdf to table:
```python
   def get_table(pdf):
       table = []
       with open(pdf, "rb") as f:
           pages = pdftotext.PDF(f)
           for page in pages:
               lines = page.split('\n')
               for line in lines:
                   words = line.split('   ')
                   while("" in words): 
                       words.remove("")
                   table.append(words)

       return table
```

## JSON
### remove spaces from a dictionary keys and values:
