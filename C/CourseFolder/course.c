#include <stdio.h>
#include <stdbool.h>
#include <string.h>


void printMessage() {
    printf("hello world.\n");
}
void excitingFunction() {
    printf("oliver was here.\n");
}

void add(){
    char name[] = "Oliver";
    int number = 63;
    int number2;
    number2 = 25;
    int number3 = number + number2;
    printf("name = %s, number = %d ", name, number3);
}
void area(){
    int height =  10, width =  20;
    int area = height * width;
    printf ("area: %d\n", area);
}


void test(){
    float thing = 20e3;
    printf ("%f\n", thing);
    /// prints with many numbers on the end for some reason
    float decimal = 1.2345;
    printf ("%.5f\n", decimal);
    /// prints 5 decimals, eg: 1.2345
    float x = 5, y = 10;
    float sum2 = x / y;
    printf ("%.1f\n", sum2);
    /// 0.5
    float sum = 8 / 9;
    printf("%f\n", sum);
    //  = 0.000000, because values are treated as integers befor being floated
    float sum3 = (float) 8 / 9;
    printf ("%.1f\n", sum3);
    ///  = 0.9, because of (float)
    int z = 10;
    z += 5;
    printf ("%d\n", z);
    ///adds 5 to a value
    int compare1 = 8;
    int compare2 = 12;
    printf("%d\n", compare1 < compare2);
    ///returns 1 (true) because 8 is less than 12
    printf ("%d\n", compare1 > compare2);
    ///returns 10
    ///&& AND (x < 5 && x <10) returns 1 if both true
    ///|| OR (x < 5 || x < 4) retruns 1 if one statement is true
    ///! NOT (!(x < 5 && x < 10)) reverse the result
    bool isProgramFun = true;
    bool isFishTasty = false;
    ///boolean values returned as integers
    ///1 represents True
    ///0 False
    ///you must use the %d value to print a boolean 
    printf ("%d\n", isProgramFun);
    printf ("%d\n", isFishTasty);
    ///1
    ///0
    printf  ("%d\n", 10 == 10);
    ///1
    printf ("%d\n", 5 == 55);
    ///0
    int myAge = 5;
    int votingAge = 18;
    if (myAge >= votingAge){
        printf("Old enough\n");
    } else{
        printf ("not old enough\n");
    }
    int time = 3;
    if (time < 2) {
        printf ("True");
    } else if (time == 2){
        printf ("time greater");
    } else {
        printf ("ow\n");
    }
    ///ow
    time = 22;
    (time < 20) ? printf ("have a good day\n") : printf ("good evening\n");
    ///short hand if else
    int day = 2;
    switch (day) {
        case 1:
            printf ("monday\n");
            break;
        case 2:
            printf ("tuesday\n");
            break;    
    }
    ///tuesday
    switch (day) {
        case 6 | 7:
            printf ("weekend\n");
            break;
        default:
            printf ("looking forward\n");
    }
    ///looking forward
    bool i = true;

    while (i) {
        printf ("yes\n");
        i = false;
        break;
        /// yes
    }
    int I = 0;
    while (I < 5) {
        printf ("%d\n", I);
        I ++;
    }
    int p = 0;

    do {
        printf ("%d\n", p);
        p++;
    }
    while (p < 10);
    ///0 - 9
    int n;
    for (n = 0; n < 5; n++) {
        printf ("%d\n", n);
    }
    int j, c;

    for (j = 1; j <= 2; j++) {
        printf ("Outer: %d\n", j);

        for (c = 1; c <= 3; c++) {
            printf ("Inner: %d\n", c);
        }
    }
    ///    Outer: 1
    ///    Inner: 1
    ///    Inner: 2
    ///    Inner: 3
    ///    Outer: 2
    ///    Inner: 1
    ///    Inner: 2
    ///    Inner: 3

    int m;

    for (m = 0; m < 10; m++) {
        if (m == 4) {
            continue;
        }
        printf("%d\n", m);
    }
    ///skips 4
    printf("\n");

    int q = 0;

    while (q < 10) {
        if (q == 4) {
            break;
    }
    printf("%d\n", q);
        q++;
    }
    ///0 1 2 3

    printf ("\n");
    
    int o = 0;

    while (o < 10) {
        if (o == 4) {
            o++;
            continue;
        }
        printf("%d\n", o);
        o++;
    }
    ///skips 4
    printf ("\n");

    int myNumbers[] = {2, 5, 10, 25};
    printf ("%d\n", myNumbers[0]);
    ///2

    printf ("\n");

    int b;

    for (b = 0; b < 4; b++) {
        printf ("%d\n", myNumbers[b]);
    }

    ///2 5 10 25
    printf ("\n");
    int myNumbers2 [4];

    myNumbers2[0] = 2;
    myNumbers2[1] = 6;
    myNumbers2[2] = 15;
    myNumbers2[3] = 55;

    int k;

    for (k = 0; k < 5; k++) {
        printf ("%d\n", myNumbers2[k]);
    }
    ///2 6 15 55
    int myNumbers3 [] = {10, 25, 26, 3, 65, 30};
    printf ("size of array: %lu\n", sizeof(myNumbers3));
    ///prints size in bytes
    ///bytes of an integer is usually 4 bytes

    int length = sizeof(myNumbers3) / sizeof(myNumbers3[0]);
    printf ("length of array: %d\n", length);

    
}



