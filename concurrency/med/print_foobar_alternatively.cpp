#include <semaphore>
#include <functional>

class FooBar {
private:
    int n;
    std::binary_semaphore s1{0}, s2{1};

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(std::function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            s2.acquire();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            s1.release();
        }
    }

    void bar(std::function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            s1.acquire();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            s2.release();
            
        }
    }
};