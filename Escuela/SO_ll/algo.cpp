/*C++ Program to Find Strongly Connected Components in Graphs*/
#include<iostream>
#include<conio.h>
using namespace std;
struct node_info
{
    int no;
    int lv_time, st_time;
}*q = NULL;
struct node
{
    node_info *pt;
    node *next;
}*top = NULL, *p = NULL, *np = NULL;
struct node1
{
    node1 *link;
    node_info *pt1;
}*head = NULL, *m = NULL, *n = NULL, *np1 = NULL;
int c = 0;
void push(node_info *ptr)
{
    np = new node;
    np->pt = ptr;
    np->next = NULL;
    if (top == NULL)
    {
        top = np;
    }
    else
    {
        np->next = top;
        top = np;
    }
}
node_info *pop()
{
    if (top == NULL)
    {
        cout<<"underflow\n";
    }
    else
    {
        p = top;
        top = top->next;
        return(p->pt);
        delete(p);
    }
}
void store(node_info *ptr1)
{
    np1 = new node1;
    np1->pt1 = ptr1;
    np1->link = NULL;
    if (c == 0)
    {
        head = np1;
        m = head;
        m->link = NULL;
        c++;
    }
    else
    {
        m = head;
        np1->link = m;
        head = np1;
    }
}
void remove(int x)
{
    m = head;
    if ((m->pt1)->no == x)
    {
        head = head->link;
        delete(m);
    }
    else
    {
        while ((m->pt1)->no != x && m->link != NULL)
        {
            n = m;
            m = m->link;
        }
        if ((m->pt1)->no == x)
        {
            n->link = m->link;
            delete(m);
        }
        else if (m->link == NULL)
        {
            cout<<"error\n";
        }
    }
}            
void topo(int *v, int am[][10], int i)
{
    q = new node_info;
    q->no = i;
    q->st_time = c;
     push(q);
    v[i] = 1;
    for (int j = 0; j < 10; j++)
    {
        if (am[i][j] == 0  || (am[i][j] == 1 && v[j] == 1))
            continue;
        else if (am[i][j] == 1 && v[j] == 0)
        {
            c++;
            topo(v,am,j);
        }
    }
    c++;
    q = pop();
    q->lv_time = c;
    store(q);
    return;
}
void topo1(int *v, int am[][10], int i)
{
    v[i] = 1;
    remove(i);
    cout<<i<<endl;
    for (int j = 0; j < 10; j++)
    {
        if (am[i][j] == 0  || (am[i][j] == 1 && v[j] == 1))
        {
            continue;
        }
        else if (am[i][j] == 1 && v[j] == 0)
        {
            topo1(v,am,j);
        }
    }
    return;
}
int main()
{
    int v[10], am[10][10], amt[10][10];
    for (int i = 0; i < 10; i++)
        v[i] = 0;
    for (int i = 0; i < 10; i++)
    {
        cout<<"enter the values for adjacency matrix row:"<<i + 1<<endl;
        for (int j = 0; j < 10; j++)
        {
            cin>>am[i][j];
        }
    }
    topo(v, am, 0);
    for (int i = 0; i < 10; i++)
    {
        v[i] = 0;
        for (int j = 0; j < 10; j++)
            amt[j][i] = am[i][j];
    }
    while (head != NULL)
    {
        cout<<"Strongly Connected Components:\n";                 
            topo1(v, amt, (head->pt1)->no);
    }
    getch();
}
