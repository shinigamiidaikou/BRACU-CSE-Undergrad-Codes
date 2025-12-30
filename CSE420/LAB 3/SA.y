%{

#include "symbol_table.h"

#define YYSTYPE symbol_info*

extern FILE *yyin;
int yyparse(void);
int yylex(void);
extern YYSTYPE yylval;

// create your symbol table here.
// You can store the pointer to your symbol table in a global variable
// or you can create an object
symbol_table* sym_table;

int lines = 1;
int errors = 0;

ofstream outlog;
ofstream errorlog;

// you may declare other necessary variables here to store necessary info
// such as current variable type, variable list, function name, return type, function parameter types, parameters names etc.

vector<symbol_info*> var_list;
vector<symbol_info*> arg_list;
symbol_info* func_symbol;
symbol_info* temp_sym;

#define logg(x) do { outlog << x; errorlog << x; } while(0)

void yyerror(char *s)
{
	outlog<<"At line "<<lines<<" "<<s<<endl<<endl;

    // you may need to reinitialize variables if you find an error
	var_list.clear();
	func_symbol = nullptr;
	temp_sym = nullptr;
}

%}

%token IF ELSE FOR WHILE DO BREAK INT CHAR FLOAT DOUBLE VOID RETURN SWITCH CASE DEFAULT CONTINUE PRINTLN ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN RPAREN LCURL RCURL LTHIRD RTHIRD COMMA SEMICOLON CONST_INT CONST_FLOAT ID

%nonassoc LOWER_THAN_ELSE
%nonassoc ELSE

%%

start : program
		{
			outlog<<"At line no: "<<lines<<" start : program "<<endl<<endl;
			outlog<<"Symbol Table"<<endl<<endl;

			// Print your whole symbol table here
			sym_table->print_all_scopes(outlog);
		}
		;

program : program unit
		{
			outlog<<"At line no: "<<lines<<" program : program unit "<<endl<<endl;
			outlog<<$1->get_name()+"\n"+$2->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"\n"+$2->get_name(),"program");
		}
		| unit
		{
			outlog<<"At line no: "<<lines<<" program : unit "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"program");
		}
		;

unit : var_declaration
		{
			outlog<<"At line no: "<<lines<<" unit : var_declaration "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"unit");
		}
		| func_definition
		{
			outlog<<"At line no: "<<lines<<" unit : func_definition "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"unit");
		}
		;

func_definition : type_specifier ID LPAREN func_dummy parameter_list RPAREN compound_statement
		{
			outlog<<"At line no: "<<lines<<" func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement "<<endl<<endl;
			outlog<<$1->get_name()<<" "<<$2->get_name()<<"("+$5->get_name()+")\n"<<$7->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+" "+$2->get_name()+"("+$5->get_name()+")\n"+$7->get_name(),"func_def");

			// The function definition is complete.
			// You can now insert necessary information about the function into the symbol table
			// However, note that the scope of the function and the scope of the compound statement are different.

			// Done during func_dummy reduction
			func_symbol = nullptr;
		}
		| type_specifier ID LPAREN func_dummy RPAREN compound_statement
		{
			outlog<<"At line no: "<<lines<<" func_definition : type_specifier ID LPAREN RPAREN compound_statement "<<endl<<endl;
			outlog<<$1->get_name()<<" "<<$2->get_name()<<"()\n"<<$6->get_name()<<endl<<endl;
			$$ = new symbol_info($1->get_name()+" "+$2->get_name()+"()\n"+$6->get_name(),"func_def");

			// The function definition is complete.
			// You can now insert necessary information about the function into the symbol table
			// However, note that the scope of the function and the scope of the compound statement are different.

			// Done during func_dummy reduction
			func_symbol = nullptr;
		}
		;

func_dummy :
		{
			// outlog<<"At line no: "<<lines<<" func_dummy : "<<endl<<endl;
			// outlog<<"$-1->get_name(): "<<$-1->get_name()<<endl<<endl;

			func_symbol = new symbol_info($-1->get_name(), $-1->get_type());
			func_symbol->set_as_function($-2->get_name(), {}); // Temporary

			if (sym_table->lookup_in_current(func_symbol) != nullptr) {
				logg("At line no: "<<lines<<" Multiple declaration of function "<<func_symbol->get_name()<<endl<<endl);
				errors++;
			} else {
				sym_table->insert(func_symbol);
			}
		}
		;

