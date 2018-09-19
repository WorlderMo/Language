# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

long long dp(int m,vector<int> &c){
    vector<long long> nums(m+1,0);
    for(int i:c){
        if (i>m)
            continue;
        for(int j = m;j>=1;j--){
            if(nums[j]>0&&j+i<=m)
                nums[j+i] += nums[j];
        }
        nums[i]++;
    }
    return nums[m];
}

int main(){
    int n,sum;
    cin>>n>>sum;
    vector<int> candidates(n,0);
    for(int i = 0;i<n;i++){
        scanf("%d",&candidates[i]);
    }
    cout<<dp(sum,candidates);
}
