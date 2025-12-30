#include "scope_table.h"

class symbol_table
{
private:
    scope_table *current_scope;
    int bucket_count;
    int current_scope_id;

public:
    symbol_table(int bucket_count);
    ~symbol_table();
    void enter_scope();
    void exit_scope();
    bool insert(symbol_info *symbol);
    symbol_info *lookup(symbol_info *symbol);
    void print_current_scope(ofstream &outlog);
    void print_all_scopes(ofstream &outlog);

    // you can add more methods if you need
    int get_current_scope_id();
    symbol_info* lookup_in_current(symbol_info *symbol);
};

// complete the methods of symbol_table class
symbol_table::symbol_table(int bucket_count)
{
    this->bucket_count = bucket_count;
    current_scope_id = 1;
    current_scope = new scope_table(bucket_count, current_scope_id, nullptr);
}
symbol_table::~symbol_table()
{
    while (current_scope != nullptr)
    {
        scope_table *temp = current_scope;
        current_scope = current_scope->get_parent_scope();
        delete temp;
    }
}
void symbol_table::enter_scope()
{
    current_scope_id++;
    scope_table *new_scope = new scope_table(bucket_count, current_scope_id, current_scope);
    current_scope = new_scope;
}
void symbol_table::exit_scope()
{
    if (current_scope != nullptr)
    {
        scope_table *temp = current_scope;
        current_scope = current_scope->get_parent_scope();
        delete temp;
    }
}
bool symbol_table::insert(symbol_info *symbol)
{
    if (current_scope == nullptr)
    {
        return false;
    }
    return current_scope->insert_in_scope(symbol);
}
symbol_info *symbol_table::lookup(symbol_info *symbol)
{
    scope_table *temp = current_scope;
    while (temp != nullptr)
    {
        symbol_info *found_symbol = temp->lookup_in_scope(symbol);
        if (found_symbol != nullptr)
        {
            return found_symbol;
        }
        temp = temp->get_parent_scope();
    }
    return nullptr;
}
void symbol_table::print_current_scope(ofstream &outlog)
{
    if (current_scope != nullptr)
    {
        current_scope->print_scope_table(outlog);
    }
}
void symbol_table::print_all_scopes(ofstream &outlog)
{
    outlog << "################################" << endl
           << endl;
    scope_table *temp = current_scope;
    while (temp != nullptr)
    {
        temp->print_scope_table(outlog);
        temp = temp->get_parent_scope();
        if (temp != nullptr)
        {
            outlog << endl;
        }
    }
    outlog << "################################" << endl
           << endl;
}

// Extra method definitions
int symbol_table::get_current_scope_id()
{
    if (current_scope != nullptr)
    {
        return current_scope->get_unique_id();
    }
    return -1;
}
symbol_info* symbol_table::lookup_in_current(symbol_info *symbol)
{
    if (current_scope != nullptr)
    {
        return current_scope->lookup_in_scope(symbol);
    }
    return nullptr;
}