parameter_list : parameter_list COMMA type_specifier ID
		{
			outlog<<"At line no: "<<lines<<" parameter_list : parameter_list COMMA type_specifier ID "<<endl<<endl;
			outlog<<$1->get_name()<<","<<$3->get_name()<<" "<<$4->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+","+$3->get_name()+" "+$4->get_name(),"param_list");

            // store the necessary information about the function parameters
            // They will be needed when you want to enter the function into the symbol table
			if (!func_symbol->get_param_list().empty()) {
				bool symbol_found = false;
				for (auto &param : func_symbol->get_param_list()) {
					if (param.second == $4->get_name()) {
						logg("At line no: "<<lines<<" Multiple declaration of variable "<<$4->get_name()<<" in parameter of "<< func_symbol->get_name() <<endl<<endl);
						errors++;
						symbol_found = true;
						break;
					}
				}
				if (!symbol_found) {
					func_symbol->add_parameter($3->get_name(), $4->get_name());
				}
			}
		}
		| parameter_list COMMA type_specifier
		{
			outlog<<"At line no: "<<lines<<" parameter_list : parameter_list COMMA type_specifier "<<endl<<endl;
			outlog<<$1->get_name()<<","<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+","+$3->get_name(),"param_list");

            // store the necessary information about the function parameters
            // They will be needed when you want to enter the function into the symbol table
			func_symbol->add_parameter($3->get_name(), "");
		}
 		| type_specifier ID
 		{
			outlog<<"At line no: "<<lines<<" parameter_list : type_specifier ID "<<endl<<endl;
			outlog<<$1->get_name()<<" "<<$2->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+" "+$2->get_name(),"param_list");

            // store the necessary information about the function parameters
            // They will be needed when you want to enter the function into the symbol table
			func_symbol->add_parameter($1->get_name(), $2->get_name());
		}
		| type_specifier
		{
			outlog<<"At line no: "<<lines<<" parameter_list : type_specifier "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"param_list");

            // store the necessary information about the function parameters
            // They will be needed when you want to enter the function into the symbol table
			func_symbol->add_parameter($1->get_name(), "");
		}
 		;

compound_statement : LCURL scope_entry statements RCURL
		{
			outlog<<"At line no: "<<lines<<" compound_statement : LCURL statements RCURL "<<endl<<endl;
			outlog<<"{\n"+$3->get_name()+"\n}"<<endl<<endl;

			$$ = new symbol_info("{\n"+$3->get_name()+"\n}","comp_stmnt");

			// The compound statement is complete.
			// Print the symbol table here and exit the scope
			// Note that function parameters should be in the current scope
			sym_table->print_all_scopes(outlog);
			int removed_id = sym_table->get_current_scope_id();
			sym_table->exit_scope();
			outlog << "ScopeTable with ID " << removed_id << " removed" << endl << endl;
		}
		| LCURL scope_entry RCURL
		{
			outlog<<"At line no: "<<lines<<" compound_statement : LCURL RCURL "<<endl<<endl;
			outlog<<"{\n}"<<endl<<endl;

			$$ = new symbol_info("{\n}","comp_stmnt");

			// The compound statement is complete.
			// Print the symbol table here and exit the scope
			sym_table->print_all_scopes(outlog);
			int removed_id = sym_table->get_current_scope_id();
			sym_table->exit_scope();
			outlog << "ScopeTable with ID " << removed_id << " removed" << endl << endl;
		}
		;

scope_entry :
		{
			sym_table->enter_scope();
			outlog << "New ScopeTable with ID " << sym_table->get_current_scope_id() << " created" << endl << endl;

			if (!func_symbol->get_param_list().empty()) {
				for (auto &param : func_symbol->get_param_list()) {
					symbol_info* param_symbol = new symbol_info(param.second, "ID");
					param_symbol->set_data_type(param.first);
					sym_table->insert(param_symbol);
				}
			}
		}
		;

