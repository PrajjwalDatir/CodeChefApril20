#include<bits/stdc++.h>
  
using namespace std;

int main(){
    long T, N;
    cin >> T;
    while(T--)
    {
        cin >> N;
        long my_array[N], mul_arr[N];
        long i = 0, j = 0;
        long cnt = 0;
        long my_iter = 0;
        while(i < N)
            cin >> my_array[i++];

				//if (mul_arr[0] % 4 != 2){
				//	cnt++;
				//}
		for (i = 0; i < N; i++)
		{
			mul_arr[i] = abs(my_array[i]) % 4;
		//cout << mul_arr[i];
		}
		//cout << endl;
		
		for (my_iter = 0; my_iter < N; my_iter++){
		// cout << my_iter << endl;
			for (i = my_iter; i < N; i++)
			{
				if (mul_arr[i] == 0){
					cnt = cnt + N - i;
					break;
				}
				if (mul_arr[i] % 4 == 1){
					while ((mul_arr[i] != 2) && (i < N)){
						cnt++;
						i++;
					}
					if (i == N){
						break;
					}
				}
				if (mul_arr[i] % 4 == 3){
					while (mul_arr[i] != 2 && i < N){
						cnt++;
						i++;
					}
					if (i == N){
						break;
					}	
				}
				if (mul_arr[i] == 2){
					while (i < N - 1)
					{
						i++;
						if (mul_arr[i] == 2){
							cnt = cnt + N - i;
							break;
						}
						if (mul_arr[i] == 0){
							cnt = cnt + N - i;
							break;	
						}
					}
					break;
				}	
			}	
		}
		cout << cnt << endl;
	}
    return 0;
}
