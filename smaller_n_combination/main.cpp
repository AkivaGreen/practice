#include <iostream>
#include <vector>
#include <cmath>

#define DECIMAL 10.0

using namespace std;

void smaller_n_combination(int n);
int convertVectorInt(vector<int> int_vector);
void swap(int &a, int &b);
vector<int> bubbleSort(vector<int> vect);

int main(){
  int n;
  char end;
  cout << "Enter a number: ";
  cin >> n;
  smaller_n_combination(n);
  cout << "Enter any key to close the program: \n";
  cin >> end;
}

void smaller_n_combination(int n){
  int digits = 0, index = 0;
  vector<int> n_vector, n_sorted, smaller_n;
  while((n / (int)pow(DECIMAL, (double)digits)) > 0){
    int temp = (n / (int)pow(DECIMAL, (double)digits)) % 10;
    n_vector.insert(n_vector.begin(), temp);
    digits++;
  }
  n_sorted = bubbleSort(n_vector);
  //* Print n vector
  for(unsigned i = 0; i < n_sorted.size(); i++){
    cout << n_sorted[i] << ", ";
  }
  //*/
  /* main while loop
  while(smaller_n.size() < digits){

  }
  */
}

int convertVectorInt(vector<int> int_vector){

}

void swap(int &a, int &b){
  int temp = a;
  a = b;
  b = temp;
}

vector<int> bubbleSort(vector<int> vect){
  unsigned i, j, n = vect.size();
  bool swapped;
  for (i = 0; i < n-1; i++){
   swapped = false;
   for (j = 0; j < n-i-1; j++){
      if (vect[j] > vect[j+1]){
        swap(vect[j], vect[j+1]);
        swapped = true;
      }
   }

   // IF no two elements were swapped by inner loop, then break
   if (swapped == false){
     break;
   }
   return vect;
  }
}