var_declaration : type_specifier declaration_list SEMICOLON
		{
			outlog<<"At line no: "<<lines<<" var_declaration : type_specifier declaration_list SEMICOLON "<<endl<<endl;
			outlog<<$1->get_name()<<" "<<$2->get_name()<<";"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+" "+$2->get_name()+";","var_dec");

			// Insert necessary information about the variables in the symbol table

			if ($1->get_name() == "void") {
				logg("At line no: "<<lines<<" variable type can not be void"<<endl<<endl);
				errors++;
				for (auto &var : var_list) { var->set_data_type("error"); }
			} else {
				for (auto &var : var_list) { var->set_data_type($1->get_name()); }
			}
			var_list.clear();
		}
		;

type_specifier : INT
		{
			outlog<<"At line no: "<<lines<<" type_specifier : INT "<<endl<<endl;
			outlog<<"int"<<endl<<endl;

			$$ = new symbol_info("int","type");
	    }
 		| FLOAT
 		{
			outlog<<"At line no: "<<lines<<" type_specifier : FLOAT "<<endl<<endl;
			outlog<<"float"<<endl<<endl;

			$$ = new symbol_info("float","type");
	    }
 		| VOID
 		{
			outlog<<"At line no: "<<lines<<" type_specifier : VOID "<<endl<<endl;
			outlog<<"void"<<endl<<endl;

			$$ = new symbol_info("void","type");
	    }
 		;

declaration_list : declaration_list COMMA ID
		{
			outlog<<"At line no: "<<lines<<" declaration_list : declaration_list COMMA ID "<<endl<<endl;
			outlog<<$1->get_name()+","<<$3->get_name()<<endl<<endl;

			// you may need to store the variable names to insert them in symbol table here or later
			$$ = new symbol_info($1->get_name()+","+$3->get_name(),"decl_list"); // Missing Synthesis Added
			temp_sym = new symbol_info($3->get_name(), "ID");

			if (sym_table->lookup_in_current(temp_sym) != nullptr) {
				logg("At line no: "<<lines<<" Multiple declaration of variable "<<$3->get_name()<<endl<<endl);
				errors++;
			} else {
				var_list.push_back(temp_sym);
				sym_table->insert(temp_sym);
			}
		}
		| declaration_list COMMA ID LTHIRD CONST_INT RTHIRD //array after some declaration
		{
			outlog<<"At line no: "<<lines<<" declaration_list : declaration_list COMMA ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
			outlog<<$1->get_name()+","<<$3->get_name()<<"["<<$5->get_name()<<"]"<<endl<<endl;

			// you may need to store the variable names to insert them in symbol table here or later
			$$ = new symbol_info($1->get_name()+","+$3->get_name()+"["+ $5->get_name()+"]","decl_list"); // Missing Synthesis Added
			temp_sym = new symbol_info($3->get_name(), "ID");
			temp_sym->set_as_array(stoi($5->get_name()));

			if (sym_table->lookup_in_current(temp_sym) != nullptr) {
				logg("At line no: "<<lines<<" Multiple declaration of variable "<<$3->get_name()<<endl<<endl);
				errors++;
			} else {
				var_list.push_back(temp_sym);
				sym_table->insert(temp_sym);
			}
		}
		|ID
		{
			outlog<<"At line no: "<<lines<<" declaration_list : ID "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			// you may need to store the variable names to insert them in symbol table here or later
			$$ = new symbol_info($1->get_name(),"decl_list"); // Missing Synthesis Added
			temp_sym = new symbol_info($1->get_name(), "ID");

			if (sym_table->lookup_in_current(temp_sym) != nullptr) {
				logg("At line no: "<<lines<<" Multiple declaration of variable "<<$1->get_name()<<endl<<endl);
				errors++;
			} else {
				var_list.push_back(temp_sym);
				sym_table->insert(temp_sym);
			}
		}
		| ID LTHIRD CONST_INT RTHIRD //array
		{
			outlog<<"At line no: "<<lines<<" declaration_list : ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
			outlog<<$1->get_name()<<"["<<$3->get_name()<<"]"<<endl<<endl;

			// you may need to store the variable names to insert them in symbol table here or later
			$$ = new symbol_info($1->get_name()+"["+ $3->get_name()+"]","decl_list"); // Missing Synthesis Added
			temp_sym = new symbol_info($1->get_name(), "ID");
			temp_sym->set_as_array(stoi($3->get_name()));

			if (sym_table->lookup_in_current(temp_sym) != nullptr) {
				logg("At line no: "<<lines<<" Multiple declaration of variable "<<$1->get_name()<<endl<<endl);
				errors++;
			} else {
				var_list.push_back(temp_sym);
				sym_table->insert(temp_sym);
			}
		}
		;


