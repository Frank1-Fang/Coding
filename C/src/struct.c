#include <stdio.h>
#include <string.h>

// 定义结构体
struct Book {
    char title[100];
    char author[50];
    char subject[100];
    int book_id;
};

// 打印结构信息（传值）按值传递（会复制结构）
void printBook(struct Book b) {
    printf("[值传递] Title: %s, Author: %s, ID: %d\n", b.title, b.author, b.book_id);
}

// 打印结构信息（传指针）按地址传递（更高效）
void printBookPtr(struct Book *b) {
    printf("[指针传递] Title: %s, Author: %s, ID: %d\n", b->title, b->author, b->book_id);
}

int main() {
    // 初始化结构体
    struct Book book1 = {
        "C Language",
        "Dennis Ritchie",
        "Programming",
        1001
    };
    // 结构体变量的定义与初始化：也可以先声明结构体变量，再分步赋值进行初始化
    // 分步进行初始化
    struct Book book2;
    strcpy(book2.title, "Algorithms");
    strcpy(book2.author, "Robert Sedgewick");
    strcpy(book2.subject, "CS Education");
    book2.book_id = 1002;

    // 调用函数
    printBook(book1);
    printBookPtr(&book2);

    // 结构体大小
    printf("结构体大小: %lu 字节\n", sizeof(struct Book));

    return 0;
}
// struct Books
// {
//    char  title[50];
//    char  author[50];
//    char  subject[100];
//    int   book_id;
// } book = {"C 语言", "RUNOOB", "编程语言", 123456};
// 和其它类型变量一样，对结构体变量可以在定义时指定初始值。
