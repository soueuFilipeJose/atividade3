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