#include "symbol_info.h"

class scope_table
{
private:
    int bucket_count;
    int unique_id;
    scope_table *parent_scope = nullptr;
    vector<list<symbol_info *>> table;

    int hash_function(string name)
    {
        // write your hash function here
        int hash = 0;
        for (char ch : name)
        {
            hash += ch;
        }
        return hash % bucket_count;
    }

public:
    scope_table();
    scope_table(int bucket_count, int unique_id, scope_table *parent_scope);
    scope_table *get_parent_scope();
    int get_unique_id();
    symbol_info *lookup_in_scope(symbol_info *symbol);
    bool insert_in_scope(symbol_info *symbol);
    bool delete_from_scope(symbol_info *symbol);
    void print_scope_table(ofstream &outlog);
    ~scope_table();

    // you can add more methods if you need
};

// complete the methods of scope_table class
scope_table::scope_table()
{
    // default constructor
    bucket_count = 10;
    unique_id = 0;
    table.resize(bucket_count);
}
scope_table::scope_table(int bucket_count, int unique_id, scope_table *parent_scope)
{
    this->bucket_count = bucket_count;
    this->unique_id = unique_id;
    this->parent_scope = parent_scope;
    table.resize(bucket_count);
}
scope_table *scope_table::get_parent_scope()
{
    return parent_scope;
}
int scope_table::get_unique_id()
{
    return unique_id;
}
symbol_info *scope_table::lookup_in_scope(symbol_info *symbol)
{
    int index = hash_function(symbol->get_name());
    for (auto &sym : table[index])
    {
        if (sym->get_name() == symbol->get_name())
        {
            return sym;
        }
    }
    return nullptr;
}
bool scope_table::insert_in_scope(symbol_info *symbol)
{
    if (lookup_in_scope(symbol) != nullptr)
    {
        return false;
    }
    int index = hash_function(symbol->get_name());
    table[index].push_back(symbol);
    return true;
}
bool scope_table::delete_from_scope(symbol_info *symbol)
{
    int index = hash_function(symbol->get_name());
    auto &bucket = table[index];
    for (auto it = bucket.begin(); it != bucket.end(); ++it)
    {
        if ((*it)->get_name() == symbol->get_name())
        {
            delete *it;
            bucket.erase(it);
            return true;
        }
    }
    return false;
}
void scope_table::print_scope_table(ofstream &outlog)
{
    outlog << "ScopeTable # " + to_string(unique_id) << endl;

    //iterate through the current scope table and print the symbols and all relevant information
    for (int i = 0; i < bucket_count; i++)
    {
        if (!table[i].empty())
        {
            outlog << i << " --> " << endl;
            for (auto &sym : table[i])
            {
                outlog << "< " << sym->get_name() << " : " << sym->get_type() << " >" << endl;

                if (sym->get_is_function())
                {
                    outlog << "Function Definition" << endl;
                    outlog << "Return Type: " << sym->get_return_type() << endl;
                    outlog << "Number of Parameters: " << sym->get_parameters().size() << endl;
                    outlog << "Parameter Details: ";

                    if (!sym->get_parameters().empty())
                    {
                        auto params = sym->get_parameters();
                        for (size_t j = 0; j < params.size(); j++)
                        {
                            outlog << params[j].first << " " << params[j].second;
                            if (j < params.size() - 1)
                            {
                                outlog << ", ";
                            }
                        }
                    }
                    outlog << endl;
                }
                else if (sym->get_is_array())
                {
                    outlog << "Array" << endl;
                    outlog << "Type: " << sym->get_data_type() << endl;
                    outlog << "Size: " << sym->get_array_size() << endl;
                }
                else
                {
                    outlog << "Variable" << endl;
                    outlog << "Type: " << sym->get_data_type() << endl;
                }
            }
            outlog << endl;
        }
    }
}
scope_table::~scope_table()
{
    for (auto &bucket : table)
    {
        for (auto &sym : bucket)
        {
            delete sym;
        }
    }
}