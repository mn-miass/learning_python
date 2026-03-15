def list_comprehension(data: list) -> None:
    print("=== List Comprehension Examples ===")
    high_score = [player['name'] for player in data if player['score'] > 2000]
    print(f"High scorers (>2000): {high_score}")
    double = [player['score'] * 2 for player in data]
    print(f"Scores doubled: {double}")
    active = [player['name'] for player in data if player['state'] != 'logout']
    print(f"Active players: {active}\n")


def dict_comprehension(data: list) -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {
        player['name']: player['score'] for player in data
        }
    print(f"Player scores: {player_scores}")
    categorys = [player['category'] for player in data]
    score_category = {
        category: categorys.count(category) for category in categorys
        }
    print(f"Score categorys: {score_category}")
    achievements = {
        player['name']: player['achievements'] for player in data
        }
    print(f"Achievement counts: {achievements}\n")


def set_comprehension(data: list) -> None:
    print("=== Set Comprehension Examples ===")
    unique_player = {player['name'] for player in data}
    print(f"Unique players: {unique_player}")
    unique_achievements = {x for player in data
                           for x in player['achievement_name']}
    print(f"Unique achievements: {unique_achievements}")
    active_region = {player['region'] for player in data}
    print(f"Active regions: {active_region}\n")


def analyze(data: list) -> None:
    print("=== Combined analyzeis ===")
    players = {player['name'] for player in data}
    print(f"Total players: {len(players)}")
    achievements = {x for player in data for x in player['achievement_name']}
    print(f"Total unique achievements: {len(achievements)}")
    average = sum([player['score'] for player in data])/len(data)
    print(f"Average score: {average}")
    scores = [player['score'] for player in data]
    top = [player for player in data if player['score'] == max(scores)]
    print(f"Top performer: {top[0]['name']} "
          f"({top[0]['score']} points, {top[0]['achievements']})")


if __name__ == "__main__":
    players = [
        {'name': 'alice', 'score': 2300, 'achievements': 4, 'region': 'north',
         'category': 'high', 'state': 'logout',
         'achievement_name': ['collector', 'perfectionist',
                              'treasure_hunter', 'speed_demon']},
        {'name': 'bob', 'score': 1800, 'achievements': 3, 'region': 'east',
         'category': 'mid', 'state': 'login',
         'achievement_name': ['first_kill', 'level_10', 'treasure_hunter']},
        {'name': 'charlie', 'score': 2150, 'achievements': 0,
         'region': 'north',
         'category': 'high', 'state': 'login', 'achievement_name': []},
        {'name': 'diana', 'score': 900, 'achievements': 2, 'region': 'central',
         'category': 'low', 'state': 'logout',
         'achievement_name': ['treasure_hunter', 'speed_demon']},
        {'name': 'eve', 'score': 2050, 'achievements': 6, 'region': 'east',
         'category': 'mid', 'state': 'logout',
         'achievement_name': ['first_kill', 'level_10', 'boss_slayer',
                              'collector', 'speed_demon', 'treasure_hunter']},
        {'name': 'frank', 'score': 400, 'achievements': 1, 'region': 'central',
         'category': 'low', 'state': 'logout',
         'achievement_name': ['boss_slayer']},
         ]

    print("=== Game Analytics Dashboard ===\n")
    list_comprehension(players)
    dict_comprehension(players)
    set_comprehension(players)
    analyze(players)
