 <span style="color:red;"> .\a.py : Filename</span> 
=====
```cpp
import os

def remove_exe_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except OSError as e:
                    print(f"Error: {file_path} - {e}")
a=f"C:/Users/kairn/OneDrive/Documents/learn/C program/g11"
remove_exe_files(a)

```

 <span style="color:red;"> .\aa.py : Filename</span> 
=====
```cpp
import os

def read_files_and_write_to_readme(base_directory, readme_file):
    with open(readme_file, 'w', encoding='utf-8') as readme:
        for root, dirs, files in os.walk(base_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        readme.write(f" <span style=\"color:red;\"> {file_path} : Filename</span> \n")
                        
                        readme.write("=====\n```cpp\n")
                        readme.write(content)
                        readme.write("\n```\n\n")
                except UnicodeDecodeError:
                    print(f"Unable to decode file: {file_path}")

if __name__ == "__main__":
    base_directory = "."  # You can change this to the root directory you want to start from
    readme_file = "readme.md"

    read_files_and_write_to_readme(base_directory, readme_file)

    print(f"Readme file '{readme_file}' has been created.")

```

 <span style="color:red;"> .\ascii.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    char a='A';
    printf("%c",a);
    printf("\nENd");
}
```

 <span style="color:red;"> .\input.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>//header school/college/bachelor
// #include<iostream>
// using namespace std;
int main(){
    int a;
    char b;
    printf("apple\n");//output stdio
    scanf("%d %c",&a,&b);
    printf("%d and %c",a,b);
    
    // cout<<"appleeee";//iostream
}
```

 <span style="color:red;"> .\readme.md : Filename</span> 
=====
```cpp

