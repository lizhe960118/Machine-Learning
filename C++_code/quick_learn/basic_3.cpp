//����C++�������֮�̳���
//c++�е��ø��ຯ����д��
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

//�̳�
class Female:public Person{
	private:
		bool _longhair;
	public:
//		���캯��ͨ��:���ŵ��ø��๹�죬ͨ��longhair��ʼ��������� 
		Female(string name, int age):Person(name, age), _longhair(longhair){
		} 
		void action(){
//			����ĵ��ã�java��super,C#��base,��c++�ø�������� 
			Person::say();
		}
}; 
