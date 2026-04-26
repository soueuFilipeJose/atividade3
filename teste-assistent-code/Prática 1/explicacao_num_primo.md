# Versão Original (não otimizada)

Antes da otimização, a função estava escrita de forma mais simples e menos legível, mas ainda correta. A versão anterior usava um loop `while` com incremento manual e não tinha type hints, o que dificultava a leitura e a manutenção.

## Código da Versão Original

```python
def is_prime(n):
    """
    Verifica se um número é primo.
    
    Args:
        n (int): O número a ser verificado.
    
    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

## Análise da Versão Original

- **Legibilidade**: A função usava `if n <= 3:` em vez de `if n == 2 or n == 3:`, o que ainda é correto mas menos explícito para o caso dos primos conhecidos.
- **Type hints ausentes**: A versão original não especificava os tipos de entrada e retorno, o que reduz a documentação automática e a detecção de erros por ferramentas.
- **Uso de `while`**: O loop `while i * i <= n:` é funcional, mas a expressão `i * i <= n` é mais verbosa do que usar `math.isqrt(n) + 1` e requer controle manual de `i`.
- **Importação ausente de `math`**: A versão original não precisava do módulo `math`, mas também perdia a oportunidade de usar `math.isqrt` para melhorar a eficiência e clareza.
- **Código mais direto**: Apesar disso, a lógica de verificação dos divisores `i` e `i + 2` já estava correta, usando o padrão 6k±1 para pular múltiplos de 2 e 3.

## Melhorias na Versão Atual

1. **Adição de type hints**: `n: int` e `-> bool` explicam claramente os tipos esperados.
2. **Melhoria na legibilidade**: A condição `if n == 2 or n == 3:` é mais explícita e fácil de entender para quem lê o código.
3. **Uso de `math.isqrt`**: Substitui a verificação `i * i <= n` por `math.isqrt(n) + 1`, deixando explícito que a iteração vai até a raiz quadrada.
4. **Loop `for` mais idiomático**: `for i in range(5, math.isqrt(n) + 1, 6):` elimina o controle manual de incremento e torna o fluxo mais Pythonic.
5. **Documentação mais robusta**: A versão atual mantém a docstring e melhora a clareza geral do código.

---

# Explicação da Função is_prime

Esta explicação descreve linha por linha o código da função `is_prime` em Python, que verifica se um número é primo. A versão atual inclui otimizações para clean code, como type hints, uso de `math.isqrt` para raiz quadrada inteira e um loop `for` mais legível.

## Código da Função

```python
import math

def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        n (int): O número a ser verificado.
    
    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Teste da função
if __name__ == "__main__":
    print(is_prime(2))  # True
    print(is_prime(3))  # True
    print(is_prime(4))  # False
    print(is_prime(17)) # True
    print(is_prime(18)) # False
```

## Explicação Linha por Linha

1. **`import math`**  
   Importa o módulo `math` para usar `math.isqrt`, que calcula a raiz quadrada inteira de forma eficiente.

2. **`def is_prime(n: int) -> bool:`**  
   Define a função chamada `is_prime` com type hints: recebe um inteiro `n` e retorna um booleano.

3. **`"""`**  
   Início da docstring (documentação da função).

4. **`Verifica se um número é primo.`**  
   Descrição da função.

5. **`Args:`**  
   Seção que descreve os argumentos da função.

6. **`n (int): O número a ser verificado.`**  
   Especifica que `n` é um inteiro que representa o número a verificar.

7. **`Returns:`**  
   Seção que descreve o valor de retorno.

8. **`bool: True se o número for primo, False caso contrário.`**  
   Indica que a função retorna um booleano: True para primo, False para não primo.

9. **`"""`**  
   Fim da docstring.

10. **`if n < 2:`**  
    Verifica se `n` é menor que 2. Números menores que 2 não são primos (inclui negativos e 0, 1).

11. **`return False`**  
    Retorna False se `n` for menor que 2.

12. **`if n == 2 or n == 3:`**  
    Verifica se `n` é 2 ou 3. Esses são os únicos números primos pares e ímpares pequenos.

13. **`return True`**  
    Retorna True se `n` for 2 ou 3.

14. **`if n % 2 == 0 or n % 3 == 0:`**  
    Verifica se `n` é divisível por 2 ou por 3. Se for, não é primo (exceto 2 e 3, que já foram tratados).

15. **`return False`**  
    Retorna False se `n` for divisível por 2 ou 3.

16. **`for i in range(5, math.isqrt(n) + 1, 6):`**  
    Loop `for` que itera de 5 até a raiz quadrada inteira de `n`, incrementando de 6 em 6. Isso otimiza verificando apenas números da forma 6k±1.

17. **`if n % i == 0 or n % (i + 2) == 0:`**  
    Verifica se `n` é divisível por `i` ou por `i + 2`. Isso cobre os possíveis fatores primos restantes.

18. **`return False`**  
    Retorna False se encontrar um divisor.

19. **`return True`**  
    Se nenhum divisor for encontrado, retorna True (o número é primo).

20. **`# Teste da função`**  
    Comentário indicando o início dos testes.

21. **`if __name__ == "__main__":`**  
    Verifica se o script está sendo executado diretamente (não importado como módulo).

22. **`print(is_prime(2))  # True`**  
    Testa a função com 2 e imprime o resultado (deve ser True).

23. **`print(is_prime(3))  # True`**  
    Testa com 3 (True).

24. **`print(is_prime(4))  # False`**  
    Testa com 4 (False).

25. **`print(is_prime(17)) # True`**  
    Testa com 17 (True).

26. **`print(is_prime(18)) # False`**  
    Testa com 18 (False).