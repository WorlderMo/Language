function myFunction(arg1, arg2) {
    this.firstName = arg1;
    this.lastName = arg2;

    function changeName(name) {
        this.lastName = name;
    }
    this.changeName = changeName;
}
// This 创建了新的对象
var x = new myFunction("John", "Doe");
console.log(x.firstName); // 返回 "John"