```

 <span style="color:red;"> .\website_link.md : Filename</span> 
=====
```cpp
__*vscode*__
[vscode](https://code.visualstudio.com/docs/?dv=win)

### Turbo C
[turbo C](https://www.fileeagle.com/software/download/10105/ada5d9)   

### ming64 
[Winlibs](https://winlibs.com/) -- slow
or, [Googledrive](https://drive.google.com/file/d/1cPvcm24sNCfwBXZjfpd-jzVqo0pkKs1I/view?usp=drive_link) -- gud_spd



### binary to decimal
[binary to decimal](https://www.rapidtables.com/convert/number/binary-to-decimal.html)

### format specifier
[format specifier](https://www.codingeek.com/tutorials/c-programming/escape-sequences-and-format-specifiers-in-c-programming-language/)


```

 <span style="color:red;"> .\0_header\.vscode\tasks.json : Filename</span> 
=====
```cpp
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "cppbuild",
			"label": "C/C++: g++.exe build active file",
			"command": "C:\\mingw64\\bin\\g++.exe",
			"args": [
				"-fdiagnostics-color=always",
				"-g",
				"-std=c++20",
				"${file}",
				"-o",
				"${fileDirname}\\${fileBasenameNoExtension}.exe"
			],
			"options": {
				"cwd": "${fileDirname}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"detail": "compiler: C:\\mingw64\\bin\\g++.exe"
		}
	]
}
```

 <span style="color:red;"> .\0_header\1_File_inclusion\apple.h : Filename</span> 
=====
```cpp
const int age=23;
```

 <span style="color:red;"> .\0_header\1_File_inclusion\current_header.cpp : Filename</span> 
=====
```cpp
#include<stdio.h> //pre-build
#include "apple.h" //specific
int main(){
    printf("%d",age);
    return 0;
}
```

 <span style="color:red;"> .\0_header\1_File_inclusion\header.cpp : Filename</span> 
=====
```cpp
#include<stdio.h> //pre-build

int main(){
    int age = 1;
    printf("%d",age);
    return 0;
}
```

 <span style="color:red;"> .\0_header\2_macro_define\apple.h : Filename</span> 
=====
```cpp
#define anything
const int age=23;
```

 <span style="color:red;"> .\0_header\2_macro_define\qwq.cpp : Filename</span> 
=====
```cpp
#include<stdio.h> 
#include "apple.h"
int main(){
    printf("%d",age);
    return 0;
}
```

 <span style="color:red;"> .\0_header\3_Conditional_inclusion\appl.h : Filename</span> 
=====
```cpp
#ifndef cc
#include "apple.h"
#endif
```

 <span style="color:red;"> .\0_header\3_Conditional_inclusion\apple.h : Filename</span> 
=====
```cpp
#define cc
const int age=193;
```

 <span style="color:red;"> .\0_header\3_Conditional_inclusion\main.cpp : Filename</span> 
=====
```cpp
#include<stdio.h> //pre-build
#include "apple.h"
#include "appl.h" //apple.h
int main(){
    printf("%d",age);
    printf("\nhere");
    return 0;
}
```

 <span style="color:red;"> .\1_basic_command\display.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>//header
#include<conio.h>

int main(){    
    int a;
    a=1;
 printf("Suntoi %d %d",a,a);
 getch();
 return 0;
}
```

 <span style="color:red;"> .\2_comment\com.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    //int a=1;
  
  
   /*if(a==2){
     printf("manago");
     printf("mnago");
    }
    else
      printf("manego");
    */

printf("\n The end");
}
```

 <span style="color:red;"> .\3_variable_and_constant\app.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int _1 = 10;  //variable
    // _1=13;
    const int b = 12; //constant 
    printf("%d ",_1);
    printf("\n%d ",b);
    printf("\nend");
    return 0;
}

//https://www.javatpoint.com/keywords-in-c
```

 <span style="color:red;"> .\4_Operator\2.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int a,b;
    a = 3;
    b=3;
    if(a == b )
      {printf("Add equal %d \n " , a+b);}
    else if(a>=b) //10>3
      printf("Add here %d \n" , a+b);
    else if(a<=b)
      printf("Add there %d \n" , a+b);
    else
      printf("Add %d \n" , a+b);
    return 0;
}
```

 <span style="color:red;"> .\4_Operator\3.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int a,b;
    a = 3;
    b = 1;
    if(a==2 && b ==3 )
      printf("Add there %d \n" , a+b);
    else if(a==10)
      printf("Add here %d \n" , a+b);
    else if(a!=10 || b ==13 )
      printf("Add hora %d \n" , a+b);
    else
      printf("Add %d \n" , a+b);

    return 0;
}
```

 <span style="color:red;"> .\4_Operator\4.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int a,b;
    a = 10; //binary 1010
    b = 3;  //binary 11
    printf("Bitwise and %d \n" , a&b);       /*  1010
                                            and  0011
                                        ------------------
                                                 0010 which is 2 in decimal*/

    printf("Bitwise or %d \n" , a|b);         /*  1010
                                        or        0011
                                        ------------------
                                                   1011 decimal 11*/
    printf("Bitwise not %d \n" , ~b);//-4  //0 change to 1 and vice versa ~b=~00000011=11111100
    //negative because the first digit represent sign Decimal from signed 2's complement (1 digit)
    printf("Bitwise xor %d \n" , a^b); // if a and b are 0 or 1 then 1 otherwise 0      1001
    printf("Bitwise  left shift %d \n" , a<<1); //00001010 --> 00010100
    printf("Bitwise  right shift %d \n" , a>>2);//00001010 --> 00000010 
    return 0;
}
```

 <span style="color:red;"> .\4_Operator\Arithematic.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int a,b;
    a = 2.99;
    b=3;
    printf("Add %d \n" , a+b);
    printf("Sub %d\n" , a-b);
    printf("Mul %d\n" , a*b);
    printf("Div %d\n" , a/b);//decimal
    printf("MOd %d" , a%b); //10/3=3-q 1-r
    
    return 0;
}
```

 <span style="color:red;"> .\4_Operator\othersoperator.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    int a[]={1,2,3,4,5};
(a[0]>a[1] )? a[2]-- : a[2]++ ;//3-1
printf("\n %d",a[2]);//2
printf("\n Finish" );
}

