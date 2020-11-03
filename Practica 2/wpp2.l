digito [0-9]
entero {digito}+
hora {entero}:{entero}
horario (p\. m\.|a\. m\.)
fecha {entero}\/{entero}\/{entero}

%%

{fecha} { printf("Fecha: ["); ECHO; printf("]"); }