void average_of_array() {
    float ages[] = {10, 12, 35, 45, 62, 44, 77, 10, 21, 88, 88, 3};
    int lengthofarray = sizeof (ages) / sizeof(ages[0]);
    int e;
    float average;
    float sum = 0;
    for  (e = 0; e < lengthofarray; e++) {
        sum += ages[e];
    }
    average = sum / lengthofarray;
    printf ("Average was: %f\n", average);
    ///41.250000

}


void lowest_age() {
    int i;
    float ages[] = {10, 12, 35, 45, 62, 44, 77, 10, 21, 88, 88, 3, 0.1};
    int lengthofarray = sizeof (ages) / sizeof(ages[0]);
    float lowest_age = ages[0];
    for (i = 0; i < lengthofarray; i++) {
        if (ages[i] < lowest_age) {
            lowest_age = ages[i];
        }
    }
    printf("Lowest age: %.2f\n", lowest_age);
    
}



void matrix() {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf ("%d\n", matrix[1][1]);
    ///5
    ////[rows], [columns]
    matrix[1][1] = 10;
    printf ("%d", matrix[1][1]);
    ///changes value to 10
}

void string() {
    char greeting[] = "Hello World!";
    printf ("%s\n", greeting);
    ///Hello World!
    printf ("%c\n", greeting[0]);
    ///H
    int i;
    for (i = 0; i < 12; i++){
        printf("%c\n", greeting[i]);
    }
    ///Hello World! each letter on new line

    greeting[0] = 'J';
    printf ("%s\n", greeting);
    ///Jello world
}


void thing() {
    int i;
    
    char car[] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
    char carnew[] ="VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV";


    int len = sizeof (car) / sizeof(car[0]);
    printf("%s\n", car);
    for (i = 0; i < len - 1; i++) {
        car[i] = carnew[i];
        printf("%s\n", car);
    }
}


void multiple() {
    char message[] = "HELLO";
    char name[] = "John";
    printf ("%s %s!", message, name);
}

void special() {     
    char txt[] = "We are the so-called \"Vikings\" from the north.";
    printf ("%s", txt);
    /// \whatever is after it
    ///"\n = new line
    ///"\t = tab
    ///"\0
    }

void stringfunctions() {
    ///#include <string.h>
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    printf ("%lu\n", strlen(alphabet));
    ///26
    printf ("%lu\n", sizeof(alphabet));
    ///27
    
    
    char alphabet2[50] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        printf("%lu\n", strlen(alphabet2));   /// 26
        printf("%lu\n", sizeof(alphabet2));   /// 50
        ///sizeof always returns the

    }

void stringcon() {
    char str1[15] = "Hello ";
    char str2[] = "World!";
    ///size of str1 must be large enough to hold the two joined strings
    strcat (str1, str2);
    ///str stored in str1
    printf ("%s", str1);
}

