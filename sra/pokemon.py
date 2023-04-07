import urllib.parse
import sra
import requests


class Ability:
    """
    Get Pokemon ability information
    """

    def __init__(self, ability: str):
        """
        :returns: id, name, generation, effects, description, pokemons, descriptions and raw response by attributes

        :param ability: Ability Name/ID
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
        """
        self.id, self.name, self.generation, self.effects, self.description, self.pokemons, self.descriptions, self.raw = self.__getability(
            ability)

    @staticmethod
    def __getability(ability):
        try:
            __resp = requests.get(f"https://some-random-api.ml/pokemon/abilities?ability={urllib.parse.quote_plus(ability)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            if 'error' in __resp.json():
                raise sra.exceptions.APIError(__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        id = __resp['id']
        name = __resp['name']
        generation = __resp['generation']
        effects = __resp['effects']
        description = __resp['description']
        pokemons = []
        for i in __resp['pokemons']:
            pokemons.append(f"{str(i['pokemon']).title()} ({'Hidden' if i['hidden'] == True else 'Visible'})")
        descriptions = []
        for i in __resp['descriptions']:
            descriptions.append(i['version'])
        return id, name, generation, effects, description, pokemons, descriptions, __resp


class Item:
    """
    Get Pokemon item information
    """

    def __init__(self, item: str):
        """
        :returns: id, name, effects, cost, attributes, category, sprite, descriptions and raw response by attributes

        :param item: Item Name/ID
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
        """
        self.id, self.name, self.effects, self.cost, self.attributes, self.category, self.sprite, self.descriptions, self.raw = self.__getitem(
            item)

    @staticmethod
    def __getitem(item):
        try:
            __resp = requests.get(f"https://some-random-api.ml/pokemon/items?item={urllib.parse.quote_plus(item)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            if 'error' in __resp.json():
                raise sra.exceptions.APIError(__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        id = __resp['id']
        name = __resp['name']
        effects = __resp['effects']
        cost = __resp['cost']
        attributes = [str(i).title() for i in __resp['attributes']]
        category = __resp['category']
        sprite = __resp['sprite']
        descriptions = __resp['descriptions']
        return id, name, effects, cost, attributes, category, sprite, descriptions, __resp


class Move:
    """
    Get Pokemon move information
    """

    def __init__(self, move: str):
        """
        :returns: the id, name, generation, effects, type, category, contest, pp, power, accuracy, priority, pokemon, descriptions and raw response by attributes

        :param move: Move Name/ID
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
        """
        self.id, self.name, self.generation, self.effects, self.type, self.category, self.contest, self.pp, self.power, self.accuracy, self.priority, self.pokemon, self.descriptions, self.raw = self.__getmove(
            move)

    @staticmethod
    def __getmove(move):
        try:
            __resp = requests.get(f"https://some-random-api.ml/pokemon/moves?move={urllib.parse.quote_plus(move)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            if 'error' in __resp.json():
                raise sra.exceptions.APIError(__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        id = __resp['id']
        name = __resp['name']
        generation = __resp['generation']
        effects = __resp['effects']
        type = __resp['type']
        category = __resp['category']
        contest = __resp['contest']
        pp = __resp['pp']
        power = __resp['power']
        accuracy = __resp['accuracy']
        priority = __resp['priority']
        pokemon = [str(i).title() for i in __resp['pokemon']]
        descriptions = __resp['descriptions']
        return id, name, generation, effects, type, category, contest, pp, power, accuracy, priority, pokemon, descriptions, __resp


class Pokedex:
    """
    Get Pokemon information
    """

    def __init__(self, pokemon: str):
        """
        :returns: the id, name, generation, effects, description, pokemons, descriptions and raw response by attributes

        :param pokemon: Pokemon Name
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
        """
        self.name, self.id, self.type, self.species, self.abilities, self.height, self.weight, self.base_experience, self.gender, self.egg_groups, self.stats, self.family, self.sprites, self.description, self.generation, self.raw = self.__getpokemon(
            pokemon)

    def __getpokemon(self, pokemon):
        try:
            __resp = requests.get(f"https://some-random-api.ml/pokemon/pokedex?pokemon={urllib.parse.quote_plus(pokemon)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            if 'error' in __resp.json():
                raise sra.exceptions.APIError(__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        name = __resp['name']
        id = __resp['id']
        type = __resp['type']
        species = __resp['species']
        abilities = __resp['abilities']
        height = __resp['height']
        weight = __resp['weight']
        base_experience = __resp['base_experience']
        gender = __resp['gender']
        egg_groups = __resp['egg_groups']

        class Stats:
            def __init__(self, stats_dict):
                self.raw = stats_dict
                self.hp = stats_dict['hp']
                self.attack = stats_dict['attack']
                self.defense = stats_dict['defense']
                self.sp_atk = stats_dict['sp_atk']
                self.sp_def = stats_dict['sp_def']
                self.speed = stats_dict['speed']
                self.total = stats_dict['total']

        stats = Stats(__resp['stats'])

        class Family:
            def __init__(self, family_dict):
                self.raw = family_dict
                self.evolutionStage = family_dict['evolutionStage']
                self.evolutionLine = family_dict['evolutionLine']

        family = Family(__resp['family'])

        class Sprite:
            def __init__(self, sprites_dict):
                self.raw = sprites_dict
                self.normal = sprites_dict['normal']
                self.animated = sprites_dict['animated']

        sprites = Sprite(__resp["sprites"])

        description = __resp['description']
        generation = __resp['generation']
        return name, id, type, species, abilities, height, weight, base_experience, gender, egg_groups, stats, family, sprites, description, generation, __resp
