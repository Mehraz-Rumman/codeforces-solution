#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int INF=2e9+10;
#define mod 1000000007
const int BIT=25;
const int N=2e5+5;
int has[N][BIT];


void solve()
{

ll n;
cin>>n;
vector<ll> v;
ll sum=0;
for(int i=0;i<n;i++)
{
	ll t;
	cin>>t;
	v.push_back(t);
	sum=(sum+t);
}
sort(v.begin(),v.end());
ll m;
cin>>m;
while(m--)
{
	ll x,y;
	cin>>x>>y;

int i=lower_bound(v.begin(),v.end(),x)-v.begin();
ll ans=2e18;

if(i>0)
{
	ans=min(ans,(x-v[i-1]))+max(0LL,y-sum+v[i-1]);

}
if(i<n)
{
	ans=min(ans,max(0LL,y-sum+v[i]));
}
cout<<ans<<endl;


}

} 
int main()
{
 
#ifndef ONLINE_JUDGE
 
    freopen("input.txt", "r", stdin);
 
    freopen("output.txt", "w", stdout);
   
#endif
    ios::sync_with_stdio(false); cin.tie(0);cout.tie(0);

   {
 
solve();
 
  }


}
