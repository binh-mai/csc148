class Register:
    """ Create a Race registry, a list of runners that have signed up.

    === Attributes ===
    name: Runner's name
    email: Runner's email address
    speed: Runner's speed category

    === Sample usage ===

    Create a race registry
    >>> b = Register('Binh', 'binh.mai@mail.utoronto.ca', 'under 40 minutes')  # (name, email, speed)
    >>> b.name
    'Binh'
    >>> b.email
    'binh.mai@mail.utoronto.ca'
    >>> b.speed
    'under 40 minutes'

    Register more runners
    >>> Register('Gerhard', , 'under 40 minutes')
    >>> Register('Tom', , 'under 30 minutes')
    >>> Register('Toni', , 'under 20 minutes')
    >>> Register('Margot', , 'under 40 minutes')

    Create a race registry.
Register the following runners:
Gerhard (with time under 40 minutes)
Tom (with time under 30 minutes)
Toni (with time under 20 minutes)
Margot (with time under 30 minutes)
Gerhard again (with time under 30 minutes---he's gotten faster)
Report the runners in the speed category of under 30 minutes.
We need to be able get a list
of runners in a given speed category. We also need to be able to look up a
runner to find their speed category
    """

    # Attribute types
    name: str
    email: str
    speed: ['under 20 minutes', 'under 30
            minutes', 'under 40 minutes', 'and 40 minutes or over']

class Runner:

    """

    Create a Runner, including what they can do.

    a runner should be able to change
their email address and speed category, or withdraw from the race entirely

    Change runner's email address
    >>> b = Runner()

    Change runner's speed category

    Runner withdraw from the race

    Sorting runner into speed category

    Look up runner's speed category


    """
