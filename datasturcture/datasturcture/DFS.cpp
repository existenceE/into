//
//  DFS.cpp
//  datasturcture
//
//  Created by 马晓宁 on 2018/7/7.
//  Copyright © 2018年 flowerao. All rights reserved.
//

#include "DFS.hpp"
#include <iostream>
#define maxSize 50


typedef struct ArcNode
{
    int adjvex;
    struct ArcNode *nextarc;
    int info;
}ArcNode;

typedef struct
{
    char data;
    ArcNode *firstarc;
}VNode;

typedef struct
{
    VNode adjlist[maxSize];
    int n,e;
}AGraph;

int visit[maxSize];

void Visit(int i)
{
    std::cout << i << std::endl;
}

void DFS(AGraph *G, int v)
{
    ArcNode *p;
    visit[v] = 1;
    Visit(v);
    p=G->adjlist[v].firstarc;
    while(p!=NULL){
        if(visit[p->adjvex]==0)
            DFS(G, p->adjvex);
        p=p->nextarc;
    }
    
}


