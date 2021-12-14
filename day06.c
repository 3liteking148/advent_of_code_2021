#include <stdio.h>
#include <stdlib.h>

unsigned long int fish(int day, const int days, unsigned long int *timers){
    unsigned long int n = 0;
    if(day == days){
        for(int i=0; i<9; i++)
            n += timers[i];
        return n;
    }

    n = timers[0];
    timers[0] = timers[1];
    timers[1] = timers[2];
    timers[2] = timers[3];
    timers[3] = timers[4];
    timers[4] = timers[5];
    timers[5] = timers[6];
    timers[6] = timers[7] + n;
    timers[7] = timers[8];
    timers[8] = n;


    return fish(day+1, days, timers);
}
int main(){
    FILE* in = fopen("day6.txt", "r");
    int day;

    unsigned long int *timers = calloc(9, sizeof(unsigned long int));
    unsigned long int *timers2 = calloc(9, sizeof(unsigned long int));
    while(fscanf(in, "%d,", &day) != EOF){
        timers[day]++;
        timers2[day]++;
    }
    fclose(in);

    printf("%lu\n", fish(0, 80, timers));
    printf("%lu\n", fish(0, 256, timers2));
}
