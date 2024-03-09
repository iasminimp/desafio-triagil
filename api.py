from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Lista para armazenar os times de Pokémons
teams = []


def get_pokemon_data(pokemon_name):
    # Consulta a pokeAPI para obter os dados do Pokémon
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            "id": pokemon_data['id'],
            "name": pokemon_data['name'],
            "weight": pokemon_data['weight'],
            "height": pokemon_data['height']
        }
    else:
        return None


def save_team_to_file(owner, pokemons):
    # Cria uma string com os dados do time
    team_data = {
        "owner": owner,
        "pokemons": []
    }

    for pokemon_name in pokemons:
        pokemon_data = get_pokemon_data(pokemon_name)
        if pokemon_data:
            team_data["pokemons"].append(pokemon_data)

    # Adiciona o time à lista de times
    teams.append(team_data)

    # Salva o time em um arquivo txt
    with open(f'teams/{owner}.txt', 'w') as file:
        file.write(str(team_data))


@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.json
    owner = data.get('user')
    pokemons = data.get('team')

    if not owner or not pokemons:
        return jsonify({'error': 'Dados incompletos.'}), 400

    save_team_to_file(owner, pokemons)

    return jsonify({'message': 'Time de Pokémon adicionado corretamente!'}), 201




@app.route('/api/teams/<string:owner>', methods=['GET'])
def get_team_by_owner(owner):
    owner_teams = []
    for team in teams:
        if team.get('owner') == owner:
            owner_teams.append({
                "owner": team.get('owner'),
                "pokemons": team.get('pokemons')
            })

    if owner_teams:
        return jsonify(owner_teams), 200
    else:
        return jsonify({'error': 'Nenhum time de Pokémon encontrado para o proprietário especificado.'}), 404


@app.route('/api/teams', methods=['GET'])
def get_all_teams():
    all_teams = {}
    for i, team in enumerate(teams, start=1):
        all_teams[str(i)] = {
            "owner": team.get('owner'),
            "pokemons": team.get('pokemons')
        }
    return jsonify(all_teams)


if __name__ == '__main__':
    # Certifica que o diretório 'teams' existe
    os.makedirs('teams', exist_ok=True)

    # Executa o servidor Flask
    app.run(host='0.0.0.0', port=3000, debug=True)