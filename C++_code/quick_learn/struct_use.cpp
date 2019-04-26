#include <iostream>
#include <cstring>

using namespace std;
void printBook(struct Books *book); // 定义指向结构体的指针 

//结构体类型 Books
struct Books{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
}; 

int main(){
	Books Book1;
	Books Book2;
	
	strcpy( Book1.title, "C++ 教程");
    strcpy( Book1.author, "Runoob"); 
    strcpy( Book1.subject, "编程语言");
    Book1.book_id = 12345;
    
    strcpy( Book2.title, "CSS 教程");
    strcpy( Book2.author, "Runoob");
    strcpy( Book2.subject, "前端技术");
    Book2.book_id = 12346;
	
	printBook(&Book1);
	printBook(&Book2);
} 

void printBook(struct Books *book){
	cout << "Title :" << book->title <<endl;
	cout << "Author :" << book->author << endl;
	cout << "Subject :" << book->subject << endl;
	cout << "Book id :" << book->book_id << endl;
}