//https://en.wikipedia.org/wiki/Order_of_operations
```

 <span style="color:red;"> .\5_Iteration_statement\do_while.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
int a = 1 ;
do{
        printf("%d  ",a); //a=2
        a++;              //a=3
   }while(a!=3);
    //false
printf("\n Finish");
}
```

 <span style="color:red;"> .\5_Iteration_statement\for.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>//header

int main(){// main function
    int a;

    for(a=1; a<=4 ; a--){      //a=1+2=3+2=5
        printf("%d\t",a);   //a=3
     if(a>=-23){    
            continue;
               }
     if(a<=-20){
       break;}
    }                      
printf("\n Finish");
return 0;
}
```

 <span style="color:red;"> .\5_Iteration_statement\while.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){            //while(condition){ statement}
    int a=1;            //1 is not equal to 10 ---true
    while(a!=10){  //10     //a is not equal to 10        //condition
        printf("%d   ",a);   //3                       //statement
        a++;          //3+1                        //statement
    } //condition end  //false

printf("\n Finish");
return 0;
}
```

 <span style="color:red;"> .\6_Control_statement\1.c : Filename</span> 
=====
```cpp
#include <stdio.h>

int main() {
 int a=1;
 char day =65;
  switch (a) {
    case 1:
      printf("Monday\n"); 
      switch(day){
        case 'A':
        printf("here");
      }
      break;
    case 2+1:
      printf("Tuesday");
      break;
    case 14:
      printf("Wednesday");
      break;
    case 4:
      printf("Thursday");
      break;
    case 5:
      printf("Friday");
      break;
    case 6:
      printf("Saturday");
      break;
    case 7:
      printf("Sunday");
      break;
    default:
     printf("Misinput");
  }
printf("\nend");
return 0;
}
```

 <span style="color:red;"> .\6_Control_statement\ifelse.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    int a = 2 ;
    if(a==2){
     printf("Banana");  if(a==2)
     printf("   sun");
    }
    else if(a==3)
{      printf("manego");
}    else{
      printf("App");}
  


printf("\n The end");
return 0;
}
```

 <span style="color:red;"> .\6_Control_statement\switch.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>
#include <conio.h>
void main(){
int a = 4;
char result[30];

  switch(a)
  {
    case 1 :  
     result = " A: (a>=2 && a <= 4)";
    break;
    case 2  :  
    result = " B: (a>=2 && a <= 5)"; 
    break;
    case 3  : 
     result = " C: (a>=2 && a <= 1)";
    break;
    case (a>=3 && a <= 6)  :  
    result = " D: (a>=3 && a <= 6)"; 
    break;

    default: result = "default: ";
  }
printf("%s",result);
printf("\nend");

}
```

 <span style="color:red;"> .\7_Statement\Compound.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    int a=1;
    if(a==2){
     printf("manago");
     printf("mnago");
    }
    else{
      printf("manego");}
printf("\n The end");
}
```

 <span style="color:red;"> .\7_Statement\control.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    int a=1;
    if(a==2){
     printf("manago");
     printf("mnago");
    }
    else
      printf("APPLE");
    while(a!=2){
     printf("\nhere\n");
     printf("manago\n");
     printf("mnago");
     a++;//1+1
    }
printf("\nThe end");
}
```

 <span style="color:red;"> .\7_Statement\simple.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    printf("man go");
    printf("\nman go"); 
    printf("\tman go");
}
```

 <span style="color:red;"> .\8_error\linker.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>
// #include<iostream> // actual header
int main()
{
    int a;
    for(a = 0; a < 12; a++)
    {
       std::cout<<a<<std::endl;

    }
    return 0;
}
```

 <span style="color:red;"> .\8_error\logical.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main()
{
    int a = 0;
    for(a = 0; a < 12; a++);
    {
       printf("print \n ");
    }
    printf("end");
    return 0;
}
```

 <span style="color:red;"> .\8_error\run_time.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

void main()
{
    int n = 9, divide = 0;
    divide = n/0;
   printf("%d",divide);
}
```

 <span style="color:red;"> .\8_error\syntax.cpp : Filename</span> 
=====
```cpp
#include<stdio.h>

int main(){
    printf("apple") // semi-colon missing i.e. printf("apple");
}
```