statements : statement
		{
			outlog<<"At line no: "<<lines<<" statements : statement "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"stmnts");
		}
		| statements statement
		{
			outlog<<"At line no: "<<lines<<" statements : statements statement "<<endl<<endl;
			outlog<<$1->get_name()<<"\n"<<$2->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"\n"+$2->get_name(),"stmnts");
		}
		;


statement : var_declaration
	  	{
	    	outlog<<"At line no: "<<lines<<" statement : var_declaration "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"stmnt");
	  	}
	  	| func_definition
	  	{
	  		outlog<<"At line no: "<<lines<<" statement : func_definition "<<endl<<endl;
            outlog<<$1->get_name()<<endl<<endl;

            $$ = new symbol_info($1->get_name(),"stmnt");
	  	}
	  	| expression_statement
	  	{
	    	outlog<<"At line no: "<<lines<<" statement : expression_statement "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"stmnt");
		}
		| compound_statement
		{
	    	outlog<<"At line no: "<<lines<<" statement : compound_statement "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"stmnt");
		}
		| FOR LPAREN expression_statement expression_statement expression RPAREN statement
		{
	    	outlog<<"At line no: "<<lines<<" statement : FOR LPAREN expression_statement expression_statement expression RPAREN statement "<<endl<<endl;
			outlog<<"for("<<$3->get_name()<<$4->get_name()<<$5->get_name()<<")\n"<<$7->get_name()<<endl<<endl;

			$$ = new symbol_info("for("+$3->get_name()+$4->get_name()+$5->get_name()+")\n"+$7->get_name(),"stmnt");
		}
		| IF LPAREN expression RPAREN statement %prec LOWER_THAN_ELSE
		{
	    	outlog<<"At line no: "<<lines<<" statement : IF LPAREN expression RPAREN statement "<<endl<<endl;
			outlog<<"if("<<$3->get_name()<<")\n"<<$5->get_name()<<endl<<endl;

			$$ = new symbol_info("if("+$3->get_name()+")\n"+$5->get_name(),"stmnt");
		}
		| IF LPAREN expression RPAREN statement ELSE statement
		{
	    	outlog<<"At line no: "<<lines<<" statement : IF LPAREN expression RPAREN statement ELSE statement "<<endl<<endl;
			outlog<<"if("<<$3->get_name()<<")\n"<<$5->get_name()<<"\nelse\n"<<$7->get_name()<<endl<<endl;

			$$ = new symbol_info("if("+$3->get_name()+")\n"+$5->get_name()+"\nelse\n"+$7->get_name(),"stmnt");
		}
		| WHILE LPAREN expression RPAREN statement
		{
	    	outlog<<"At line no: "<<lines<<" statement : WHILE LPAREN expression RPAREN statement "<<endl<<endl;
			outlog<<"while("<<$3->get_name()<<")\n"<<$5->get_name()<<endl<<endl;

			$$ = new symbol_info("while("+$3->get_name()+")\n"+$5->get_name(),"stmnt");
		}
		| PRINTLN LPAREN ID RPAREN SEMICOLON
		{
	    	outlog<<"At line no: "<<lines<<" statement : PRINTLN LPAREN ID RPAREN SEMICOLON "<<endl<<endl;
			outlog<<"printf("<<$3->get_name()<<");"<<endl<<endl;

			$$ = new symbol_info("printf("+$3->get_name()+");","stmnt");

			if (sym_table->lookup($3) == nullptr) {
				logg("At line no: "<<lines<<" Undeclared variable "<<$3->get_name()<<endl<<endl);
				errors++;
			}
		}
		| RETURN expression SEMICOLON
		{
	    	outlog<<"At line no: "<<lines<<" statement : RETURN expression SEMICOLON "<<endl<<endl;
			outlog<<"return "<<$2->get_name()<<";"<<endl<<endl;

			$$ = new symbol_info("return "+$2->get_name()+";","stmnt");
		}
		;

