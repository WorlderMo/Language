class HelloWorld
end

class << HelloWorld
    def hello(name)
      print name, 'Said hello.'
    end
end

HelloWorld.hello('mohailang')
