#include<bits/stdc++.h>

using namespace std;

const float EPSILON = 1e-4;
const float MAX_HP = 1000;

bool explore_dungeon(float health_points, vector<pair<string, float>> events){
    for(auto [event, argument] : events){
        if(event == "DMG"){
            health_points -= argument;
        } else if(event == "POISON"){
            health_points = health_points * (1 - argument);
        } else if(event == "HEAL"){
            health_points += argument;
        } else if(event == "BLESS"){
            health_points = health_points * (argument + 1);
        }

        if(health_points > MAX_HP){
            health_points = MAX_HP;
        }

        if(health_points <= 0){
            return false;
        }
    }

    return true;
}

int main(){
    int T;
    cin >> T;

    for(int i=0; i<T; i++){
        int E;
        cin >> E;

        vector<pair<string, float>> events;
        for(int j=0; j<E; j++){
            string event;
            float argument;
            cin >> event >> argument;

            events.push_back(make_pair(event, argument));
        }

        float upper_hp = MAX_HP;
        float bottom_hp = 0;

        float health_points, delta;
        do{
            health_points = (upper_hp + bottom_hp) / 2;
            bool success = explore_dungeon(health_points, events);
            if(success){
                upper_hp = health_points;
            } else{
                bottom_hp = health_points;
                continue;
            }
            delta = health_points - ((upper_hp + bottom_hp) / 2);
            delta = abs(delta);
        }while(!(delta < EPSILON && success));
        printf("%.3f\n", health_points+1e-3);
    }

    return 0;
}
