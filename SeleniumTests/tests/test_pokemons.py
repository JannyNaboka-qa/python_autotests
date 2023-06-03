import requests
import pytest

host= 'https://pokemonbattle.me:9104'
token= 'daa7c7d4b3d934ee8cc1710a1156ad82'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 4359},
                             headers= {"Content-Type":"application/json", "trainer_token":f"{token}"})
    assert response.status_code == 200

def test_part_of_response():
    response_body = requests.get(f'{host}/trainers', params= {'trainer_id' : 4359},
                             headers= {"Content-Type":"application/json", "trainer_token":f"{token}"})
    assert response_body.json()['trainer_name'] == 'JannyN'