void stringcopy() {
    char str1[20] = "hello world";
    char str2[20];

    strcpy(str2,str1);
    printf("%s", str2);
}

void stringcompare() {
    char str1[] = "Hello";
    char str2[] = "Hello";
    char str3[] = "Hi";

    printf("%d\n", strcmp(str1, str2));
    ///0 Equal
    printf("%d\n", strcmp(str1, str3));
    ///-4 Not equal

}

void userinput() {
    int mynum;

    printf("Type a number: \n");
    scanf("%d", &mynum);
    
    printf("Your number is: %d", mynum);
}

void twoinputs() {
    int MyNUM;
    char MyChar;

    printf("number and chracter: ");

    scanf("%d %c", &MyNUM, &MyChar);

    printf("Your number is: %d\n", MyNUM);
    printf("Your character is: %c\n", MyChar);
}

void takestring() {
    char firstname[30];
    printf("Enter your first name: \n");
    scanf("%s", firstname);
    printf("Hello %s", firstname);
}

void address() {
    int age = 43;
    printf("%p", &age);
}

void pointers() {
    int age = 43;
    printf("%d\n", age); ///43
    printf("%p\n", &age); ///0x16bd930ac


    int num = 42;
    int* ptr = &num;

    printf("%d\n", num);
    printf("%p\n", &num);
    ///0x16cebb0a8
    printf("%p\n", ptr);
    ///0x16cebb0a8
    printf("%d\n", *ptr);
    ///42
}

void arraypointers() {
    int numbers[] = {1, 4, 5, 63, 22};

    int i;
    for (i= 0; i< 5; i++) {
        printf("%d\n", numbers[i]);
        ///1 3 5 63 22

    }
    for (i = 0; i< 5; i++) {
        printf("%p\n", &numbers[i]);
        ///displays memory addresses
        

    }
    int myint;
    printf("%lu\n", sizeof(myint));
    ///usually four bytes
    int lengthinbits = sizeof(myint) * 8;
    printf("%d\n", lengthinbits);
    ///32


    int morenumbers[4] = {4, 35, 62, 63};

    printf("%p\n", morenumbers);
    printf("%p\n", &morenumbers[0]);
    ///both will be the same as pointers 
    ///display address of the first value as the address of the array


    int numberS[4] = {25, 50, 75, 100};
    printf("%d\n", *numberS);
    ///prints the first value(25) as * goes to the adress of the array

    printf("%d\n", *(numberS + 1));
    ///50
    printf("%d\n", *(numberS + 2));
    ///75
    int *ptr = numberS;
    int j;
    for (j = 0; j < 4; j++) {
        printf("%d\n", *(ptr + j));
        ///loops through array (eg. 25, 50, ...)
    }
}

void changearrayointers() {
    int numbers[9] = {1, 2, 3, 5, 6, 7, 8, 9};

    *numbers = 2;
    printf("%d\n", *numbers);
    ///prints 2
}

void arguments(char name[]) {
    printf("Hello %s\n", name);
    ///hello oliver, john, willem
}

void multipleargu(char name[], int age) {
    printf("Hello %s. You are %d years old.\n", name, age);
}

void arrayFunc(int numbers[5]) {
    for (int i = 0; i < 5; i++) {
        printf("%d\n", numbers[i]);
    }
}



int main() {
    ///excitingFunction();
    ///printMessage();
    ///add();
    ///printf ("\n");
    ///area();
    ///test();
    ///average_of_array();
    ///lowest_age();
    ///matrix();
    ///string();
    ///thing();
    ///multiple();
    ///special();
    ///stringfunctions();
    ///stringcon();
    ///stringcopy();
    ///stringcompare();
    ///userinput();
    ///twoinputs();
    ///takestring();
    ///address();
    ///pointers();
    ///arraypointers();
    ///changearrayointers();
    ///arguments("Oliver");
    ///arguments("John");
    ///arguments("Willem");
    ///multipleargu("Oliver", 16);
    int numbers[5] = {10, 20, 30, 40, 50};
    arrayFunc(numbers);
    
    
    return 0;
}
