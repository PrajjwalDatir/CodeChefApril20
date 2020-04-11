#include<bits/stdc++.h>
  
using namespace std;

int main(){
    long T, N;
    cin >> T;
    while(T--){
        cin >> N;
        long my_array[N], mul_arr[N];
        long i = 0, j = 0;
        long cnt = 0;
        while(i < N)
            cin >> my_array[i++];

				mul_arr[0] = my_array[0];
				if (mul_arr[0] % 4 != 2){
					cnt++;
				}

				for (i = 1; i < N; i++){
			        mul_arr[i] = my_array[i] * mul_arr[i - 1];
			  //mul array is right!
				}
				
				for (i = 1; i < N; i++){
					for (j = i; j < N; j++){
						if ((mul_arr[j] / mul_arr[i - 1]) % 4 != 2){
							cnt++;
						}
					}
					if (mul_arr[i] % 4 != 2){
						cnt++;
					}
				}
		cout << cnt << endl;
		}
    return 0;
}