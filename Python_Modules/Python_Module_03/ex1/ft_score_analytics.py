import sys


def parse_scores() -> list:
    scores_list = []
    for score in sys.argv[1:]:
        try:
            scores_list.append(int(score))
        except ValueError:
            print(f"Oups You typed {score} instead of a number")
    return scores_list


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores_list = parse_scores()

    if scores_list:
        print(f"Scores processed: {scores_list}")
        print(f"Total players: {len(scores_list)}")
        print(f"Total score: {sum(scores_list)}")
        print(f"Average score: {sum(scores_list)/len(scores_list)}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {(max(scores_list) - min(scores_list))}\n")

    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
