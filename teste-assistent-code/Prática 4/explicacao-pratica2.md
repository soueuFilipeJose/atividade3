import math

def calculate_circumference(radius: float) -> float:
    """
    Calcula a circunferência de um círculo dado o raio.

    Args:
        radius (float): O raio do círculo.

    Returns:
        float: A circunferência.
    """
    return 2 * math.pi * radius

def calculate_area(radius: float) -> float:
    """
    Calcula a área de um círculo dado o raio.

    Args:
        radius (float): O raio do círculo.

    Returns:
        float: A área.
    """
    return math.pi * radius * radius

def calculate_volume(radius: float, height: float) -> float:
    """
    Calcula o volume de um cilindro dado o raio e a altura.

    Args:
        radius (float): O raio da base do cilindro.
        height (float): A altura do cilindro.

    Returns:
        float: O volume.
    """
    return math.pi * radius * radius * height

def calculate_option(radius: float, height: float, option: int) -> float:
    """
    Calcula uma propriedade baseada na opção selecionada.

    Args:
        radius (float): O raio.
        height (float): A altura (usada apenas para volume).
        option (int): A opção (1: circunferência, 2: área, 3: volume).

    Returns:
        float: O resultado do cálculo ou 0 se inválido.
    """
    if option == 1:
        return calculate_circumference(radius)
    elif option == 2:
        return calculate_area(radius)
    elif option == 3:
        return calculate_volume(radius, height)
    else:
        return 0.0

if __name__ == "__main__":
    radius = float(input("Digite o raio: "))
    height = float(input("Digite a altura: "))
    option = int(input("Digite a opção (1: Circunferência, 2: Área, 3: Volume): "))
    result = calculate_option(radius, height, option)
    print(f"Resultado: {result}")

##Codigo da prática 2 refatorado.

## Explicação Linha por Linha do Codigo da prática 2 refatorado.

1. **`import math`**  
   Importa o módulo `math` para utilizar `math.pi` (constante Pi ≈ 3.14159) em cálculos geométricos.

2. **`def calculate_circumference(radius: float) -> float:`**  
   Define a função `calculate_circumference` com type hints. Recebe `radius` (float) e retorna float. Calcula a circunferência de um círculo.

3-8. **Docstring de `calculate_circumference`**  
   Documentação que explica o propósito da função, seus argumentos (Args) e valor de retorno (Returns).

9. **`return 2 * math.pi * radius`**  
   Retorna a circunferência usando a fórmula: 2πr (2 × π × raio).

10. **`def calculate_area(radius: float) -> float:`**  
    Define a função `calculate_area` com type hints. Recebe `radius` (float) e retorna float. Calcula a área de um círculo.

11-16. **Docstring de `calculate_area`**  
    Documentação explicando que a função calcula a área do círculo.

17. **`return math.pi * radius * radius`**  
    Retorna a área usando a fórmula: πr² (π × raio × raio).

18. **`def calculate_volume(radius: float, height: float) -> float:`**  
    Define a função `calculate_volume` com type hints. Recebe `radius` (float) e `height` (float), retorna float. Calcula o volume de um cilindro.

19-24. **Docstring de `calculate_volume`**  
    Documentação explicando que a função calcula o volume de um cilindro dado raio e altura.

25. **`return math.pi * radius * radius * height`**  
    Retorna o volume usando a fórmula: πr²h (π × raio² × altura).

26. **`def calculate_option(radius: float, height: float, option: int) -> float:`**  
    Define a função `calculate_option` que coordena qual cálculo executar baseado na opção escolhida. Recebe `radius` (float), `height` (float) e `option` (int), retorna float.

27-32. **Docstring de `calculate_option`**  
    Documentação detalhada indicando que a função seleciona qual cálculo realizar baseado na opção (1, 2 ou 3).

33. **`if option == 1:`**  
    Verifica se `option` é igual a 1.

34. **`return calculate_circumference(radius)`**  
    Se option é 1, chama `calculate_circumference` e retorna o resultado (circunferência).

35. **`elif option == 2:`**  
    Else-if: verifica se `option` é igual a 2.

36. **`return calculate_area(radius)`**  
    Se option é 2, chama `calculate_area` e retorna o resultado (área).

37. **`elif option == 3:`**  
    Else-if: verifica se `option` é igual a 3.

38. **`return calculate_volume(radius, height)`**  
    Se option é 3, chama `calculate_volume` e retorna o resultado (volume).

39. **`else:`**  
    Se nenhuma das opções anteriores (1, 2 ou 3) for verdadeira.

40. **`return 0.0`**  
    Retorna 0.0 para indicar uma opção inválida.

41. **`if __name__ == "__main__":`**  
    Verifica se o script está sendo executado diretamente (não importado como módulo). Isso permite que o código só execute quando o arquivo é rodado diretamente.

42. **`radius = float(input("Digite o raio: "))`**  
    Solicita ao usuário que digite o raio e converte a entrada (string) para float.

43. **`height = float(input("Digite a altura: "))`**  
    Solicita ao usuário que digite a altura e converte a entrada para float.

44. **`option = int(input("Digite a opção (1: Circunferência, 2: Área, 3: Volume): "))`**  
    Solicita ao usuário que escolha uma opção (1 para circunferência, 2 para área, ou 3 para volume) e converte para int.

45. **`result = calculate_option(radius, height, option)`**  
    Chama a função `calculate_option` com os valores fornecidos pelo usuário e armazena o resultado na variável `result`.

46. **`print(f"Resultado: {result}")`**  
    Imprime o resultado usando uma f-string, exibindo "Resultado: " seguido do valor calculado.

## Resumo da Funcionalidade

Este código implementa um sistema de cálculos geométricos com as seguintes características:
- **4 funções principais** que calculam propriedades de círculos e cilindros
- **Type hints** para melhor documentação e detecção de erros
- **Docstrings** completas em cada função
- **Interface interativa** que permite ao usuário escolher qual cálculo realizar
- **Validação** básica de entrada através de conversão de tipos (int, float)
- **Estrutura if-elif-else** para rotear a opção selecionada para a função apropriada
