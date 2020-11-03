	int contador = 0;

%%

[0-9]	{ contador++; }

%%

int main() {
	yylex();
	printf("Se conto: %d\n numeros", contador);
}
