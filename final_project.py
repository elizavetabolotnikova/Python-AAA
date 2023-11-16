import click
import time
from functools import wraps


class Pizza:
    def __init__(self, name, ingredients, size='L'):
        """Инициализирует объект Pizza.

              Аргументы:
              name (str): Название пиццы.
              ingredients (list): Ингредиенты пиццы.
              size (str): Размер пиццы (по умолчанию 'L').
              """

        self.name = name
        self.ingredients = ingredients
        self.size = size

    def dict(self):
        """Возвращает данные о пицце в виде словаря."""
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'size': self.size
        }


class Margherita(Pizza):
    def __init__(self, size):
        name = 'Margherita🍅'
        ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        size = size
        super().__init__(name, ingredients, size)


class Pepperoni(Pizza):
    def __init__(self, size):
        name = 'Pepperoni🍕'
        ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        size = size
        super().__init__(name, ingredients, size)


class Hawaiian(Pizza):
    def __init__(self, size):
        name = 'Hawaiian🌴'
        ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        size = size
        super().__init__(name, ingredients, size)


def log_time(template=''):
    """Декоратор, измеряющий время выполнения функции."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = round(time.time() - start_time, 2)
            function_name = func.__name__
            if template:
                message = template.format(execution_time)
            else:
                message = f'{function_name} - {execution_time}с!'
            print(message)
            return result

        return wrapper

    return decorator


@click.group()
def cli():
    """Command-line интерфейс для заказа пиццы."""
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L', type=click.Choice(['L', 'XL']))
@click.argument('pizza_type', nargs=1)
def order(pizza_type, delivery, size):
    """Готовит и доставляет пиццу"""
    pizza_type = pizza_type.lower()
    if pizza_type == 'margherita':
        pizza = Margherita(size=size)
    elif pizza_type == 'pepperoni':
        pizza = Pepperoni(size=size)
    elif pizza_type == 'hawaiian':
        pizza = Hawaiian(size=size)
    else:
        click.echo('Извините, такой пиццы у нас нет.')
        return
    preparation_time = 2 if pizza.size == 'L' else 4
    delivery_time = 1
    click.echo(f'👩‍🍳 Приготовили за {preparation_time}с!')
    if delivery:
        click.echo(f'🛵 Доставили за {delivery_time}с!')


@cli.command()
def menu():
    """Выводит меню"""
    margherita = Margherita('L/XL')
    pepperoni = Pepperoni('L/XL')
    hawaiian = Hawaiian('L/XL')
    click.echo('Меню:\n')
    for pizza in [margherita, pepperoni, hawaiian]:
        click.echo(f'{pizza.name}:')
        click.echo(f'Размеры - {pizza.size}')
        for ingredient in pizza.ingredients:
            click.echo(f'- {ingredient}')


@log_time()
def bake(pizza):
    """Готовит пиццу"""
    time.sleep(2)
    return f'{bake.__name__} - готово'


@log_time('Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""
    time.sleep(1)
    return f'{delivery.__name__} - доставлено'


@log_time('Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    time.sleep(1)
    return f'{pickup.__name__} - забрано'


# Тесты
def test_bake_margherita_xl():
    assert bake(Margherita('XL')) == 'bake - готово'


def test_delivery_pepperoni_l():
    assert delivery(Pepperoni('L')) == 'delivery - доставлено'


def test_pickup_hawaiian_xl():
    assert pickup(Hawaiian('XL')) == 'pickup - забрано'


if __name__ == '__main__':
    cli()
