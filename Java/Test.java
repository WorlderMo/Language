class Dog {
    public void action() {
        System.out.println("Bark");
    }

}

class Lion {
    public void action() {
        System.out.println("Run");
    }
}

class Bird {
    public void action() {
        System.out.println("Fly");
    }
}

class Fish {
    public void action() {
        System.out.println("Swin");
    }
}

public class AnimalAction {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.action();

        Lion lion = new Lion();
        lion.action();

        Bird bird = new Bird();
        bird.action();

        Fish fish = new Fish();
        fish.action();
    }
}
