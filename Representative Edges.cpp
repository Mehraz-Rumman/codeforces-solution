#include <bits/stdc++.h>

using namespace std;

void solve(){
int n;
cin>>n;
vector<float> v(n);
for(float &i:v) cin>>i;
if(n<3) {
    cout<<0<<endl;
    return ;
}
int ans=2;
for(int i=0;i<n;i++){
for(int j=i+1;j<n;j++){
    float d=(v[j]-v[i]);
    int r=1;
    for(int k=j;k<n;k++){
      if(v[k]==v[j]+d*(k-j)/(j-i)) r++;
    }
    ans=max(ans,r);
}
}
cout<<n-ans<<endl;
}

int main()
{
    int t;
    cin>>t;
    while(t--) solve();
    return 0;
}
