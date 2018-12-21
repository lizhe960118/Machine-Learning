template<typename T>
T lp_max(const T a, const T b){
	if(a >= b) return a;
	else return b;
}
//将模板方法的声明和实现都放在lp_max.h中，编译main.h时会按照需要生成不同的方法 
