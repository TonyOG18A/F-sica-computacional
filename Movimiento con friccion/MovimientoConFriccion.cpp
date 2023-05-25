#include<iostream>
#include<fstream>

using namespace std;
int main(){
	long double v_0=0, t_0=0, v_n=v_0, v_mej=v_0,  v_aux=v_0, a=10, b=1, h=0.05;
	
	ofstream file_plot;
	file_plot.open("Datos.dat");
	file_plot<<t_0<<" "<<v_0<<endl;
		
	for(double t=t_0+h;t<=10;t+=h){
		v_n=v_aux+h*(a-b*v_aux);
		v_mej=v_aux+(h/2)*(2*a-b*(v_n+v_aux));
		v_aux=v_mej;
		file_plot<<t<<" "<<v_mej<<endl;
	}
	file_plot.close();
	FILE*vent=popen("gnuplot -persist","w");
	fprintf(vent, "load \"ConfiguracionDeGraficas.txt\" \n");
	return 0;
}
