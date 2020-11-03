real [0-9]+\.[0-9]+
digito [0-9]
entero {digito}+

%%
{entero} { ECHO;}
{real} {ECHO;}
