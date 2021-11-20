#include<bits/stdc++.h>
#define maxN 7000
typedef long double ld;
using namespace std;
const int sz=12;
unordered_map<int,int> mp;
unordered_map<int,unordered_map<int,ld>> dp;
struct node{
    ld w[sz];
}artist[maxN];
int n,m;
ld score[2];
ld dis[sz];
ld cal1(int u,int v)
{
    if(dp.find(u)==dp.end()||dp[u].find(v)==dp[u].end()){
        ld sum=0;
        for(int i=0;i<sz;++i) sum+=(artist[u].w[i]-artist[v].w[i])*(artist[u].w[i]-artist[v].w[i]);
        if(sum==0) return 0;
        return sqrt(sum/sz);
    }
    else return dp[u][v];
}
ld cal2(int u,int v)
{
    ld w=0;
    int cnt=0;
    for(int i=0;i<n;++i){
        if(i==u||i==v) continue;
        ld tmp=cal1(v,i);
        if(tmp!=0){
            w+=tmp;
            cnt+=1;
        }
    }
    return w/cnt;
}
void cal3(int u,int v)
{
    for(int i=0;i<sz;++i){
        dis[i]+=(artist[u].w[i]-artist[v].w[i])*(artist[u].w[i]-artist[v].w[i]);
    }
}
int main()
{
    freopen("artist_pd.txt","r+",stdin);
    cin>>n;
    for(int i=0;i<n;++i){
        ld id;cin>>id;
        mp[int(id)]=i;id=mp[id];
        for(int j=0;j<sz;++j) cin>>artist[i].w[j];
    }
    freopen("influence_pd.txt","r+",stdin);
    cin>>m;
    // int cnt=0;
    // for(int i=0;i<m;++i){
    //     if(i%1000==0) cout<<i<<"\n";
    //     int u,v;cin>>u>>v;
    //     if(mp.find(v)==mp.end()) {
    //         cnt++;
    //         continue;
    //     }
    //     u=mp[u];v=mp[v];
    //     score[0]+=cal1(u,v);
    //     score[1]+=cal2(u,v);
    // }
    // cout<<cnt<<"\n";
    for(int i=0;i<m;++i){
        int u,v;cin>>u>>v;
        // cout<<"in:"<<u<<" "<<v<<"\n";
        if(mp.find(v)==mp.end()) continue;
        u=mp[u];v=mp[v];
        cal3(u,v);
        // break;
    }
    for(int i=0;i<sz;++i) cout<<dis[i]<<",";
    // cout<<fixed<<score[0]<<"\n"<<score[1]<<"\n";
}