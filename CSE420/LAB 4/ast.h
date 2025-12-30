#ifndef AST_H
#define AST_H

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>

using namespace std;

class ASTNode
{
public:
    virtual ~ASTNode() {}
    virtual string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp, int &temp_count, int &label_count) const = 0;

    // New virtual method, for scope management
    virtual const vector<pair<string, int>> &get_vars() const {
        static const vector<pair<string, int>> empty;
        return empty;
    }
};

// Expression node types

class ExprNode : public ASTNode
{
protected:
    string node_type; // Type information (int, float, void, etc.)
public:
    ExprNode(string type) : node_type(type) {}
    virtual string get_type() const { return node_type; }
};

// Variable node (for ID references)

class VarNode : public ExprNode
{
private:
    string name;
    ExprNode *index; // For array access, nullptr for simple variables

public:
    VarNode(string name, string type, ExprNode *idx = nullptr)
        : ExprNode(type), name(name), index(idx) {}

    ~VarNode()
    {
        if (index)
            delete index;
    }

    bool has_index() const { return index != nullptr; }

    string generate_index_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                               int &temp_count, int &label_count) const
    {
        // TODO: Implement this method
        // Should generate code to calculate the array index and return the temp variable
        string index_expr_temp = index->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        string temp = "t" + to_string(temp_count++);
        if (get_type() == "int") {
            outcode << temp << " = " << index_expr_temp << " * 4" << endl; // Assuming 4 bytes
        } else if (get_type() == "float") {
            outcode << temp << " = " << index_expr_temp << " * 8" << endl; // Assuming 8 bytes
        } else {
            outcode << temp << " = " << index_expr_temp << endl; // Default
        }
        return temp;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for variable access or array access

        if (has_index()) {
            string temp = "t" + to_string(temp_count++);
            string index_temp = generate_index_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << temp << " = " << name << "[" << index_temp << "]" << endl;
            return temp;
        } else {
            string temp = "t" + to_string(temp_count++);
            if (symbol_to_temp.find(name) != symbol_to_temp.end()) {
                return symbol_to_temp[name];
            } else {
                outcode << temp << " = " << name << endl;
                symbol_to_temp[name] = temp;
                return temp;
            }
        }
    }

    string get_name() const { return name; }
};

// Constant node

class ConstNode : public ExprNode
{
private:
    string value;

public:
    ConstNode(string val, string type) : ExprNode(type), value(val) {}

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for constant values

        string temp = "t" + to_string(temp_count++);
        outcode << temp << " = " << value << endl;
        return temp;
    }
};

// Binary operation node

class BinaryOpNode : public ExprNode
{
private:
    string op;
    ExprNode *left;
    ExprNode *right;

public:
    BinaryOpNode(string op, ExprNode *left, ExprNode *right, string result_type)
        : ExprNode(result_type), op(op), left(left), right(right) {}

    ~BinaryOpNode()
    {
        delete left;
        delete right;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for binary operations

        string left_temp = left->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        string right_temp = right->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        string result_temp = "t" + to_string(temp_count++);

        outcode << result_temp << " = " << left_temp << " " << op << " " << right_temp << endl;
        return result_temp;
    }
};

// Unary operation node

class UnaryOpNode : public ExprNode
{
private:
    string op;
    ExprNode *expr;

public:
    UnaryOpNode(string op, ExprNode *expr, string result_type)
        : ExprNode(result_type), op(op), expr(expr) {}

    ~UnaryOpNode() { delete expr; }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for unary operations

        string op_temp = expr->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << op << op_temp << endl;

        return result_temp;
    }
};

// Assignment node

class AssignNode : public ExprNode
{
private:
    VarNode *lhs;
    ExprNode *rhs;

public:
    AssignNode(VarNode *lhs, ExprNode *rhs, string result_type)
        : ExprNode(result_type), lhs(lhs), rhs(rhs) {}

    ~AssignNode()
    {
        delete lhs;
        delete rhs;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for assignment operations
        string rhs_temp = rhs->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        if (lhs->has_index()) {
            string index_temp = lhs->generate_index_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << lhs->get_name() << "[" << index_temp << "] = " << rhs_temp << endl;
        } else {
            outcode << lhs->get_name() << " = " << rhs_temp << endl;
            if (symbol_to_temp.find(lhs->get_name()) != symbol_to_temp.end()) {
                symbol_to_temp[lhs->get_name()] = rhs_temp;
            }
        }
        return "";
    }
};

// Statement node types

class StmtNode : public ASTNode
{
public:
    virtual string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                                 int &temp_count, int &label_count) const = 0;
};

