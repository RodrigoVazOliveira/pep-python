def divid_two_numbers(number_one, number_two):
    return number_one / number_two


def test_divisor(divisor):
    try:
        result = divid_two_numbers(10, divisor)
        print(f'O resultado da divisão de 10 por {divisor} é {result}')
    except ZeroDivisionError as e:
        print(f'Erro de divisão por zero tratado, mensagem {e}')
    except AttributeError as e:
        print(f'Erro de atributo tratado, {e}')


test_divisor(0)
