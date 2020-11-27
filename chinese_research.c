int* gacha(int *pulls,int length,int *dist){

    double rate4 = 0.051;

    double rate5 = 0.006;

    static int count4 = 0;

    static int count5 = 0;

    static int* rewardList = NULL;

    int reward4 = 0;

    int reward5 = 0;

    int reward = 0;

    int threshold4 = 8;

    double rate4up = 0.511;

    int threshold5 = 75;

    double rate5up = 0.324;

    double rand;

    int t,tt;

    if(rewardList == NULL){

        rewardList = (int*)malloc((length+1)*sizeof(int));

    }

    if(length > 1){

        count4 = 0;

        count5 = 0;

    }

    for(t = 0,tt = 0;tt < length;tt++){
        for(;t < pulls[tt];t++){
            rand = mt19937();
            if(count5 < threshold5)
                if(rand < rate5)
                    reward = 5;
                else
                    if(count4 < threshold4)
                        if(rand < rate5+rate4)
                            reward = 4;
                        else
                            reward = 0;
                    else if(count4 < 9)
                        if(rand < rate5+rate4up)
                            reward = 4;
                        else
                            reward = 0;
                    else
                        reward = 4;
            else if(count5 < 89)
                if(rand < rate5up)
                    reward = 5;
                else
                    if(count4 < threshold4)
                        if(rand < rate5up+rate4)
                            reward = 4;
                        else
                            reward = 0;
                    else if(count4 < 9)
                        if(rand < rate5up+rate4up)
                            reward = 4;
                        else
                            reward = 0;
                    else
                        reward = 4;
            else
                reward = 5;

            if(reward == 5){
                reward5++;

                dist[count5]++;

                count4++;

                count5 = 0;

            }

            else if(reward == 4){

                reward4++;

                count4 = 0;

                count5++;

            }

            else{

                count4++;

                count5++;

            }

        }

        rewardList[0] = reward4;

        rewardList[tt+1] = reward5;

    }

    return rewardList;

}



int ratedistribution(){

    int t = 0;

    int reward4 = 0;

    int reward5 = 0;

    int dist[90] = {0};

    int dist45[10] = {0};

    int dist5[10] = {0};

    int dist04[10] = {0};

    int* reward;

    int pulls = 1000000000;

    int pull10 = 10;

    while(t < pulls){

        t++;

        reward = gacha(&pull10,1,dist);

        reward4 += *reward;

        reward5 += *(reward+1);

        dist5[*(reward+1)]++;

        dist45[*(reward)+*(reward+1)-1]++;

        if(*reward == 0)

            dist04[*(reward+1)]++;

    }

    printf("\n4-star items: %d average rate including pity: %lf%%\n", reward4,(double)reward4/pulls*10);

    printf("5-star items: %d  average rate including pity: %lf%%\n\n", reward5,(double)reward5/pulls*10);

    printf("5-star items distribution\n");

    for(t = 0;t < 18;t++)

        printf("%2d-%2d: %.2lf%%\n",5*t+1,5*t+5,(double)(dist[5*t]+dist[5*t+1]+dist[5*t+2]+dist[5*t+3]+dist[5*t+4])/reward5*100);

    printf("\n");

    for(t = 0;t < 90;t++){

        printf("%2d: %.3lf%%",t+1,(double)dist[t]/reward5*100);

        if((t+1)%5 == 0)

            printf("\n");

        else

            printf("\t");

    }

    printf("\n");

    printf("multi-5-star rates in 10-pull\n");

    for(t = 0;t < 10;t++){

        printf("%d: %9d  rate: %lf%%",t,dist5[t],(double)dist5[t]/pulls*100);

        if(t > 1)

            printf(" ");

        printf("  without 4-star: %9d  rate: %lf%%\n",dist04[t],(double)dist04[t]/dist5[t]*100);

    }

    printf("\n");

    printf("no 4-star rate totally: %lf%%\n",(double)(dist04[1]+dist04[2]+dist04[3]+dist04[4]+dist04[5])/(dist5[0]+dist5[1]+dist5[2]+dist5[3]+dist5[4]+dist5[5])*100);

    printf("\n");

    printf("multi-4&5-star rates in 10-pull\n");

    for(t = 0;t < 10;t++)

        printf("%2d: %9d  rate: %lf%%\n",t+1,dist45[t],(double)dist45[t]/pulls*100);

    printf("\n");

    return 0;

}



int rateaverage(){

    int t = 0;

    int reward5 = 0;

    int dist[90] = {0};

    int dist5[4][200] = {0};

    int average[4][101] = {0};

    int* reward;

    int players = 1000000;

    int pulls[4] = {300,1000,3000,10000};

    int tt,i;

    while(t < players){

        t++;

        reward = gacha(pulls,4,dist);

        reward5 += *(reward+4);

        for(tt = 0;tt < 4;tt++)

            dist5[tt][*(reward+tt+1)]++;

    }

    for(t = 0;t < 200;t++){

        for(tt = 0;tt < 4;tt++){

            if(t > 0 && pulls[tt]/t < 101)

                if(pulls[tt] - pulls[tt]/t*t > 0)

                    average[tt][pulls[tt]/t+1] += dist5[tt][t];

                else

                    average[tt][pulls[tt]/t] += dist5[tt][t];

        }

    }

    printf("\n");

    printf("  pulls:     300     1000     3000    10000\n");

    for(t = 0;t < 20;t++){

        printf("%2d ~%3d:  ",5*t+1,5*t+5);

        for(tt = 0;tt < 4;tt++){

            i = average[tt][5*t+1]+average[tt][5*t+2]+average[tt][5*t+3]+average[tt][5*t+4]+average[tt][5*t+5];

            if(i == 0)

                printf("     -");

            else{

                if(i*100/players > 9)

                    printf("%.2lf%%",(double)i/players*100);

                else

                    printf(" %.2lf%%",(double)i/players*100);

            }

            if(tt == 3)

                printf("\n");

            else

                printf("   ");

        }



    }

    printf("\n");

    return 0;

}