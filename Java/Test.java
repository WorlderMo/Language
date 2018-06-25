


//①编写一条打开“oldmast.dat”文件以供输入的语句；使用ObjectInputStream对象的引用inOldmaster来包装一个FileInputStream对象。
    ObjectInputStream inOldmaster = new ObjectInputStream(new FileInputStream("oldmast.dat"));


//②编写一条打开“newmast.dat”文件以供输出的语句；使用ObjectOutputStream对象的引用outNewmaster来包装一个FileOutputStream对象。
    ObjectOutputStream outNewmaster = new ObjectOutputStream(new FileOutputStream("newmast.dat"));


//③编写一条打开“oldmast.dat”文件以供输入的语句，该记录是AccountRecord类的对象record；使用ObjectInputStream对象inOldmaster。
    ObjectInputStream inOldmaster = new ObjectInputStream(new FileInputStream("oldmast.dat"));
    record = (AccountRecord)inOldmaster.readObject();


//④编写一条向文件“newmast.dat”输出记录的语句，该记录是AccountRecord类的对象record。使用ObjectOutputStream对象outNewmaster
    // 来包装一个FileOutputStream对象。
    ObjectOutputStream outNewmaster = new ObjectOutputStream(new FileOutputStream("newmast.dat"));
    outNewmaster.writeObject(record);
