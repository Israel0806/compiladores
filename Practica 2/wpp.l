	char *horastr[100], *horariostr[100], *fechastr[100], *mensajestr[100], *nombrestr[100];
	int mensajes = 0;
digito [0-9]
entero {digito}+
hora {entero}:{entero}
horario "p. m."|"a. m."
fecha {entero}\/{entero}\/{entero}
letra [a-zA-Zñ]
cEspecial [\=\!\¡\?\¿\)\(\/\"\%]
palabra ({letra}|{cEspecial})+
nombre "] "{palabra}({palabra}|" "|",")+":"
mensaje {palabra}({palabra}|" "|",")+.$

%%

{hora} { horastr[mensajes] = strdup(yytext); }
{horario} { horariostr[mensajes] = strdup(yytext); }
{fecha} { fechastr[mensajes] = strdup(yytext); }
{nombre} { nombrestr[mensajes] = strdup(yytext);}
{mensaje} { mensajestr[mensajes] = yytext;}
\n {mensajes++;}
. 
%%
#include <string.h>

int main() {
	yylex();
	int i = 0, j;
	printf("Number of messages: %i\n", mensajes);
	for(; i < mensajes; ++i) {
		j = 2;
		*(*(nombrestr+i)+0) = ' ';
		*(*(nombrestr+i)+1) = ' ';
		while(*(*(nombrestr+i)+j) != '\0') {
			if (*(*(nombrestr+i)+j) == ':') {
				*(*(nombrestr+i)+j) = '\0';
				break;
			}
			*(*(nombrestr+i)+j) = *(*(nombrestr+i)+j);
			++j;
		}
		j = 0;
		while(1) {
			if(*(*(mensajestr+i)+j) == '\n') {
				*(*(mensajestr+i)+j) = '\0';
				break;
			}
			if(*(*(mensajestr+i)+j) == '\0') {
				break;
			}
			++j;
		}
		printf("\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|}\\hline\n");
		printf("%i & \n",i+1);
		printf(" \\textsc{%s}&\n",nombrestr[i]);
		printf("\r%s\n",mensajestr[i]);
		printf(" &\n");
		printf("\\begin{tabular}{c}\n");
		printf("\t\\footnotesize{%s} \\\\\n",fechastr[i]);
		printf("\t\\Large{\\textbf{%s}} \\\\\n",horastr[i]);
		printf("\t%s\n",horariostr[i]);
		printf(" \\end{tabular} \\\\\n");
		printf("\\hline\n");
		printf("\\end{tabular}\n\n\n");
	}
}
