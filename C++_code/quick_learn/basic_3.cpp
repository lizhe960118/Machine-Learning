//三、C++面向对象之继承性
//c++中调用父类函数的写法
class Person{
	private:
		string _name;
		int _age;
	public:
		Person(string name, int age):_name(name), _age(age){
		}
		void say(){
			cout << "Hello World";
		}
}; 

//继承
class Female:public Person{
	private:
		bool _longhair;
	public:
//		构造函数通过:符号调用父类构造，通过longhair初始化本类参数 
		Female(string name, int age):Person(name, age), _longhair(longhair){
		} 
		void action(){
//			父类的调用，java用super,C#用base,而c++用父类的名字 
			Person::say();
		}
}; 
