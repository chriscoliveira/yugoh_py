import requests
import json
import yugioh
from googletrans import Translator
from googletrans.gtoken import TokenAcquirer


id = '6983839'


def retorna_info(id):
    res = json.loads(requests.get(
        f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={id}').text)
    # print(res)
    card_name = res['data'][0]['name']
    card_type = res['data'][0]['type']
    card_desc = res['data'][0]['desc']
    card_atk = res['data'][0]['atk']
    card_def = res['data'][0]['def']
    card_level = res['data'][0]['level']
    card_race = res['data'][0]['race']
    card_attribute = res['data'][0]['attribute']

    card_images = res['data'][0]['card_images'][0]['image_url']

    return card_name, card_type, card_atk, card_def, card_level, card_desc, card_attribute, card_race, card_images


def batalha(card_atk, card_def):
    atk_name, atk_type, atk_atk, atk_def, atk_level, atk_desc, atk_attribute, atk_race, atk_images = retorna_info(
        card_atk)
    def_name, def_type, def_def, def_def, def_level, def_desc, def_attribute, def_race, def_images = retorna_info(
        card_def)
    if atk_atk > def_def:
        print(f'{atk_name} ganhou! "{atk_atk}/{def_def}"')
    elif atk_atk < def_def:
        print(f'{def_name} ganhou! "{def_def}/{atk_atk}"')
    else:
        print('empate')


batalha(6983839, 73398797)
# print(retorna_info(11714098))
