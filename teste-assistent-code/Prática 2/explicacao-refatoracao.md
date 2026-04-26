# Comparação: Código Original vs. Refatorado

Esta seção compara o código original com a versão refatorada, destacando as melhorias aplicadas para aumentar a legibilidade, manutenibilidade e aderência às boas práticas de programação em Python.

## Código Original

```python
import math
def c(r):
 return 2*math.pi*r
def a(r):
 return math.pi*r*r
def v(r,h):
 return math.pi*r*r*h
def xpto(r,h,tp):
 if tp==1:
  return c(r)
  elif tp==2:
   return a(r)
  elif tp==3:
   return v(r,h)
  else:
   return 0
x=float(input("r: "))
y=float(input("h: "))
z=int(input("op: "))
print(xpto(x,y,z))
```

## Código Refatorado

```python
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
```

## Melhorias Realizadas

1. **Nomenclatura Descritiva**:
   - Funções renomeadas de `c`, `a`, `v`, `xpto` para `calculate_circumference`, `calculate_area`, `calculate_volume`, `calculate_option`. Isso torna o código autoexplicativo.
   - Variáveis renomeadas: `r` → `radius`, `h` → `height`, `tp` → `option`, `x` → `radius`, `y` → `height`, `z` → `option`. Nomes curtos e não descritivos foram substituídos por nomes claros.

2. **Type Hints**:
   - Adicionados type hints como `radius: float` e `-> float` para indicar tipos de parâmetros e retorno. Isso melhora a legibilidade e permite detecção de erros por ferramentas como mypy.

3. **Docstrings**:
   - Cada função agora inclui uma docstring detalhada explicando propósito, argumentos e retorno. Isso segue o padrão PEP 257 e facilita a documentação e manutenção.

4. **Estrutura e Indentação**:
   - Corrigida a indentação incorreta no bloco `if-elif` da função `xpto`. Agora, o código é sintaticamente correto e mais legível.
   - Adicionado espaçamento consistente (e.g., `2 * math.pi * radius` em vez de `2*math.pi*r`).

5. **Separação de Responsabilidades**:
   - Funções separadas para cada cálculo, promovendo o princípio da responsabilidade única.
   - Bloco `if __name__ == "__main__":` para proteger o código de execução quando importado como módulo.

6. **Mensagens de Entrada Melhoradas**:
   - Inputs agora têm mensagens descritivas em português, como "Digite o raio:" em vez de "r:".
   - Output formatado com f-string para clareza.

7. **Consistência e Legibilidade Geral**:
   - Uso de constantes implícitas (math.pi) mantido, mas código mais espaçado.
   - Remoção de redundâncias e melhoria na organização lógica.

Essas mudanças tornam o código mais profissional, fácil de entender, manter e estender, seguindo boas práticas como PEP 8 e princípios de clean code.

## Análise dos Pontos Esperados no Código Original

### Nomes de Funções e Variáveis sem Significado
- As funções `c`, `a`, `v` e `xpto` não indicam seu propósito. É difícil entender que `c` calcula circunferência, `a` área, `v` volume e `xpto` é uma função seletora sem examinar o código.
- Variáveis como `r`, `h`, `tp`, `x`, `y`, `z` são abreviaturas genéricas que não transmitem significado. Por exemplo, `tp` poderia ser `tipo` ou `opcao`, mas permanece obscuro.

### Uso Inadequado de Estruturas de Repetição
- Este código não utiliza estruturas de repetição, então não há exemplos de uso inadequado como `range(len(lista))`. No entanto, se houvesse listas envolvidas, esse padrão anti-pattern seria problemático, pois ignora a eficiência do Python ao iterar diretamente sobre elementos.

### Retorno de Múltiplos Valores sem Estrutura Adequada
- A função `xpto` retorna apenas um valor por vez, não múltiplos. No entanto, em cenários onde múltiplos valores fossem necessários, retornar tuplas sem nomear (e.g., `return a, b, c`) tornaria o código confuso. Aqui, não se aplica diretamente, mas destaca a falta de clareza geral.

### Ausência de Documentação (Docstring/Comentários)
- Não há docstrings em nenhuma função, o que viola PEP 257. Também faltam comentários explicativos, tornando o código opaco para outros desenvolvedores ou para manutenção futura.

### Nomenclatura Genérica de Variáveis
- Variáveis como `x`, `y`, `z` são completamente genéricas e não indicam seu papel (raio, altura, opção). Isso leva a confusão e erros, especialmente em códigos maiores.

## Conclusões
O código original apresenta problemas graves de legibilidade e manutenibilidade devido à nomenclatura pobre e falta de documentação. Embora não haja loops ou retornos múltiplos, os pontos analisados ilustram anti-patterns comuns que tornam o código difícil de entender e modificar. A refatoração corrige esses issues, transformando-o em um código profissional e aderente às boas práticas de Python. Esses problemas, se não endereçados, podem levar a bugs, dificuldade de colaboração e alto custo de manutenção em projetos reais.