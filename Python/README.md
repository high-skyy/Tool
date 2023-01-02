# Python
Python에서 변수가 저장되는 모든 방식은 Object이다.
> 파이썬에서는 모든 (정수, 실수, 문자열 ...)이 객체로 구현되며 변수는 메모리를 할당하는 것이 아닌
> 해당 object에 이름을 붙이는 것이다.

- Example
```
x = 10
y = x
```

![객체 참조](https://user-images.githubusercontent.com/105041834/210198290-1c985530-ecc3-4b68-9935-f7295d171608.jpg)

> 만약 x의 값을 변화 시키면 그에 해당하는 객체가 또 생성되고 x는 10 객체의 참조를 끊고 11 참조를 한다.

**Python의 경우 Stack을 사용하지 않고 private heap을 사용한다.**

## Design of python
Python is a dynamically typed language.

> Python의 경우에는 동적으로 하나 하나 실행하는 interpreted language에 해당 한다. (Compile)
> 을 사용하지만 결국 PVM에 의해 하나하나 실행되어야 하므로 굳이 data type을 먼저 선언할 이유가 없다.
> 미리 선언을 해야 했으면 굳이 interpreted language가 아닌 compile을 하는 것이 좋다.
> Stack도 존재하지 않는 이유가 바로 이 때문이다. 결국 전부 다 동적으로 해결한다.
> **Interpreted language**는 code 전체가 execution 전에 analyze 되지 않는다.

## Interpreter 언어
The source code of a programming language can be executed using an interpreter or
a compiler. In a compiled language, a compiler will translate the source code
directly into binary machine code. In an interpreted language, ther source code
is not directly run by the target machine. There is another program called the
interpreter that reads and executes the source code directly. The interpreter, 
which is specific to the target machine, translates each statement of the source
code into machine code and runs it.

Python is usually called an interpreted language, however, it combines compiling and
interpreting. When we execute a source code (.py extension) Python first compiles
it into a bytecode. However, it is not the binary machine code and cannot be run
by the target machine directly. In fact, it is a set of instructions for a virtual
machine which is called the Python Virtual Machine.

![PVM](https://user-images.githubusercontent.com/105041834/210201423-c2f94142-f3b4-4f65-a1c1-55dfa00b3009.jpg)

> Interpreted language의 경우에는 target machine에 바로 실행 되지 않고 interpreter라는 
> program에 의해 machine code(byte code)로 translation이 일어나게 된다. Python은 interpreted 언어라고
> 알고 있지만 compiling도 같이 사용한다. Python program을 실행하게 되면 byte code로 먼저 
> compile이 일어나며 이는 machine에 바로 적용이 되는 것이 아니라 PVM(interpreter 장착 되어 있음) 의 instruction으로 작용한다.

- byte code로 모든 instruction을 나타낸다.
- 보통 PVM이 대부분의 일을 하여 PVM을 보통 interpreter라고도 한다.

## Python virtual machine
> 여기서 "virtual machine"은 OS의 virtual machine을 의미 하는게 아니라
> process virtual machine (program)을 의미하는 것으로 programming environment를 의미한다.

Java 의 경우에는 C++ 처럼 data type을 명시하게 되어 있으며 이는 

## Memory Management in Python
### Garbage collector
Garbage collection is a process in which the interpreter frees up the memory
when not in use to make it available for other objects. Assume a case where
no reference is pointing to an object in memory. It is not in use so, the virtual
machine has a garbage collector that automatically deletes that object from the 
heap memory.

> Garbage collection 이라는 process는 아무도 reference 하지 않는 (어떠한 변수도 가리키지 않는)
> object가 있을 경우에는 해당 object를 자동적으로 heap memory에서 삭제 시킨다.

### Reference Counting
Reference counting works by counting the number of times an object is referenced
by other objects in the system. When references to an object are removed, the
reference count for an object is decremented. When the reference count becomes
zero, the object is deallocated.

> Python에서 변수는 객체에 이름을 붙여주는 역할인데 (즉, 참조) 만약 해당 객체를 참조하는 변수가
> 줄어들어서 0이 되면 deallocated 된다. (garbage collector deallocates)

- Example

```
b = 9
b = 4
```
> b = 9 에서 object 9에 참조가 1 증가하고 b = 4가 되면서 object 9의 reference counting
> 이 감소한다.

- Reference cycle
  - reference count가 0가 될 경우에 본인을 찹조하는 object를 만든다.
  - 이렇게 되면 함수가 반환이 되면서 자동적으로 release가 일어나지 않는다.
  - garbage collector의 invoke 전에 free 되지 않는다.

#### Automatic Garbage collection of Cycles
Because reference cycles take computational work to discover, garbage collection
must be a scheduled activity. Python schedules garbage collection based
upon a threshold of object allocations and object deallocations. When the number
of allocations minus the number of deallocations is greater then the threshold 
number the garbage collector is run. 

> 특정 (할당 의 수) - (release의 수) 가 특정 threshold 이상을 넘어가게 되면 garbage collector가 작동한다.
> Reference cycle을 찾는데 computation이 필요하기 때문에 schedule이 되어야 한다.

#### Manual Garbage Collection
- Time-based garbage collection : garbage collector is called after a fixed time interval.
- Event-based garbage collection : calls the garbage collecotr on event occurence.

## Reference
- [Reference](https://ahracho.github.io/posts/python/2017-05-01-everything-in-python-is-object-integer/)
- [Reference](https://www.geeksforgeeks.org/memory-management-in-python/)
- [Reference](https://ko.strephonsays.com/python-and-vs-c-language-3456#:~:text=Python%20%EB%B0%8F%20C%20%EC%96%B8%EC%96%B4%EB%8A%94,%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94%20%EB%B2%94%EC%9A%A9%20%EC%96%B8%EC%96%B4%EC%9E%85%EB%8B%88%EB%8B%A4.)
- [Reference](https://stackoverflow.com/questions/441824/java-virtual-machine-vs-python-interpreter-parlance)
- [Reference](https://towardsdatascience.com/understanding-python-bytecode-e7edaae8734d)
- [Reference](https://www.gkindex.com/python-tutorial/python-virtual-machine.jsp)
- [Reference](https://www.sololearn.com/discuss/2815567/why-we-don-t-use-data-type-in-python-for-declaring-variable/)