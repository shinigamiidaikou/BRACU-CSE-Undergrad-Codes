#include <bits/stdc++.h>

using namespace std;

class symbol_info
{
private:
    string name;
    string type;

    // Write necessary attributes to store what type of symbol it is (variable/array/function)
    // Write necessary attributes to store the type/return type of the symbol (int/float/void/...)
    // Write necessary attributes to store the parameters of a function
    // Write necessary attributes to store the array size if the symbol is an array

    string data_type;
    bool is_array = false;
    int array_size = -1;

    string return_type;
    bool is_function = false;
    vector<pair<string, string>> param_list;

public:
    symbol_info(string name, string type)
    {
        this->name = name;
        this->type = type;
    }
    string get_name()
    {
        return name;
    }
    string get_type()
    {
        return type;
    }
    void set_name(string name)
    {
        this->name = name;
    }
    void set_type(string type)
    {
        this->type = type;
    }

    // Write necessary functions to set and get the attributes
    void set_data_type(const string &data_type)
    {
        this->data_type = data_type;
    }
    void set_as_array(int size)
    {
        is_array = true;
        array_size = size;
    }
    void set_as_function(const string &return_type, const vector<pair<string, string>>&params)
    {
        is_function = true;
        this->return_type = return_type;
        param_list = params;
    }
    void add_parameter(const string &datatype, const string &name)
    {
        param_list.push_back({datatype, name});
    }
    string get_data_type() const
    {
        return data_type;
    }
    bool get_is_array() const
    {
        return is_array;
    }
    int get_array_size() const
    {
        return array_size;
    }
    bool get_is_function() const
    {
        return is_function;
    }
    string get_return_type() const
    {
        return return_type;
    }
    vector<pair<string, string>> get_param_list() const
    {
        return param_list;
    }
    ~symbol_info()
    {
        // Write necessary code to deallocate memory, if necessary
    }
};
