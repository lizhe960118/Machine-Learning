// auto use
# include <iostream>
# include <vector>

/*
auto a_int = 8;
auto a_float = 8.023;
auto ptr = &a_float;
//auto data; // this is not allowed

auto merge(auto a, auto b){
    std::vector<int> c = dosomething(a, b);
    return c;
}

std::vector<int> a = {1, 2, 3};
std::vector<int> b = {1, 2, 3};
auto c = merge(a, b);
*/

/*
void populate(auto &data){
    data.insert({"a", {1, 4}});
    data.insert({"b", {3, 1}});
    data.insert({"c", {2, 3}});
};

auto merge(auto data, auto uncoming_data){
    auto result = data;
    for (auto it:uncoming_data){
        result.insert(it);
    }
    return result;
}

int main(){
    std::map<std::string, std::pair<int, int> > data;
    populate(data);

    std::map<std::string, std::pair<int, int> > uncoming_data;
    uncoming_data.insert({"d", {1, 5}});

    auto final_data = merge(data, uncoming_data);

    for (auto itr : final_data){
        auto [v1,v2] = itr.second;
        std::cout << itr.first << " " << v1 << " " << v2 << std::endl;
    }

    return 0;
}
*/

// lambda表达式
/*
std::vector<std::pair<int,int> > data = {{1, 3}, {7, 6}, {12, 4}};
std::sort(begin(data), end(data),[](auto a, auto b){
    return a.second < b.second;
});
*/
/*
［］代表空。因此你不可以在 lambda 表达式中使用任何外部作用域的局部变量。
    只可以使用参数。
［＝］代表可通过值获取作用域内的局部对象（局部变量和参数）   ，
    即你只可以使用但不可修改。
［&］代表可通过引用获取作用域内的局部对象（局部变量和参数），
    即你可以像下面例子中一样修改它。
［this］代表可通过值获取 this 指针。
［a,&b］代表通过值获取对象 a, 通过引用获取对象 b。
*/

/*
int main(){
    std::vector<int> data = {2, 4, 1, 1, 9, 9};
    int factor = 7;
    for_each(begin(data), end(data), [&factor](int &val){
        val = val * factor;
        factor--;
    });
    for (int val:data){
        std::cout << val << " ";
    }
    return 0;
}
*/

//constexpr double
/*
constexpr double fib(int n){
    if (n == 1) return 1;
    return n * fib(n-1);
}

int main(){
    const long long bigval = fib(20);
    std::cout << bigval << std::endl;
    return 0;
}
*/

int main(){
    auto user_info = std::make_tuple("M", "Chowdhully", 25);
    std::get<0>(user_info);
    std::get<1>(user_info);
    std::get<2>(user_info);

    std::string first_name, last_name, age;
    std::tie(first_name, last_name, age) = user_info;

    // auto [first_name, last_name, age] = user_info;
    return 0;
}


