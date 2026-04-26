#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)









# Identificação e Correção de Erros no Código debug.py

## Erros Identificados

### Erro 1: Falta de Aspas na String de Input (Linha 5)
**Localização:** Linha 5
```python
item1 = float(input(Preço do item 1? ))
```

**Causa:** A string `Preço do item 1?` não está entre aspas. Python interpreta isso como código a executar, não como uma string literal, resultando em um `SyntaxError` ou `NameError`.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### Erro 2: Tipo de Dado Incorreto para desconto_cupom (Linha 17)
**Localização:** Linha 17
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

**Causa:** A função `input()` retorna uma string. Nas linhas 18 e 31, o código tenta fazer operações matemáticas (`/ 100`) e comparações (`> 0`) com uma string, o que causa um `TypeError`.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

---

### Erro 3: F-String Sem o Prefixo `f` (Linha 23)
**Localização:** Linha 23
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Causa:** A string contém placeholders `{}` para interpolação de variáveis, mas não possui o prefixo `f` que ativa a f-string. Sem o `f`, Python trata isso como uma string comum, não interpola as variáveis e imprime literalmente `{total_item2:.2f}`.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### Erro 4: Indentação Incorreta no Bloco If (Linha 30-31)
**Localização:** Linhas 30-31
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa:** A instrução `print()` não está indentada corretamente dentro do bloco `if`. Em Python, o corpo do bloco `if` deve estar indentado, caso contrário resulta em um `IndentationError`.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Código Corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## Resumo das Mudanças

| Linha | Erro | Correção |
|-------|------|----------|
| 5 | `input(Preço do item 1? )` | `input("Preço do item 1? ")` - Adicionar aspas |
| 17 | `desconto_cupom = (input(...))` | `desconto_cupom = float(input(...))` - Converter para float |
| 23 | `print(" Item 2: ...)` | `print(f" Item 2: ...)` - Adicionar prefixo `f` |
| 30-31 | Indentação incorreta do `print` | Indentar o `print` dentro do bloco `if` |

Após essas correções, o código executará sem erros e produzirá o resultado esperado: um recibo formatado com os itens, subtotal, imposto e desconto (se aplicável).