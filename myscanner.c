#include <stdio.h>
#include <time.h>
#include "values.h"

extern int yylex();
extern int yylineno;
extern char* yytext;


int main (void){

	int ntoken, prevToken,  expectedIndent, i;
	int currentIndent = 0;

	double start, end;
	start=time(0);


	ntoken = yylex();
	while(ntoken){


	switch (ntoken){
            case 1:
                //The Token matched to be a Keyword
                printf( "Keyword (%s)\n", yytext);
		prevToken = ntoken;
		ntoken = yylex();
		break;
            case 2:
                //The Token matched to be a literal
                printf( "Literal (%s)\n", yytext);
		prevToken = ntoken;
		ntoken = yylex();

		break;

            case 3:
                //The Token matched to be an operator
                printf( "Operator (%s)\n", yytext);
		prevToken = ntoken;
		ntoken = yylex();
		break;

            case 4:
                //The Token matched to be an identifier
                printf( "Identifier (%s)\n", yytext);
		prevToken = ntoken;
		ntoken = yylex();
		break;

            case 5:
                //The Token matched to be a delimeter
                printf( "Delimiters (%s)\n", yytext);
		prevToken = ntoken;
		ntoken = yylex();
		break;

            case 6:
                //The Token matched to be an Indent
		++currentIndent;
		prevToken = ntoken;
		ntoken = yylex();
		break;

            case 7:
                //The Token matched to be a NewLine
		prevToken = ntoken;
		ntoken = yylex();
		if(!ntoken){
		break;
		}
		printf(  "NEWLINE\n");

		//This line is needed because in the case of an indent following an indent the following conditional would be true.
		if((expectedIndent > 0 && ntoken==6)||expectedIndent == 0){
		}
		//In a case where you are expecting an Indent and the following token is not an indent then you will go back, or dedent, the number of indents
		else if(expectedIndent > 0 && ntoken!=6){
			int temp = expectedIndent;
			for(i=0; i < temp; i++){
				printf("DEDENT\n");
				expectedIndent--;
			}
		}

		currentIndent = 0;

		break;

            default:
                //The Token didn't match anything
		printf("Syntax error in line %d\n", yylineno);

           	 }

		if(ntoken != 6 && prevToken == 6){
			for(i=0; i<currentIndent; i++){
				printf("INDENT \n");
			}
			expectedIndent = currentIndent;
		}

		}
		end = time(0);
		printf("%f\n",end-start);
		return 0;
}
