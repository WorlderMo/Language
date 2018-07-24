Array.prototype.myUcase = function () {
    for (i = 0; i < this.length; i++) {
        this[i] = this[i].toUpperCase();
    }
}
a = ["a", "b", "c"]
a.myUcase()
console.log(a)
