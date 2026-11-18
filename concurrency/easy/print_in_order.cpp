#include <semaphore>
#include <functional>

class Foo {
public:
    std::binary_semaphore s2{0}, s3{0};

    Foo() {}

    void first(std::function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        s2.release();
    }

    void second(std::function<void()> printSecond) {
        s2.acquire();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        s3.release();
    }

    void third(std::function<void()> printThird) {
        s3.acquire();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};