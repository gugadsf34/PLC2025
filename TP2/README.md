# **Pergunta**:
```
## **Conversor de MarkDown para HTML**

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

### Bold: pedaços de texto entre "**":

In: `Este é um **exemplo** ...`

Out: `Este é um <b>exemplo</b> ...`

### Itálico: pedaços de texto entre "*":

In: `Este é um *exemplo* ...`

Out: `Este é um <i>exemplo</i> ...`

### Lista numerada:

In:
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>


### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`
```


# **Resposta**
```
import re


texto="""
# Exemplo
## Exemplo
### Exemplo
Este é um **exemplo** ...
Este é um *exemplo* ...
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Exemplo
"""

#tirar ?P<> para os q sao inutil

def subs(texto):
    # cabeçalho
    def hashtag(t):
        qt=len(t.group(1))
        return f'<h{qt}>'+t.group("texto")+f'</h{qt}>'
    t1=re.sub(r'(#{1,3})\s+(?P<texto>.*)', hashtag, texto) 

    #bold
    t2=re.sub(r'\*\*(?P<texto>.*?)\*\*', r'<b>\1</b>', t1)

    #italico
    t3=re.sub(r'\*(?P<texto>.*?)\*', r'<i>\1</i>', t2)

    #lista
    t4=re.sub(r'^\d+\.\s(.+)$', r'<li>\1</li>', t3, flags=re.MULTILINE)
    t5=re.sub(r'((?:<li>.*</li>\s*\n?)+)+', r'<ol>\n\1</ol>\n', t4, flags=re.MULTILINE)

    #link & imagem
    def link_image(t):
        text=t.group('text')
        if '!' not in text:
            #link
            return f'{text}<a href="{t.group("link")}">{t.group("pagina")}</a>'
        else:
            #imagem
            text=text.replace('!', '')
            return f'{text}<img src="{t.group("link")}" alt="{t.group("pagina")}"/>'

    t6=re.sub(r'(?P<text>.*)\[(?P<pagina>.*)\]\((?P<link>.*)\)', link_image, t5)
    print("\nResultado final:\n", t6)

subs(texto)
```
