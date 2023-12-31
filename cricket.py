import random

def play_cricket():
    user_score = 0
    user_wickets = 0

    for over in range(1, 6):  # 5 overs per inning
        print(f"Over {over} - User's Turn")
        for ball in range(1, 7):
            user_choice = input(f"Ball {ball}: Enter 'h' to hit the ball: ").strip().lower()
            ai_bowler_actions = {"out": 0, "dot": 0, "1": 1, "2": 2, "4": 4, "6": 6}
            ai_bowler_action = random.choice(list(ai_bowler_actions.keys()))
            
            if user_choice == "h":
                if ai_bowler_action == "out":
                    print("You're out!")
                    user_wickets += 1
                else:
                    runs = ai_bowler_actions[ai_bowler_action]
                    user_score += runs
                    print(f"You scored {runs} runs!")
            else:
                print("You missed the ball.")

        print(f"User's Score after over {over}: {user_score}/{user_wickets}")

    print("AI's Turn")
    ai_score = 0
    ai_wickets = 0

    for over in range(1, 6):
        print(f"Over {over} - User's Turn")
        for ball in range(1, 7):
            user_choice = input(f"Ball {ball}: Enter 'b' to bowl: ").strip().lower()
            ai_batter_actions = {"out": 0, "dot": 0, "1": 1, "2": 2, "4": 4, "6": 6}
            ai_batter_action = random.choice(list(ai_batter_actions.keys()))
            
            if user_choice == "b":
                if ai_batter_action == "out":
                    print("wicket!")
                    ai_wickets += 1
                else:
                    runs = ai_batter_actions[ai_batter_action]
                    ai_score += runs
                    print(f"AT scored {runs} runs!")
            else:
                ai_score += 6
                print("its a six.")

        print(f"AI Score after over {over}: {ai_score}/{ai_wickets}")


    print("Match Over")
    if user_score > ai_score:
        print("You win!")
    elif user_score < ai_score:
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to the Text-Based Cricket Game")
    play_cricket()
