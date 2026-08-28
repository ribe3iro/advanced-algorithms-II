#include<bits/stdc++.h>

using namespace std;

const double EPSILON = 1e-8;
const double MAX_HP = 1000;

bool explore_dungeon(double health_points, vector<pair<string, double>> events){
    for(auto [event, argument] : events){
        if(health_points <= EPSILON){
            return false;
        }

        if(event == "DMG"){
            health_points -= argument;
        } else if(event == "POISON"){
            health_points = health_points * (1 - argument);
        } else if(event == "HEAL"){
            health_points = health_points + argument;
            health_points = min(health_points, MAX_HP);
        } else if(event == "BLESS"){
            health_points = health_points * (argument + 1);
            health_points = min(health_points, MAX_HP);
        }
    }

    return health_points > EPSILON;
}

int main(){
    int T;
    cin >> T;

    for(int i=0; i<T; i++){
        int E;
        cin >> E;

        vector<pair<string, double>> events;
        for(int j=0; j<E; j++){
            string event;
            double argument;
            cin >> event >> argument;

            events.push_back(make_pair(event, argument));
        }

        double health_points = 1e-3;
        while(!explore_dungeon(health_points, events)){
            health_points += 1e-3;
        }

        health_points = round(health_points * 1000.0) / 1000.0;

        if(!explore_dungeon(health_points, events)){
            health_points += 1e-3;
        }

        printf("%.3f\n", health_points);
    }

    return 0;
}
