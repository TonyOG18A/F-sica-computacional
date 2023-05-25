#include<iostream>
#include<math.h>
#include<fstream>

using namespace std;

int main(){
	int N_0=100;
	long double t_0 = 0, h = 0.05, tau = 1, t_i = 0, N_t = 0, t_aux = 0, N_aux = N_0, 	
	N_exacta = 0,N_mej = 0;
	ofstream file_plot;
	file_plot.open("Datos.dat");
	for(double i = t_0; i<=6*tau; i+=h){
		N_t = N_aux - h*(N_aux/tau);
		N_mej = N_aux -(h/(2*tau))*(N_aux+N_t);
		N_aux = N_mej;
		N_exacta = N_0*exp(-i/tau);
		file_plot<<i<<" "<<N_mej<<" "<<N_exacta<<endl;
	}
	file_plot.close();
	FILE*vent=popen("gnuplot -persist","w");
	fprintf(vent, "load \"ConfiguracionDeGraficas.txt\" \n");
	return 0;
}	