expression_statement : SEMICOLON
		{
			outlog<<"At line no: "<<lines<<" expression_statement : SEMICOLON "<<endl<<endl;
			outlog<<";"<<endl<<endl;

			$$ = new symbol_info(";","expr_stmt");
		}
		| expression SEMICOLON
		{
			outlog<<"At line no: "<<lines<<" expression_statement : expression SEMICOLON "<<endl<<endl;
			outlog<<$1->get_name()<<";"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+";","expr_stmt");

			$$->set_data_type($1->get_data_type());
		}
		;

variable : ID
      	{
	    	outlog<<"At line no: "<<lines<<" variable : ID "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"varbl");

			temp_sym = sym_table->lookup($1);
			if (temp_sym == nullptr) {
				logg("At line no: "<<lines<<" Undeclared variable "<<$1->get_name()<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else {
				string var_type = temp_sym->get_data_type();
				if (temp_sym->get_is_array()) {
					logg("At line no: "<<lines<<" variable is of array type : "<<$1->get_name()<<endl<<endl);
					errors++;
				}
				$$->set_data_type(var_type);
			}
		}
		| ID LTHIRD expression RTHIRD
		{
			outlog<<"At line no: "<<lines<<" variable : ID LTHIRD expression RTHIRD "<<endl<<endl;
			outlog<<$1->get_name()<<"["<<$3->get_name()<<"]"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"["+$3->get_name()+"]","varbl");

			if ($3->get_data_type() != "int") {
				logg("At line no: "<<lines<<" array index is not of integer type : "<<$1->get_name()<<endl<<endl);
				errors++;
			}

			temp_sym = sym_table->lookup($1);
			if (temp_sym == nullptr) {
				logg("At line no: "<<lines<<" Undeclared variable "<<$1->get_name()<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else {
				string var_type = temp_sym->get_data_type();
				if (!temp_sym->get_is_array()) {
					logg("At line no: "<<lines<<" variable is not of array type : "<<$1->get_name()<<endl<<endl);
					errors++;
				}
				$$->set_data_type(var_type);
			}
		}
		;

expression : logic_expression
	   	{
	    	outlog<<"At line no: "<<lines<<" expression : logic_expression "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"expr");

			$$->set_data_type($1->get_data_type());
		}
		| variable ASSIGNOP logic_expression
		{
	    	outlog<<"At line no: "<<lines<<" expression : variable ASSIGNOP logic_expression "<<endl<<endl;
			outlog<<$1->get_name()<<"="<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"="+$3->get_name(),"expr");

			if ($1->get_data_type() == "void" || $3->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "error" || $3->get_data_type() == "error") {
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "int" && $3->get_data_type() == "float") {
				logg("At line no: "<<lines<<" Warning: Assignment of float value into variable of integer type "<<endl<<endl);
				errors++;
				$$->set_data_type($1->get_data_type());
			} else {
				$$->set_data_type($1->get_data_type());
			}
		}
		;

logic_expression : rel_expression
	    {
	    	outlog<<"At line no: "<<lines<<" logic_expression : rel_expression "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"lgc_expr");

			$$->set_data_type($1->get_data_type());
		}
		| rel_expression LOGICOP rel_expression
		{
	    	outlog<<"At line no: "<<lines<<" logic_expression : rel_expression LOGICOP rel_expression "<<endl<<endl;
			outlog<<$1->get_name()<<$2->get_name()<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+$2->get_name()+$3->get_name(),"lgc_expr");

			if ($1->get_data_type() == "void" || $3->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "error" || $3->get_data_type() == "error") {
				$$->set_data_type("error");
			} else {
				$$->set_data_type("int");
			}
		}
		;

