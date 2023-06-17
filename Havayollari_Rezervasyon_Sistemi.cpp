#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	
	while(1==1){
		
		int sinif_secin;
		int first_class_koltuk_numarasi[5]={0};
		int economy_class_koltuk_numarasi[5]={0};
		int first_toplam=5;
		int economy_toplam=5;
		
		cout<<"first class sinifi icin 1 e basin"<<endl<<"economy sinifi icin 2 ye basin"<<endl;
		cin>>sinif_secin;
		switch(sinif_secin){
		
			case 1:
				cout << "First Class paketi tercih edildi";
				for(int i=0;i<5;i++)
				{
					cout<<"\n"<<"first class sinifindan koltuk numarasi secin:";
					cin>>first_class_koltuk_numarasi[i];
            		if(first_class_koltuk_numarasi[i]>=1 && first_class_koltuk_numarasi[i]<6 && first_class_koltuk_numarasi[first_class_koltuk_numarasi[i]] == 0)
					{ 
                		first_class_koltuk_numarasi[first_class_koltuk_numarasi[i]] = 1;
						cout<<"\n"<<"First class sinifindan" << " " << first_class_koltuk_numarasi[i] << " " << "numarali koltugu aldiniz.";

                		first_toplam-=1;            
                		cout<<"\n"<<"kalan toplam koltuk sayisi:"<< first_toplam;
                		if(first_toplam == 0)
						{
                    		cout<<"\n"<<"Koltuk kalmadi,economy sinifindan alabilirsiniz.";
                    		return 0;
						}
                		else
						{
                    		cout<<"\n"<<"Ýsleminiz basariyla gerceklesti.";
                		}					
					}
            		else 
					{
                		cout << "\n" << "Koltuk dolu veya gecersiz numara girdiniz";
                		i--;
            		}
				}
			case 2:
				for(int i=0;i<5;i++)
				{
					cout<<"Economy sinifindan koltuk numarasi girin:";
					cin>>economy_class_koltuk_numarasi[i];
					if(6<=economy_class_koltuk_numarasi[i] && economy_class_koltuk_numarasi[i]<11 && economy_class_koltuk_numarasi[economy_class_koltuk_numarasi[i]-1] == 0)
					{
						economy_class_koltuk_numarasi[economy_class_koltuk_numarasi[i]-1] = 1;
						cout<<"\n"<<"economy sinifindan" << " " << economy_class_koltuk_numarasi[i] << " " << "numarali koltugu aldiniz.";
                		economy_toplam-=1;
               			cout<<"\n"<<"Kalan toplam koltuk sayisi:"<< economy_toplam;
                		if(economy_toplam == 0)
						{
                    		cout<<"\n"<<"koltuk kalmadi,first class sinifindan alabilirsiniz.";
                    		return 0;
                		}
                		else
						{
                    		cout<<"\n"<<"isleminiz basariyla gerceklesti.";
               			}

            		} 
					else 
					{
                		cout << "\n" << "Koltuk dolu veya gecersiz numara girdiniz.\n";
                		i--;
					}
				}
		}	
	}
	return 0;
}