// Expression statement node

class ExprStmtNode : public StmtNode
{
private:
    ExprNode *expr;

public:
    ExprStmtNode(ExprNode *e) : expr(e) {}
    ~ExprStmtNode()
    {
        if (expr)
            delete expr;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for expression statements
        if (expr) {
            return expr->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        }
        return "";
    }
};

// Block (compound statement) node

class BlockNode : public StmtNode
{
private:
    vector<StmtNode *> statements;

public:
    ~BlockNode()
    {
        for (auto stmt : statements)
        {
            delete stmt;
        }
    }

    void add_statement(StmtNode *stmt)
    {
        if (stmt)
            statements.push_back(stmt);
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for all statements in the block
        map<string, string> block_scope = symbol_to_temp;
        set<string> declared_vars;

        for (auto stmt : statements)
        {
            // Track variables declared in this block to prevent incorrect syncing
            vector<pair<string, int>> vars = stmt->get_vars();
            for (const auto& var : vars) {
                declared_vars.insert(var.first);
            }
            // Pass the local scope to statements so they can see/update it
            stmt->generate_code(outcode, block_scope, temp_count, label_count);
        }

        // Scope Management:
        // Propagate changes back to the outer scope for all variables
        // that were NOT declared in this block (i.e., they came from
        // outer scope or were first accessed here)
        for (const auto &entry : block_scope) {
            if (declared_vars.find(entry.first) == declared_vars.end()) {
                symbol_to_temp[entry.first] = entry.second;
            }
        }
        return "";
    }
};

// If statement node

class IfNode : public StmtNode
{
private:
    ExprNode *condition;
    StmtNode *then_block;
    StmtNode *else_block; // nullptr if no else part

public:
    IfNode(ExprNode *cond, StmtNode *then_stmt, StmtNode *else_stmt = nullptr)
        : condition(cond), then_block(then_stmt), else_block(else_stmt) {}

    ~IfNode()
    {
        delete condition;
        delete then_block;
        if (else_block)
            delete else_block;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for if-else statements

        string true_label = "L" + to_string(label_count++);
        string false_label = "L" + to_string(label_count++);
        string next_label = "L" + to_string(label_count++);

        string cond_temp = condition->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        outcode << "if " << cond_temp << " goto " << true_label << endl;
        outcode << "goto " << false_label << endl;

        outcode << true_label << ":\n";
        then_block->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        outcode << "goto " << next_label << endl;

        outcode << false_label << ":\n";
        if (else_block) {
            map<string, string> else_scope = symbol_to_temp;
            else_block->generate_code(outcode, else_scope, temp_count, label_count);
        }

        outcode << next_label << ":\n";
        return "";
    }
};

// While statement node

class WhileNode : public StmtNode
{
private:
    ExprNode *condition;
    StmtNode *body;

public:
    WhileNode(ExprNode *cond, StmtNode *body_stmt)
        : condition(cond), body(body_stmt) {}

    ~WhileNode()
    {
        delete condition;
        delete body;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for while loops

        string start_label = "L" + to_string(label_count++);
        string body_label = "L" + to_string(label_count++);
        string next_label = "L" + to_string(label_count++);

        outcode << start_label << ":\n";
        string cond_temp = condition->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        outcode << "if " << cond_temp << " goto " << body_label << endl;
        outcode << "goto " << next_label << endl;

        outcode << body_label << ":\n";
        body->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        outcode << "goto " << start_label << endl;

        outcode << next_label << ":\n";
        return "";
    }
};

// For statement node

class ForNode : public StmtNode
{
private:
    // The "init" and "condition" declarations were changed to ExprStmtNode* because
    // they are parsed as expression statements in the grammar

    ExprStmtNode *init;      // This was changed from ExprNode* to ExprStmtNode*
    ExprStmtNode *condition; // This was changed from ExprNode* to ExprStmtNode*
    ExprNode *update;
    StmtNode *body;

public:
    // Argument Types are also changed in the constructor
    ForNode(ExprStmtNode *init_expr, ExprStmtNode *cond_expr, ExprNode *update_expr, StmtNode *body_stmt)
        : init(init_expr), condition(cond_expr), update(update_expr), body(body_stmt) {}

