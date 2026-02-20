#include <iostream>
#include <string>
using namespace std;

class Batter {
public:
    string name;
    int runs, balls, fours, sixes;
    bool out;

    Batter() {
        name = "";
        runs = balls = fours = sixes = 0;
        out = false;
    }

    void addRuns(int r) {
        runs += r;
        balls++;
        if (r == 4) fours++;
        if (r == 6) sixes++;
    }

    void markOut() {
        out = true;
    }
};

class Bowler {
public:
    string name;
    int ballsBowled, runsConceded, wickets;

    Bowler() {
        name = "";
        ballsBowled = runsConceded = wickets = 0;
    }

    void bowlBall(int r) {
        ballsBowled++;
        runsConceded += r;
    }

    void addExtra(int r) {
        runsConceded += r;
    }

    void takeWicket() {
        ballsBowled++;
        wickets++;
    }

    string overs() {
        int over = ballsBowled / 6;
        int ball = ballsBowled % 6;
        return to_string(over) + "." + to_string(ball);
    }
};

class Match {
public:
    Batter batters[11];
    Bowler bowlers[5];
    int striker, nonStriker, nextBatter;
    int bowlerIndex;
    int totalRuns, wickets, balls, maxOvers;

    Match(string battingTeam[], string bowlingTeam[], int overs) {
        for (int i = 0; i < 11; i++) {
            batters[i].name = battingTeam[i];
        }
        for (int i = 0; i < 5; i++) {
            bowlers[i].name = bowlingTeam[i];
        }
        striker = 0;
        nonStriker = 1;
        nextBatter = 2;
        bowlerIndex = 0;
        totalRuns = wickets = balls = 0;
        maxOvers = overs;
    }

    void swapStrike() {
        int temp = striker;
        striker = nonStriker;
        nonStriker = temp;
    }

    void printScoreboard() {
        cout << "
========== SCOREBOARD ==========
";
        cout << "Score: " << totalRuns << "/" << wickets
             << "  Overs: " << (balls / 6) << "." << (balls % 6) << "/" << maxOvers << "

";
        cout << "Batting:
";
        for (int i = 0; i < 11; i++) {
            if (i == striker)
                cout << batters[i].name << "* " << batters[i].runs << "(" << batters[i].balls << ")
";
            else if (i == nonStriker)
                cout << batters[i].name << " " << batters[i].runs << "(" << batters[i].balls << ")
";
            else if (batters[i].balls > 0 || batters[i].out)
                cout << batters[i].name << " " << batters[i].runs << "(" << batters[i].balls << ")"
                     << (batters[i].out ? " OUT" : "") << "
";
        }

        cout << "
Bowling:
";
        for (int i = 0; i < 5; i++) {
            if (bowlers[i].ballsBowled > 0)
                cout << bowlers[i].name << " - " << bowlers[i].overs()
                     << "  Runs:" << bowlers[i].runsConceded
                     << "  Wkts:" << bowlers[i].wickets << "
";
        }
        cout << "================================
";
    }

    void processBall(string event) {
        Bowler &bowler = bowlers[bowlerIndex];
        if (event == "W") {
            bowler.takeWicket();
            batters[striker].markOut();
            wickets++;
            balls++;
            if (wickets == 10) return;
            striker = nextBatter++;
        }
        else if (event == "WD" || event == "NB") {
            bowler.addExtra(1);
            totalRuns++;
            // Don't increment balls for illegal delivery
            return;
        }
        else {
            int runs = stoi(event);
            batters[striker].addRuns(runs);
            bowler.bowlBall(runs);
            totalRuns += runs;
            balls++;
            if (runs % 2 != 0) swapStrike();
        }
    }

    void simulate(int target = -1) {
        string event;
        while (balls / 6 < maxOvers && wickets < 10) {
            if (target != -1 && totalRuns >= target) break; // target chase condition

            printScoreboard();

            cout << "Select bowler for this over (0-4): ";
            for (int i = 0; i < 5; i++)
                cout << i << ": " << bowlers[i].name << "  ";
            cout << "
Your choice: ";
            cin >> bowlerIndex;
            if (bowlerIndex < 0 || bowlerIndex > 4) {
                cout << "Invalid index. Defaulting to 0.
";
                bowlerIndex = 0;
            }

            cout << "Enter 6 ball results for this over (e.g. 1 0 4 W WD 6):
";
            for (int i = 0; i < 6 && balls / 6 < maxOvers && wickets < 10; ) {
                if (target != -1 && totalRuns >= target) break;
                cin >> event;
                processBall(event);
                // Only increment i on legal ball (not WD or NB)
                if (event != "WD" && event != "NB")
                    i++;
                if (wickets == 10)
                    break;
            }
            if (target == -1 || totalRuns < target)  // swap strike only if innings isn't over
                swapStrike();
        }
        cout << "
🏁 INNINGS COMPLETE!
";
        printScoreboard();
    }
};

int main() {
    string teamA[11] = {
        "Rohit", "Gill", "Kohli", "Iyer", "Rahul",
        "Hardik", "Jadeja", "Ashwin", "Shami", "Bumrah", "Siraj"
    };
    string teamB[11] = {
        "Warner", "Head", "Marsh", "Smith", "Labuschagne",
        "Carey", "Stoinis", "Starc", "Cummins", "Hazlewood", "Zampa"
    };
    string bowlersA[5] = {"Starc", "Cummins", "Hazlewood", "Zampa", "Stoinis"};
    string bowlersB[5] = {"Shami", "Bumrah", "Siraj", "Hardik", "Jadeja"};

    int overs;
    cout << "Enter number of overs: ";
    cin >> overs;

    cout << "
--- FIRST INNINGS ---
";
    Match firstInnings(teamA, bowlersA, overs);
    firstInnings.simulate();

    int target = firstInnings.totalRuns + 1;

    cout << "
--- SECOND INNINGS ---
";
    Match secondInnings(teamB, bowlersB, overs);
    secondInnings.simulate(target);

    cout << "
--- MATCH RESULT ---
";
    if (secondInnings.totalRuns >= target) {
        int ballsLeft = overs * 6 - secondInnings.balls;
        cout << "Team B wins by " << (11 - secondInnings.wickets)
             << " wickets and " << ballsLeft << " balls remaining!
";
    } else if (secondInnings.totalRuns == firstInnings.totalRuns) {
        cout << "Match Tied!
";
    } else {
        cout << "Team A wins by " << (target - secondInnings.totalRuns - 1)
             << " runs!
";
    }

    return 0;
}