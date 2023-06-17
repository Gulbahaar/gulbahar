#include <iostream>
using namespace std;

class Hesap{
    private:
        string sahipad, sahipsoyad;
        float bakiye = 0.0f;

    public:
        void hesap_bilgilerini_ekle(){
	    string telefon, email, adres;

        cout<< "Hesap bilgilerinizi giriniz:"<< endl;

	    cout<< "Adiniz: ";
	    cin >>sahipad;

	    cout<< "Soyadiniz: ";
	    cin >>sahipsoyad;

	    cout<< "Telefon: ";
	    cin >>telefon;

	    cout<< "E-mail: ";
	    cin >>email;

	    cout<< "Adres: ";
	    cin >>adres;

        cout<< endl;
        }

        float para_yatir(float miktar){
            bakiye += miktar;
	    cout<< "Heaspiniza "<< miktar<< "TL yatirildi."<< endl;
            return bakiye;
        }

        float para_cek(float miktar){
            bakiye -= miktar;
	    cout<< "Hesapiniz'dan "<< miktar<< "TL cekildi."<< endl;
            return bakiye;
        }

        void para_aktar(Hesap& a, float miktar){
	    bakiye   -=	miktar;	
            a.bakiye += miktar;

            cout<< a.sahipad<< " "<< a.sahipsoyad<< " adli hesap sahipine "<< miktar<< " aktarildi."<< endl;
        }

        void bakiye_kontrolu(){
            cout<< "Hesap bakiyeniz: "<< bakiye<< "TL."<< endl;
        }

};


int main(){

    Hesap hesap_1;
    Hesap hesap_2;

    hesap_1.hesap_bilgilerini_ekle();
    hesap_2.hesap_bilgilerini_ekle();

    hesap_1.para_yatir(300);
    hesap_2.para_yatir(700);
    hesap_1.para_cek(150);
    hesap_1.bakiye_kontrolu();
    hesap_2.para_cek(50);
    hesap_2.bakiye_kontrolu();
    hesap_1.para_aktar(hesap_2, 180);

    return 0;
}