rel_expression : simple_expression
		{
	    	outlog<<"At line no: "<<lines<<" rel_expression : simple_expression "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"rel_expr");

			$$->set_data_type($1->get_data_type());
	    }
		| simple_expression RELOP simple_expression
		{
	    	outlog<<"At line no: "<<lines<<" rel_expression : simple_expression RELOP simple_expression "<<endl<<endl;
			outlog<<$1->get_name()<<$2->get_name()<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+$2->get_name()+$3->get_name(),"rel_expr");

			if ($1->get_data_type() == "void" || $3->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "error" || $3->get_data_type() == "error") {
				$$->set_data_type("error");
			} else {
				$$->set_data_type("int");
			}
	    }
		;

simple_expression : term
		{
	    	outlog<<"At line no: "<<lines<<" simple_expression : term "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"simp_expr");

			$$->set_data_type($1->get_data_type());

		}
		| simple_expression ADDOP term
		{
	    	outlog<<"At line no: "<<lines<<" simple_expression : simple_expression ADDOP term "<<endl<<endl;
			outlog<<$1->get_name()<<$2->get_name()<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+$2->get_name()+$3->get_name(),"simp_expr");

			if ($1->get_data_type() == "void" || $3->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "error" || $3->get_data_type() == "error") {
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "float" || $3->get_data_type() == "float") {
				$$->set_data_type("float");
			} else {
				$$->set_data_type("int");
			}
		}
		;

term : unary_expression //term can be void because of un_expr->factor
     	{
	    	outlog<<"At line no: "<<lines<<" term : unary_expression "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"term");

			$$->set_data_type($1->get_data_type());
		}
		|  term MULOP unary_expression
		{
	    	outlog<<"At line no: "<<lines<<" term : term MULOP unary_expression "<<endl<<endl;
			outlog<<$1->get_name()<<$2->get_name()<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+$2->get_name()+$3->get_name(),"term");

			if ($1->get_data_type() == "void" || $3->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if ($1->get_data_type() == "error" || $3->get_data_type() == "error") {
				$$->set_data_type("error");
			} else {
				if ($3->get_name() == "0") {
					if ($2->get_name() == "/") {
						logg("At line no: "<<lines<<" Division by 0"<<endl<<endl);
						errors++;
					} else if ($2->get_name() == "%") {
						logg("At line no: "<<lines<<" Modulus by 0"<<endl<<endl);
						errors++;
					}
					$$->set_data_type("error");
				}
				if ($2->get_name() == "%") {
					if ($1->get_data_type() != "int" || $3->get_data_type() != "int") {
						logg("At line no: "<<lines<<" Modulus operator on non integer type "<<endl<<endl);
						errors++;
						$$->set_data_type("error");
					} else {
						$$->set_data_type("int");
					}
				} else if ($1->get_data_type() == "float" || $3->get_data_type() == "float") {
					$$->set_data_type("float");
				} else {
					$$->set_data_type("int");
				}
			}
		}
		;

