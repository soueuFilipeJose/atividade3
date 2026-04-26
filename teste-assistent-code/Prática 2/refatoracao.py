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