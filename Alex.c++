#include <iostream>
using namespace std;

int main(){
   int pin_code=2324;
   int guess;
   int attempts=4;
   cout<<"Type your pin code to success the code you have 4 attempts left:";
   cin>>guess;
   int length=sizeof(guess) / sizeof (int);
   while (guess!=pin_code || length>4){
    attempts-=1;
    cout<<"Type again you have "<<attempts<<" attempts left:";
    cin>>guess;
    if (attempts==0){
        cout<<"Too bad you are out of attempts";
        break;
    }
   }
   if (guess==pin_code){
    cout<<"Great this is your pin code you are success to the code";
   }
   return 0; 
}