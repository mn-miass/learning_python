def print_set(player: str, achievement: set) -> None:
    print(f"Player {player} achievements: {achievement}")


if __name__ == "__main__":
    alice = {'first_kill',
             'level_10',
             'treasure_hunter',
             'speed_demon'
             }

    bob = {'first_kill',
           'level_10',
           'boss_slayer',
           'collector'
           }

    charlie = {'level_10',
               'treasure_hunter',
               'boss_slayer',
               'speed_demon',
               'perfectionist'
               }

    print("=== Achievement Tracker System ===\n")

    print_set("alice", alice)
    print_set("bob", bob)
    print_set("charlie", charlie)

    print("=== Achievement Analytics ===\n")

    all_achievements = bob.union(alice).union(charlie)
    common_achievements = bob.intersection(alice).intersection(charlie)

    alice_vs_bob = bob.intersection(alice)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    only_alice = alice.difference(bob).difference(charlie)
    only_bob = bob.difference(alice).difference(charlie)
    only_charlie = charlie.difference(alice).difference(bob)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    print(f"Common to all players: {common_achievements}")
    print("Rare achievements (1 player): "
          f"{only_alice.union(only_bob).union(only_charlie)}\n")

    print(f"Alice vs Bob common: {alice_vs_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