    ~ForNode()
    {
        if (init)
            delete init;
        if (condition)
            delete condition;
        if (update)
            delete update;
        delete body;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for "for" loops

        if (init) {
            init->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        }

        string start_label = "L" + to_string(label_count++);
        string body_label = "L" + to_string(label_count++);
        string next_label = "L" + to_string(label_count++);

        outcode << start_label << ":\n";
        if (condition) {
            string cond_temp = condition->generate_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << "if " << cond_temp << " goto " << body_label << endl;
            outcode << "goto " << next_label << endl;
        }

        outcode << body_label << ":\n";
        body->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        if (update) {
            update->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        }
        outcode << "goto " << start_label << endl;

        outcode << next_label << ":\n";
        return "";
    }
};

// Return statement node

class ReturnNode : public StmtNode
{
private:
    ExprNode *expr;

public:
    ReturnNode(ExprNode *e) : expr(e) {}
    ~ReturnNode()
    {
        if (expr)
            delete expr;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for return statements
        if (expr) {
            string temp = expr->generate_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << "return " << temp << endl;
        } else {
            outcode << "return\n";
        }
        return "";
    }
};

// Declaration node

class DeclNode : public StmtNode
{
private:
    string type;
    vector<pair<string, int>> vars; // Variable name and array size (0 for regular vars)

public:
    DeclNode(string t) : type(t) {}

    void add_var(string name, int array_size = 0)
    {
        vars.push_back(make_pair(name, array_size));
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for variable declarations
        for (const auto &var : vars) {
            if (var.second > 0) {
                outcode << "// Declaration: " << type << " " << var.first << "[" << var.second << "]" << endl;
            } else {
                outcode << "// Declaration: " << type << " " << var.first << endl;
            }
            // Reset mapping for new variable in new scope
            symbol_to_temp.erase(var.first);
        }
        return "";
    }

    string get_type() const { return type; }
    const vector<pair<string, int>> &get_vars() const override { return vars; }
};

// Function declaration node

class FuncDeclNode : public ASTNode
{
private:
    string return_type;
    string name;
    vector<pair<string, string>> params; // Parameter type and name
    BlockNode *body;

public:
    FuncDeclNode(string ret_type, string n) : return_type(ret_type), name(n), body(nullptr) {}
    ~FuncDeclNode()
    {
        if (body)
            delete body;
    }

    void add_param(string type, string name)
    {
        params.push_back(make_pair(type, name));
    }

    void set_body(BlockNode *b)
    {
        body = b;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for function declarations

        outcode << "// Function: "  << return_type << " " << name << "(";
        for (size_t i = 0; i < params.size(); i++)
        {
            outcode << params[i].first << " " << params[i].second;
            if (i != params.size() - 1)
                outcode << ", ";
        }
        outcode << ")\n";

        if (body)
        {
            body->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        }
        return "";
    }
};

// Helper class for function arguments

class ArgumentsNode : public ASTNode
{
private:
    vector<ExprNode *> args;

public:
    ~ArgumentsNode()
    {
        // Don't delete args here - they'll be transferred to FuncCallNode
    }

    void add_argument(ExprNode *arg)
    {
        if (arg)
            args.push_back(arg);
    }

    ExprNode *get_argument(int index) const
    {
        if (index >= 0 && index < args.size())
        {
            return args[index];
        }
        return nullptr;
    }

    size_t size() const
    {
        return args.size();
    }

    const vector<ExprNode *> &get_arguments() const
    {
        return args;
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // This node doesn't generate code directly
        return "";
    }
};

// Function call node

class FuncCallNode : public ExprNode
{
private:
    string func_name;
    vector<ExprNode *> arguments;

public:
    FuncCallNode(string name, string result_type)
        : ExprNode(result_type), func_name(name) {}

    ~FuncCallNode()
    {
        for (auto arg : arguments)
        {
            delete arg;
        }
    }

    void add_argument(ExprNode *arg)
    {
        if (arg)
            arguments.push_back(arg);
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for function calls

        for (auto arg : arguments) {
            string arg_temp = arg->generate_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << "param " << arg_temp << endl;
        }

        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = call " << func_name << ", " << arguments.size() << endl;

        return result_temp;
    }
};

// Program node (root of AST)

class ProgramNode : public ASTNode
{
private:
    vector<ASTNode *> units;

public:
    ~ProgramNode()
    {
        for (auto unit : units)
        {
            delete unit;
        }
    }

    void add_unit(ASTNode *unit)
    {
        if (unit)
            units.push_back(unit);
    }

    string generate_code(ofstream &outcode, map<string, string> &symbol_to_temp,
                         int &temp_count, int &label_count) const override
    {
        // TODO: Implement this method
        // Should generate code for the entire program
        for (auto unit : units)
        {
            unit->generate_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << endl;
            symbol_to_temp.clear();
        }
        return "";
    }
};

#endif // AST_H