unary_expression : ADDOP unary_expression  // un_expr can be void because of factor
		{
	    	outlog<<"At line no: "<<lines<<" unary_expression : ADDOP unary_expression "<<endl<<endl;
			outlog<<$1->get_name()<<$2->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+$2->get_name(),"un_expr");

			if ($2->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else {
				$$->set_data_type($2->get_data_type());
			}
		}
		| NOT unary_expression
		{
	    	outlog<<"At line no: "<<lines<<" unary_expression : NOT unary_expression "<<endl<<endl;
			outlog<<"!"<<$2->get_name()<<endl<<endl;

			$$ = new symbol_info("!"+$2->get_name(),"un_expr");

			if ($2->get_data_type() == "void") {
				logg("At line no: "<<lines<<" operation on void type "<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else {
				$$->set_data_type("int");
			}
		}
		| factor
		{
	    	outlog<<"At line no: "<<lines<<" unary_expression : factor "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"un_expr");

			$$->set_data_type($1->get_data_type());
		}
		;

factor	: variable
		{
			outlog<<"At line no: "<<lines<<" factor : variable "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"fctr");

			$$->set_data_type($1->get_data_type());
		}
		| ID LPAREN argument_list RPAREN
		{
			outlog<<"At line no: "<<lines<<" factor : ID LPAREN argument_list RPAREN "<<endl<<endl;
			outlog<<$1->get_name()<<"("<<$3->get_name()<<")"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"("+$3->get_name()+")","fctr");

			func_symbol = sym_table->lookup($1);
			if (func_symbol == nullptr) {
				logg("At line no: "<<lines<<" Undeclared function "<<$1->get_name()<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else if (!func_symbol->get_is_function()) {
				logg("At line no: "<<lines<<" "<<$1->get_name()<<" is not a function"<<endl<<endl);
				errors++;
				$$->set_data_type("error");
			} else {
				string ret_type = func_symbol->get_return_type();
				$$->set_data_type(ret_type);
				if (arg_list.size() != func_symbol->get_param_list().size()) {
					logg("At line no: "<<lines<<" Inconsistencies in number of arguments in function call: "<<$1->get_name()<<endl<<endl);
					errors++;
				} else {
					if (!func_symbol->get_param_list().empty()) {
						for (size_t i = 0; i < arg_list.size(); i++) {
							string expected_type = func_symbol->get_param_list()[i].first;
							string actual_type = arg_list[i]->get_data_type();
							if (expected_type != actual_type) {
								logg("At line no: "<<lines<<" argument "<<(i+1)<<" type mismatch in function call: "<<$1->get_name()<<endl<<endl);
								errors++;
							}
						}
					}
				}
			}
			arg_list.clear();
		}
		| LPAREN expression RPAREN
		{
			outlog<<"At line no: "<<lines<<" factor : LPAREN expression RPAREN "<<endl<<endl;
			outlog<<"("<<$2->get_name()<<")"<<endl<<endl;

			$$ = new symbol_info("("+$2->get_name()+")","fctr");
			$$->set_data_type($2->get_data_type());
		}
		| CONST_INT
		{
			outlog<<"At line no: "<<lines<<" factor : CONST_INT "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"fctr");
			$$->set_data_type("int");

		}
		| CONST_FLOAT
		{
			outlog<<"At line no: "<<lines<<" factor : CONST_FLOAT "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"fctr");
			$$->set_data_type("float");
		}
		| variable INCOP
		{
			outlog<<"At line no: "<<lines<<" factor : variable INCOP "<<endl<<endl;
			outlog<<$1->get_name()<<"++"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"++","fctr");
			$$->set_data_type($1->get_data_type());
		}
		| variable DECOP
		{
			outlog<<"At line no: "<<lines<<" factor : variable DECOP "<<endl<<endl;
			outlog<<$1->get_name()<<"--"<<endl<<endl;

			$$ = new symbol_info($1->get_name()+"--","fctr");
			$$->set_data_type($1->get_data_type());
		}
		;

argument_list : arguments
		{
			outlog<<"At line no: "<<lines<<" argument_list : arguments "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"arg_list");
		}
		|
		{
			outlog<<"At line no: "<<lines<<" argument_list :  "<<endl<<endl;
			outlog<<""<<endl<<endl;

			$$ = new symbol_info("","arg_list");
		}
		;

arguments : arguments COMMA logic_expression
		{
			outlog<<"At line no: "<<lines<<" arguments : arguments COMMA logic_expression "<<endl<<endl;
			outlog<<$1->get_name()<<","<<$3->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name()+","+$3->get_name(),"arg");

			arg_list.push_back($3);
		}
		| logic_expression
		{
			outlog<<"At line no: "<<lines<<" arguments : logic_expression "<<endl<<endl;
			outlog<<$1->get_name()<<endl<<endl;

			$$ = new symbol_info($1->get_name(),"arg");

			arg_list.push_back($1);
		}
		;


%%

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		cout<<"Please give input file name"<<endl;
		return 0;
	}
	yyin = fopen(argv[1], "r");
	outlog.open("my_log.txt", ios::trunc);
	errorlog.open("my_error.txt", ios::trunc);

	if(yyin == NULL)
	{
		cout<<"Couldn't open input file"<<endl;
		return 0;
	}
	// Enter the global or the first scope here
	sym_table = new symbol_table(10);
	outlog << "New ScopeTable with ID " << sym_table->get_current_scope_id() << " created" << endl << endl;

	yyparse();

	outlog << endl << "Total lines: " << lines << endl;
	outlog << "Total errors: " << errors << endl;
	errorlog << "Total errors: " << errors << endl;

	outlog.close();
	errorlog.close();

	fclose(yyin);
	delete sym_table;

	return 0;
}